import reflex as rx
import reflex_enterprise as rxe
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.chat_widget import chat_widget
from app.components.search_bar import search_section
from app.components.scanner import scanner_page
from app.states.medicine_state import MedicineState
from app.states.auth_state import AuthState


def index() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Find Affordable Generic Alternatives",
                    class_name="text-5xl font-black text-center mb-4 mt-20",
                ),
                rx.el.p(
                    "Save up to 90% on your healthcare bills with quality-assured generic medicines.",
                    class_name="text-gray-500 text-center max-w-2xl mx-auto mb-12",
                ),
                search_section(),
                class_name="max-w-7xl mx-auto px-4",
            ),
            class_name="min-h-screen",
        ),
        chat_widget(),
        footer(),
        class_name="font-['Inter']",
    )


def results_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1("Medicine Results", class_name="text-3xl font-bold mb-8"),
                rx.el.p(f"Details for {MedicineState.selected_medicine['brand_name']}"),
                class_name="max-w-7xl mx-auto px-4 py-20",
            )
        ),
        footer(),
    )


def scan() -> rx.Component:
    return rx.el.div(navbar(), scanner_page(), footer())


app = rxe.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400..900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(
    index, route="/", on_load=[AuthState.check_session, AuthState.seed_demo_user]
)
app.add_page(results_page, route="/results", on_load=MedicineState.on_load_results)
app.add_page(scan, route="/scan")