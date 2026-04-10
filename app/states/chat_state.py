import reflex as rx
import asyncio
from app.states.medicine_state import MedicineState


class ChatState(rx.State):
    is_open: bool = False
    is_typing: bool = False
    current_message: str = ""
    messages: list[dict[str, str]] = [
        {
            "role": "bot",
            "content": "Hi! I'm your MedSaver Assistant. I can help you find generic medicines, compare prices, or locate pharmacies. How can I help you today?",
        }
    ]
    suggested_questions: list[str] = [
        "What are generic medicines?",
        "How much can I save?",
        "What is Jan Aushadhi?",
        "Find alternative for Crocin",
        "How to scan a prescription?",
        "Are generic medicines safe?",
    ]

    @rx.event
    def toggle_chat(self):
        self.is_open = not self.is_open

    @rx.event
    async def handle_submit(self, form_data: dict):
        msg = form_data.get("message", "").strip()
        if not msg:
            return
        yield ChatState.process_message(msg)

    @rx.event
    async def send_suggested_question(self, msg: str):
        if not msg:
            return
        yield ChatState.process_message(msg)

    @rx.event
    async def process_message(self, msg: str):
        self.messages.append({"role": "user", "content": msg})
        self.is_typing = True
        yield
        await asyncio.sleep(0.8)
        msg_lower = msg.lower()
        msg_words = [w.strip("!?.,;:'\"") for w in msg_lower.split()]
        response = ""
        new_suggestions = []
        medicine_state = await self.get_state(MedicineState)
        medicines = medicine_state.medicines
        if "what are generic medicines" in msg_lower or "generic medicine" in msg_lower:
            response = "Generic medicines are equivalents of branded drugs. They have the exact same active ingredients (salt composition), dosage, safety, and quality standards, but cost significantly less because manufacturers don't have to repeat the clinical trials or spend on marketing."
            new_suggestions = [
                "Are generic medicines safe?",
                "How much can I save?",
                "Search a medicine",
            ]
        elif "safe" in msg_lower and "generic" in msg_lower:
            response = "Yes, absolutely! Generic medicines approved in India undergo strict quality testing and must meet the same WHO-GMP and DCGI standards as branded medicines. They are just as safe and effective."
            new_suggestions = ["What is Jan Aushadhi?", "Search a medicine"]
        elif "jan aushadhi" in msg_lower or "pmbjp" in msg_lower:
            response = "The Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP) is a government initiative that provides high-quality generic medicines at affordable prices through special kendras across India. We can help you find these stores nearby!"
            new_suggestions = ["Find Jan Aushadhi Kendra", "How much can I save?"]
        elif "how to scan" in msg_lower or "scan prescription" in msg_lower:
            response = "It's easy! Go to the 'Scan Prescription' page, upload a clear photo of your prescription or medicine strip, and our system will automatically read the medicine names and show you the affordable generic alternatives."
            new_suggestions = ["Try scanning now", "Search manually instead"]
        elif "how much" in msg_lower and "save" in msg_lower:
            response = "On average, you can save between 50% to 90% by switching to generic medicines! For example, some common antibiotics that cost ₹200 as a brand might cost just ₹50 as a generic."
            new_suggestions = ["Find alternative for Crocin", "Cheapest medicines"]
        elif (
            "pharmacy" in msg_lower
            or "where to buy" in msg_lower
            or "store" in msg_lower
        ):
            response = "You can find these medicines at generic stores, regular pharmacies, or Jan Aushadhi Kendras. Visit our 'Find Pharmacy' page to see a map of verified stores near your location."
            new_suggestions = ["Find Jan Aushadhi Kendra", "Search a medicine"]
        elif "headache" in msg_lower or "fever" in msg_lower or "pain" in msg_lower:
            response = "For pain and fever, common generic options include Paracetamol (alternative to Crocin/Dolo) or Ibuprofen+Paracetamol (alternative to Combiflam). Always consult your doctor before taking medication."
            new_suggestions = ["Price of Paracetamol", "Price of Combiflam alternative"]
        else:
            found = False
            for m in medicines:
                if (
                    m["brand_name"].lower() in msg_lower
                    or m["generic_name"].lower() in msg_lower
                    or m["salt_composition"].lower() in msg_lower
                ):
                    savings = round(m["brand_price"] - m["generic_price"], 2)
                    pct = round(savings / m["brand_price"] * 100, 1)
                    approval_text = (
                        "It is available at Jan Aushadhi Kendras."
                        if m["is_jan_aushadhi"]
                        else "It is a government-approved generic."
                    )
                    response = f"I found information for **{m['brand_name']}**. \n\nThe generic alternative is **{m['generic_name']}** ({m['salt_composition']}). \n\nThe brand costs ₹{m['brand_price']}, but the generic is only ₹{m['generic_price']}. By switching, you save **₹{savings} ({pct}%)**. \n\n{approval_text}"
                    new_suggestions = [
                        "Find pharmacy near me",
                        "Are generic medicines safe?",
                        "Compare other medicines",
                    ]
                    found = True
                    break
            if found:
                pass
            elif (
                any((word in msg_words for word in ["hi", "hello", "hey"]))
                or "good morning" in msg_lower
            ):
                response = "Hello there! I'm ready to help you save on healthcare. You can ask me about specific medicines, conditions, or how our platform works."
                new_suggestions = [
                    "Find generic alternative",
                    "How much can I save?",
                    "What are generic medicines?",
                ]
            else:
                response = "I couldn't find a specific match for that in my database. Could you try checking the spelling, or ask me something else like 'What is Jan Aushadhi?' or 'How much can I save?'"
                new_suggestions = [
                    "What are generic medicines?",
                    "How to scan a prescription?",
                    "Find pharmacy",
                ]
        self.messages.append({"role": "bot", "content": response})
        if new_suggestions:
            self.suggested_questions = new_suggestions
        self.is_typing = False