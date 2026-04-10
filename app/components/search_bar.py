import reflex as rx
from app.states.medicine_state import MedicineState


def suggestion_item(medicine: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    medicine["brand_name"],
                    class_name="font-semibold text-gray-900 mr-2",
                ),
                rx.el.span(
                    medicine["dosage_form"],
                    class_name="text-[10px] font-bold text-gray-500 bg-gray-100 px-2 py-0.5 rounded-full uppercase tracking-wider",
                ),
                class_name="flex items-center mb-1",
            ),
            rx.el.div(
                rx.el.div(
                    class_name=rx.match(
                        (
                            medicine["brand_price"].to(float)
                            - medicine["generic_price"].to(float)
                        )
                        / medicine["brand_price"].to(float)
                        * 100
                        > 80,
                        (True, "h-2 w-2 rounded-full bg-yellow-500 mr-1.5 shrink-0"),
                        rx.match(
                            (
                                medicine["brand_price"].to(float)
                                - medicine["generic_price"].to(float)
                            )
                            / medicine["brand_price"].to(float)
                            * 100
                            > 60,
                            (True, "h-2 w-2 rounded-full bg-gray-400 mr-1.5 shrink-0"),
                            rx.match(
                                (
                                    medicine["brand_price"].to(float)
                                    - medicine["generic_price"].to(float)
                                )
                                / medicine["brand_price"].to(float)
                                * 100
                                > 40,
                                (
                                    True,
                                    "h-2 w-2 rounded-full bg-orange-400 mr-1.5 shrink-0",
                                ),
                                "h-2 w-2 rounded-full bg-teal-500 mr-1.5 shrink-0",
                            ),
                        ),
                    )
                ),
                rx.el.p(
                    "Generic: " + medicine["generic_name"],
                    class_name="text-xs text-gray-500",
                ),
                class_name="flex items-center",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.span(
                "₹" + medicine["brand_price"].to_string(),
                class_name="text-sm line-through text-gray-400 mr-2",
            ),
            rx.el.span(
                "₹" + medicine["generic_price"].to_string(),
                class_name="text-sm font-bold text-teal-600",
            ),
            class_name="text-right",
        ),
        on_click=lambda: MedicineState.select_medicine(medicine),
        class_name="flex items-center p-3 hover:bg-teal-50 cursor-pointer border-b border-gray-50 last:border-0 transition-colors",
    )


def search_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 h-5 w-5 z-20",
                ),
                rx.el.input(
                    placeholder="Search for a medicine (e.g. Crocin, Augmentin...)",
                    on_change=MedicineState.update_search.debounce(300),
                    class_name="w-full pl-12 pr-4 py-4 rounded-2xl border border-white/50 focus:border-teal-500 focus:ring-4 focus:ring-teal-500/20 outline-none text-lg transition-all shadow-[0_8px_30px_rgb(0,0,0,0.04)] glass-card bg-white/80 backdrop-blur-xl relative z-10",
                    default_value=MedicineState.search_query,
                ),
                rx.el.div(
                    class_name="absolute inset-0 rounded-2xl animate-glow-pulse pointer-events-none z-0"
                ),
                class_name="relative group",
            ),
            rx.cond(
                MedicineState.show_suggestions
                & (MedicineState.filtered_suggestions.length() > 0),
                rx.el.div(
                    rx.foreach(MedicineState.filtered_suggestions, suggestion_item),
                    class_name="absolute top-full left-0 right-0 mt-3 glass-card rounded-2xl shadow-2xl border border-white/60 overflow-hidden z-40 animate-in fade-in slide-in-from-top-2 duration-200",
                ),
            ),
            class_name="relative w-full max-w-2xl mx-auto mt-8",
        ),
        on_blur=MedicineState.hide_suggestions,
        class_name="w-full relative z-30",
    )