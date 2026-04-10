import reflex as rx
from app.states.medicine_state import MedicineState


class DashboardState(rx.State):
    compare_ids: list[int] = []
    show_compare_modal: bool = False

    @rx.var
    async def top_savings_medicines(self) -> list[dict]:
        medicine_state = await self.get_state(MedicineState)
        medicines = medicine_state.medicines
        items = []
        for m in medicines:
            savings_amount = round(m["brand_price"] - m["generic_price"], 2)
            savings_pct = round(savings_amount / m["brand_price"] * 100, 1)
            tier = "Standard"
            if savings_pct > 80:
                tier = "Gold"
            elif savings_pct > 60:
                tier = "Silver"
            elif savings_pct > 40:
                tier = "Bronze"
            items.append(
                {
                    "id": m["id"],
                    "brand_name": m["brand_name"],
                    "generic_name": m["generic_name"],
                    "brand_price": m["brand_price"],
                    "generic_price": m["generic_price"],
                    "savings_pct": savings_pct,
                    "savings_amount": savings_amount,
                    "category": m["category"],
                    "tier": tier,
                    "is_jan_aushadhi": m["is_jan_aushadhi"],
                }
            )
        items.sort(key=lambda x: x["savings_pct"], reverse=True)
        return items[:10]

    @rx.var
    async def category_savings(self) -> list[dict]:
        medicine_state = await self.get_state(MedicineState)
        medicines = medicine_state.medicines
        categories = {}
        for m in medicines:
            cat = m["category"]
            savings_pct = (
                (m["brand_price"] - m["generic_price"]) / m["brand_price"] * 100
            )
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(savings_pct)
        result = []
        for cat, pct_list in categories.items():
            avg = round(sum(pct_list) / len(pct_list), 1)
            result.append({"category": cat, "avg_savings": avg})
        result.sort(key=lambda x: x["avg_savings"], reverse=True)
        return result

    @rx.var
    async def price_distribution(self) -> list[dict]:
        medicine_state = await self.get_state(MedicineState)
        medicines = medicine_state.medicines
        ranges = {"₹0-5": 0, "₹5-15": 0, "₹15-50": 0, "₹50-100": 0, "₹100+": 0}
        for m in medicines:
            price = m["generic_price"]
            if price <= 5:
                ranges["₹0-5"] += 1
            elif price <= 15:
                ranges["₹5-15"] += 1
            elif price <= 50:
                ranges["₹15-50"] += 1
            elif price <= 100:
                ranges["₹50-100"] += 1
            else:
                ranges["₹100+"] += 1
        return [{"range": k, "count": v} for k, v in ranges.items()]

    @rx.var
    async def compare_medicines(self) -> list[dict]:
        medicine_state = await self.get_state(MedicineState)
        return [m for m in medicine_state.medicines if m["id"] in self.compare_ids]

    @rx.var
    async def total_potential_savings(self) -> float:
        medicine_state = await self.get_state(MedicineState)
        return round(
            sum(
                (
                    m["brand_price"] - m["generic_price"]
                    for m in medicine_state.medicines
                )
            ),
            2,
        )

    @rx.var
    async def avg_savings_percentage(self) -> float:
        medicine_state = await self.get_state(MedicineState)
        medicines = medicine_state.medicines
        if not medicines:
            return 0.0
        total_pct = sum(
            (
                (m["brand_price"] - m["generic_price"]) / m["brand_price"] * 100
                for m in medicines
            )
        )
        return round(total_pct / len(medicines), 1)

    @rx.var
    async def jan_aushadhi_count(self) -> int:
        medicine_state = await self.get_state(MedicineState)
        return sum((1 for m in medicine_state.medicines if m["is_jan_aushadhi"]))

    @rx.var
    async def high_alert_count(self) -> int:
        medicine_state = await self.get_state(MedicineState)
        return sum(
            (
                1
                for m in medicine_state.medicines
                if (m["brand_price"] - m["generic_price"]) / m["brand_price"] * 100 > 50
            )
        )

    @rx.var
    async def all_medicines(self) -> list[dict]:
        medicine_state = await self.get_state(MedicineState)
        return medicine_state.medicines

    @rx.event
    def toggle_compare(self, medicine_id: int):
        if medicine_id in self.compare_ids:
            self.compare_ids.remove(medicine_id)
        elif len(self.compare_ids) < 3:
            self.compare_ids.append(medicine_id)

    @rx.event
    def clear_compare(self):
        self.compare_ids = []

    @rx.event
    def toggle_compare_modal(self):
        self.show_compare_modal = not self.show_compare_modal

    @rx.event
    async def navigate_to_medicine(self, medicine_id: int):
        medicine_state = await self.get_state(MedicineState)
        medicine = next(
            (m for m in medicine_state.medicines if m["id"] == medicine_id), None
        )
        if medicine:
            return MedicineState.select_medicine(medicine)