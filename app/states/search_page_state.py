import reflex as rx
from app.states.medicine_state import MedicineState, Medicine


class SearchPageState(rx.State):
    category_filter: str = "All"
    search_text: str = ""
    categories: list[str] = [
        "All",
        "Analgesic",
        "Antibiotic",
        "Pain Relief",
        "Antipyretic",
        "Antacid",
        "NSAID",
        "Antiallergic",
        "Antidiabetic",
        "Antihypertensive",
        "Gastrointestinal",
        "Hormonal",
        "Liver Support",
    ]

    @rx.var
    async def search_results(self) -> list[Medicine]:
        medicine_state = await self.get_state(MedicineState)
        results = medicine_state.medicines
        if self.category_filter != "All":
            results = [m for m in results if m["category"] == self.category_filter]
        if self.search_text:
            q = self.search_text.lower()
            results = [
                m
                for m in results
                if q in m["brand_name"].lower()
                or q in m["generic_name"].lower()
                or q in m["salt_composition"].lower()
            ]
        return results

    @rx.event
    def set_category(self, category: str):
        self.category_filter = category

    @rx.event
    def update_search_text(self, text: str):
        self.search_text = text

    @rx.event
    def select_search_result(self, medicine: dict[str, str | int | float | bool]):
        return MedicineState.select_medicine(medicine)