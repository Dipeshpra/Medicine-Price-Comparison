import reflex as rx
import os
import logging
import asyncio
from app.states.medicine_state import MedicineState


class AICompareState(rx.State):
    ai_comparison_result: str = ""
    ai_loading: bool = False
    ai_error: str = ""
    ai_api_available: bool = False
    has_fetched: bool = False

    @rx.event
    def check_api_key(self):
        key = os.getenv("GOOGLE_API_KEY")
        self.ai_api_available = bool(key)

    @rx.event
    def clear_comparison(self):
        self.ai_comparison_result = ""
        self.ai_error = ""
        self.has_fetched = False

    @rx.event(background=True)
    async def fetch_online_prices(self):
        async with self:
            medicine_state = await self.get_state(MedicineState)
            medicine = medicine_state.selected_medicine
        if not medicine:
            yield rx.toast("No medicine selected for comparison.", duration=3000)
            return
        key = os.getenv("GOOGLE_API_KEY")
        if not key:
            async with self:
                self.ai_error = "To enable AI-powered online price comparison, add your Google API key in Settings → Integrations"
                self.ai_loading = False
            return
        async with self:
            self.ai_loading = True
            self.ai_error = ""
            self.ai_comparison_result = ""
            self.has_fetched = True
        try:
            from google import genai
            from google.genai import types

            prompt = f'''You are a pharmaceutical price comparison assistant for Indian online pharmacies.\n\nFor the medicine "{medicine.get("brand_name")}" ({medicine.get("salt_composition")}, {medicine.get("dosage_form")} {medicine.get("dosage_strength")}):\n\n1. List the approximate current prices on these major Indian online pharmacies:\n   - 1mg (Tata 1mg)\n   - PharmEasy\n   - Netmeds\n   - Apollo Pharmacy Online\n   - MedPlus\n\n2. For each store, provide:\n   - Store name\n   - Approximate price (₹) for a standard pack\n   - Pack size (e.g., strip of 10, bottle of 100ml)\n   - Availability status (Available / Likely Available / Check Store)\n\n3. Also mention the generic alternative "{medicine.get("generic_name")}" prices if available on these platforms.\n\n4. End with a brief "💡 Best Deal" recommendation.\n\nFormat your response in clean markdown with a table. Use ₹ symbol for prices.\nKeep it concise and practical.'''
            models_to_try = ["gemini-2.5-flash", "gemini-2.5-flash-lite"]
            last_error = None
            for model_name in models_to_try:
                for attempt in range(3):
                    try:
                        client = genai.Client(api_key=key)
                        response_stream = (
                            await client.aio.models.generate_content_stream(
                                model=model_name,
                                contents=prompt,
                                config=types.GenerateContentConfig(
                                    temperature=0.3, max_output_tokens=1500
                                ),
                            )
                        )
                        async for chunk in response_stream:
                            if chunk.text:
                                async with self:
                                    self.ai_comparison_result += chunk.text
                                    yield
                        last_error = None
                        break
                    except Exception as e:
                        logging.exception("Unexpected error")
                        last_error = e
                        error_str = str(e)
                        if any(
                            (
                                x in error_str.upper()
                                for x in [
                                    "503",
                                    "429",
                                    "UNAVAILABLE",
                                    "OVERLOADED",
                                    "INTERNAL ERROR",
                                ]
                            )
                        ):
                            async with self:
                                self.ai_comparison_result = ""
                                if attempt < 2:
                                    yield rx.toast(
                                        f"Server busy. Retrying... (Attempt {attempt + 2}/3)",
                                        duration=2000,
                                    )
                                elif model_name != models_to_try[-1]:
                                    yield rx.toast(
                                        "Switching to alternate model...", duration=2000
                                    )
                            await asyncio.sleep(2)
                            continue
                        else:
                            break
                if last_error is None:
                    break
            if last_error:
                async with self:
                    self.ai_error = "Online pharmacies are busy right now. Please try again in a moment."
                    logging.error(f"AI Comparison final error: {last_error}")
        except ImportError:
            async with self:
                self.ai_error = "The google-genai library is not installed."
                logging.error("google-genai is missing")
        except Exception as e:
            async with self:
                self.ai_error = f"Error fetching AI prices: {str(e)}"
                logging.exception(f"Error in fetch_online_prices: {e}")
        finally:
            async with self:
                self.ai_loading = False