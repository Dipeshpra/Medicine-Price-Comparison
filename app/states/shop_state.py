import reflex as rx
from typing import TypedDict
import time
import random
from app.states.medicine_state import MedicineState


class CartItem(TypedDict):
    id: int
    brand_name: str
    generic_name: str
    salt_composition: str
    price: float
    brand_price: float
    quantity: int
    dosage_form: str
    dosage_strength: str
    is_jan_aushadhi: bool


class Order(TypedDict):
    order_id: str
    items: list[CartItem]
    total: float
    delivery_address: str
    payment_method: str
    status: str
    created_at: str


class ShopState(rx.State):
    cart_items: list[CartItem] = []
    orders: list[Order] = []
    delivery_name: str = ""
    delivery_phone: str = ""
    delivery_address: str = ""
    delivery_city: str = ""
    delivery_pincode: str = ""
    payment_method: str = "cod"
    checkout_error: str = ""
    shop_search: str = ""
    shop_category: str = "All"
    shop_sort: str = "savings"
    show_cart_drawer: bool = False
    order_placed: bool = False
    last_order_id: str = ""

    @rx.var
    def cart_count(self) -> int:
        return sum((item["quantity"] for item in self.cart_items))

    @rx.var
    def cart_total(self) -> float:
        return round(
            sum((item["price"] * item["quantity"] for item in self.cart_items)), 2
        )

    @rx.var
    def cart_brand_total(self) -> float:
        return round(
            sum((item["brand_price"] * item["quantity"] for item in self.cart_items)), 2
        )

    @rx.var
    def cart_savings(self) -> float:
        return round(self.cart_brand_total - self.cart_total, 2)

    @rx.var
    def delivery_fee(self) -> float:
        if self.cart_total >= 199:
            return 0.0
        return 49.0

    @rx.var
    def order_total(self) -> float:
        return round(self.cart_total + self.delivery_fee, 2)

    @rx.var
    async def shop_medicines(self) -> list[dict]:
        medicine_state = await self.get_state(MedicineState)
        results = medicine_state.medicines
        if self.shop_category != "All":
            results = [m for m in results if m["category"] == self.shop_category]
        if self.shop_search:
            q = self.shop_search.lower()
            results = [
                m
                for m in results
                if q in m["brand_name"].lower() or q in m["generic_name"].lower()
            ]
        if self.shop_sort == "savings":
            results.sort(
                key=lambda x: (x["brand_price"] - x["generic_price"])
                / x["brand_price"],
                reverse=True,
            )
        elif self.shop_sort == "price_low":
            results.sort(key=lambda x: x["generic_price"])
        elif self.shop_sort == "price_high":
            results.sort(key=lambda x: x["generic_price"], reverse=True)
        elif self.shop_sort == "name":
            results.sort(key=lambda x: x["generic_name"])
        return results

    @rx.event
    def add_to_cart(self, medicine: dict):
        med_id = int(medicine.get("id", 0))
        for i, item in enumerate(self.cart_items):
            if item["id"] == med_id:
                self.cart_items[i]["quantity"] += 1
                return rx.toast(
                    f"Updated quantity for {medicine['generic_name']}", duration=2000
                )
        self.cart_items.append(
            {
                "id": med_id,
                "brand_name": str(medicine.get("brand_name", "")),
                "generic_name": str(medicine.get("generic_name", "")),
                "salt_composition": str(medicine.get("salt_composition", "")),
                "price": float(medicine.get("generic_price", 0)),
                "brand_price": float(medicine.get("brand_price", 0)),
                "quantity": 1,
                "dosage_form": str(medicine.get("dosage_form", "")),
                "dosage_strength": str(medicine.get("dosage_strength", "")),
                "is_jan_aushadhi": bool(medicine.get("is_jan_aushadhi", False)),
            }
        )
        return rx.toast(f"Added {medicine['generic_name']} to cart! 🛒", duration=2000)

    @rx.event
    def remove_from_cart(self, med_id: int):
        self.cart_items = [item for item in self.cart_items if item["id"] != med_id]
        return rx.toast("Item removed from cart", duration=2000)

    @rx.event
    def increment_qty(self, med_id: int):
        for i, item in enumerate(self.cart_items):
            if item["id"] == med_id:
                self.cart_items[i]["quantity"] += 1
                break

    @rx.event
    def decrement_qty(self, med_id: int):
        for i, item in enumerate(self.cart_items):
            if item["id"] == med_id:
                if item["quantity"] > 1:
                    self.cart_items[i]["quantity"] -= 1
                else:
                    self.cart_items = [
                        it for it in self.cart_items if it["id"] != med_id
                    ]
                break

    @rx.event
    def clear_cart(self):
        self.cart_items = []

    @rx.event
    def toggle_cart_drawer(self):
        self.show_cart_drawer = not self.show_cart_drawer

    @rx.event
    def set_delivery_field(self, field: str, value: str):
        setattr(self, f"delivery_{field}", value)

    @rx.event
    def set_payment_method(self, method: str):
        self.payment_method = method

    @rx.event
    def place_order(self, form_data: dict):
        name = form_data.get("name", "").strip()
        phone = form_data.get("phone", "").strip()
        address = form_data.get("address", "").strip()
        city = form_data.get("city", "").strip()
        pincode = form_data.get("pincode", "").strip()
        payment_method = form_data.get("payment_method", "cod")
        self.payment_method = payment_method
        if not all([name, phone, address, city, pincode]):
            self.checkout_error = "Please fill in all delivery details"
            return
        if not self.cart_items:
            self.checkout_error = "Your cart is empty"
            return
        order_id = f"MED{int(time.time())}{random.randint(100, 999)}"
        order = {
            "order_id": order_id,
            "items": list(self.cart_items),
            "total": self.order_total,
            "delivery_address": f"{name}, {address}, {city} - {pincode}, Phone: {phone}",
            "payment_method": self.payment_method,
            "status": "Confirmed",
            "created_at": time.strftime("%Y-%m-%d %H:%M"),
        }
        self.orders.insert(0, order)
        self.last_order_id = order_id
        self.order_placed = True
        self.cart_items = []
        self.checkout_error = ""
        return [rx.toast(f"Order #{order_id} placed successfully! 🎉", duration=5000)]

    @rx.event
    def reset_order_placed(self):
        self.order_placed = False

    @rx.event
    def update_shop_search(self, val: str):
        self.shop_search = val

    @rx.event
    def set_shop_category(self, val: str):
        self.shop_category = val

    @rx.event
    def set_shop_sort(self, val: str):
        self.shop_sort = val

    @rx.event
    def go_to_checkout(self):
        return rx.redirect("/checkout")

    @rx.event
    def continue_shopping(self):
        self.order_placed = False
        return rx.redirect("/shop")