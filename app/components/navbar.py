import reflex as rx
from app.states.medicine_state import MedicineState


def nav_link(label: str, route: str) -> rx.Component:
    is_active = MedicineState.active_nav == route
    return rx.el.a(
        label,
        on_click=lambda: MedicineState.set_nav(route),
        class_name=rx.cond(
            is_active,
            "gradient-text font-bold border-b-2 border-teal-500 px-1 py-4 transition-all relative after:absolute after:bottom-0 after:left-0 after:w-full after:h-0.5 after:bg-gradient-to-r after:from-teal-500 after:to-emerald-500",
            "text-gray-600 font-medium hover:text-teal-600 px-1 py-4 transition-all relative after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 after:bg-gradient-to-r after:from-teal-500 after:to-emerald-500 hover:after:w-full after:transition-all after:duration-300",
        ),
        href="javascript:void(0)",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.nav(
            rx.el.div(
                class_name="h-[2px] w-full bg-gradient-to-r from-teal-500 via-emerald-500 to-cyan-500 absolute top-0 left-0"
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("shield-plus", class_name="h-5 w-5 text-white"),
                        class_name="bg-gradient-to-br from-teal-500 to-emerald-500 p-1.5 rounded-xl shadow-lg shadow-teal-500/30 group-hover:animate-pulse",
                    ),
                    rx.el.span(
                        "MedSaver",
                        class_name="text-2xl font-black tracking-tight text-gray-900",
                    ),
                    rx.el.span(
                        rx.icon("sparkles", class_name="h-3 w-3 mr-1 text-white"),
                        "AI Powered",
                        class_name="hidden sm:flex items-center text-[10px] font-bold uppercase tracking-wider bg-gradient-to-r from-cyan-500 to-teal-500 text-white px-2 py-0.5 rounded-full ml-2 shadow-sm animate-shimmer",
                    ),
                    class_name="flex items-center gap-2 cursor-pointer group",
                    on_click=lambda: MedicineState.set_nav("/"),
                ),
                rx.el.div(
                    nav_link("Home", "/"),
                    nav_link("Search", "/search"),
                    nav_link("Insights", "/insights"),
                    nav_link("Scan Prescription", "/scan"),
                    nav_link("Find Pharmacy", "/pharmacies"),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.button(
                    rx.icon("menu", class_name="h-6 w-6"),
                    on_click=MedicineState.toggle_mobile_menu,
                    class_name="md:hidden p-2 text-gray-600 hover:text-teal-600 transition-colors",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-16 relative z-10",
            ),
            rx.cond(
                MedicineState.is_mobile_menu_open,
                rx.el.div(
                    rx.el.div(
                        nav_link("Home", "/"),
                        nav_link("Search", "/search"),
                        nav_link("Insights", "/insights"),
                        nav_link("Scan Prescription", "/scan"),
                        nav_link("Find Pharmacy", "/pharmacies"),
                        class_name="flex flex-col px-4 py-6 space-y-4 bg-white/95 backdrop-blur-xl border-t border-white/50 shadow-2xl",
                    ),
                    class_name="md:hidden absolute w-full left-0 top-16 z-40 animate-in slide-in-from-top-4 fade-in duration-300",
                ),
            ),
            class_name="bg-white/70 backdrop-blur-xl border-b border-white/50 sticky top-0 z-50 shadow-[0_4px_30px_rgba(0,0,0,0.03)] w-full transition-all",
        )
    )