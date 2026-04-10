import reflex as rx
from app.states.medicine_state import MedicineState


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            class_name="h-1 w-full bg-gradient-to-r from-teal-500 via-emerald-500 to-cyan-500"
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon("shield-plus", class_name="h-6 w-6 text-white"),
                            class_name="bg-gradient-to-br from-teal-500 to-emerald-500 p-1.5 rounded-xl shadow-md",
                        ),
                        rx.el.span(
                            "MedSaver", class_name="text-2xl font-black text-gray-900"
                        ),
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        "Empowering citizens to access quality medicines at affordable prices through generic alternatives.",
                        class_name="text-gray-500 text-sm leading-relaxed",
                    ),
                    rx.el.div(
                        rx.el.span("Made with ", class_name="text-sm text-gray-500"),
                        rx.icon(
                            "heart",
                            class_name="h-4 w-4 text-red-500 mx-1 animate-pulse fill-red-500",
                        ),
                        rx.el.span(
                            " for affordable healthcare",
                            class_name="text-sm text-gray-500",
                        ),
                        class_name="flex items-center mt-6",
                    ),
                    class_name="col-span-1 lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.h4("Quick Links", class_name="font-bold mb-6 text-gray-900"),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.button(
                                "Shop Medicines",
                                on_click=lambda: MedicineState.set_nav("/shop"),
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "About Jan Aushadhi",
                                href="#",
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        rx.el.li(
                            rx.el.button(
                                "Find Pharmacy",
                                on_click=lambda: MedicineState.set_nav("/pharmacies"),
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        rx.el.li(
                            rx.el.button(
                                "Scan Prescription",
                                on_click=lambda: MedicineState.set_nav("/scan"),
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        class_name="space-y-3 text-sm font-medium",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4("Support", class_name="font-bold mb-6 text-gray-900"),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "Contact Us",
                                href="#",
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Terms of Service",
                                href="#",
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "Privacy Policy",
                                href="#",
                                class_name="text-gray-500 hover:text-teal-600 transition-colors hover:translate-x-1 inline-block",
                            )
                        ),
                        class_name="space-y-3 text-sm font-medium",
                    ),
                    class_name="col-span-1",
                ),
                rx.el.div(
                    rx.el.h4("Newsletter", class_name="font-bold mb-6 text-gray-900"),
                    rx.el.p(
                        "Subscribe to get the latest medicine price drop alerts.",
                        class_name="text-sm text-gray-500 mb-4",
                    ),
                    rx.el.div(
                        rx.el.input(
                            placeholder="Enter your email",
                            class_name="w-full px-4 py-2 bg-white/50 border border-gray-200 rounded-l-xl focus:outline-none focus:ring-2 focus:ring-teal-500/50",
                        ),
                        rx.el.button(
                            rx.icon("send", class_name="h-4 w-4"),
                            class_name="bg-gradient-to-r from-teal-500 to-emerald-500 text-white px-4 py-2 rounded-r-xl hover:opacity-90 transition-opacity",
                        ),
                        class_name="flex shadow-sm",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.icon("twitter", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-400 hover:text-teal-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("facebook", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-400 hover:text-teal-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("instagram", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-400 hover:text-teal-500 transition-colors",
                        ),
                        rx.el.a(
                            rx.icon("linkedin", class_name="h-5 w-5"),
                            href="#",
                            class_name="text-gray-400 hover:text-teal-500 transition-colors",
                        ),
                        class_name="flex gap-4 mt-6",
                    ),
                    class_name="col-span-1 lg:col-span-2",
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-6 gap-12",
            ),
            rx.el.div(
                rx.el.p(
                    "© 2024 MedSaver Intelligence. Data verified by Health Ministry Guidelines.",
                    class_name="text-sm font-medium gradient-text",
                ),
                rx.el.button(
                    "Back to top",
                    rx.icon("arrow-up", class_name="h-4 w-4 ml-1"),
                    on_click=rx.call_script(
                        "window.scrollTo({top: 0, behavior: 'smooth'})"
                    ),
                    class_name="text-sm text-gray-500 hover:text-teal-600 flex items-center transition-colors",
                ),
                class_name="mt-16 pt-8 border-t border-gray-200/50 flex flex-col md:flex-row justify-between items-center gap-4",
            ),
            class_name="max-w-7xl mx-auto px-4 py-16 relative z-10",
        ),
        class_name="bg-gradient-to-b from-gray-50/50 to-gray-100/50 mt-20 relative overflow-hidden",
    )