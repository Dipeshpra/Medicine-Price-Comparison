import reflex as rx
from typing import Any
from app.states.medicine_state import MedicineState, Medicine
import logging


class ScanState(rx.State):
    uploading: bool = False
    processing: bool = False
    uploaded_image: str = ""
    raw_text: str = ""
    detected_medicines: list[Medicine] = []

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return
        file = files[0]
        upload_data = await file.read()
        upload_dir = rx.get_upload_dir()
        upload_dir.mkdir(parents=True, exist_ok=True)
        import uuid

        unique_name = f"{uuid.uuid4().hex[:8]}_{file.name}"
        file_path = upload_dir / unique_name
        with file_path.open("wb") as f:
            f.write(upload_data)
        self.uploaded_image = unique_name
        self.raw_text = ""
        self.detected_medicines = []
        yield rx.toast("Image uploaded successfully! Starting OCR...", duration=3000)
        yield ScanState.process_ocr

    @rx.event(background=True)
    async def process_ocr(self):
        async with self:
            self.processing = True
        try:
            import pytesseract
            from PIL import Image

            async with self:
                file_path = rx.get_upload_dir() / self.uploaded_image
            img = Image.open(file_path)
            text = pytesseract.image_to_string(img)
            async with self:
                self.raw_text = text.strip() or "No text detected."
                medicine_state = await self.get_state(MedicineState)
                medicines = medicine_state.medicines
                detected = []
                text_lower = text.lower()
                for m in medicines:
                    if (
                        m["brand_name"].lower() in text_lower
                        or m["generic_name"].lower() in text_lower
                    ):
                        if m not in detected:
                            detected.append(m)
                self.detected_medicines = detected
                if not detected:
                    yield rx.toast(
                        "No matching medicines found in the prescription.",
                        duration=4000,
                    )
                else:
                    yield rx.toast(f"Found {len(detected)} medicine(s)!", duration=4000)
        except Exception as e:
            logging.exception(f"OCR Error: {e}")
            async with self:
                self.raw_text = f"Error during processing: {str(e)}"
                yield rx.toast("Error processing image.", duration=4000)
        finally:
            async with self:
                self.processing = False

    @rx.event
    def select_scanned_medicine(self, medicine: dict[str, str | int | float | bool]):
        return MedicineState.select_medicine(medicine)