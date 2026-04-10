import reflex as rx
import reflex_enterprise as rxe
from app.states.medicine_state import MedicineState
from app.states.pharmacy_state import PharmacyState
from app.states.search_page_state import SearchPageState
from app.states.dashboard_state import DashboardState
from app.states.ai_compare_state import AICompareState
from app.states.smart_features_state import SmartFeaturesState
from app.states.shop_state import ShopState
from app.components.navbar import navbar
from app.components.search_bar import search_section
from app.components.footer import footer
from app.components.chat_widget import chat_widget
from app.components.scanner import scanner_page
from app.states.auth_state import AuthState


def login_page() -> rx.Component:
    return rx.el.main(
        rx.el.header(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("shield-plus", class_name="h-5 w-5 text-white"),
                        class_name="bg-gradient-to-br from-teal-500 to-emerald-500 p-1.5 rounded-xl shadow-lg",
                    ),
                    rx.el.span(
                        "MedSaver", class_name="text-xl font-black text-gray-900"
                    ),
                    class_name="flex items-center gap-2 cursor-pointer",
                    on_click=lambda: rx.redirect("/"),
                ),
                class_name="max-w-7xl mx-auto px-4 h-16 flex items-center",
            ),
            class_name="bg-white/70 backdrop-blur-xl border-b border-gray-100 sticky top-0 z-50",
        ),
        rx.el.div(
            rx.el.div(
                class_name="absolute top-0 left-0 w-full h-[500px] bg-gradient-to-b from-teal-50 to-white -z-10"
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.button(
                                "Login",
                                on_click=AuthState.toggle_auth_tab,
                                class_name=rx.cond(
                                    AuthState.show_login,
                                    "flex-1 py-4 text-sm font-black text-teal-600 border-b-2 border-teal-500",
                                    "flex-1 py-4 text-sm font-bold text-gray-400 border-b-2 border-transparent hover:text-gray-600",
                                ),
                            ),
                            rx.el.button(
                                "Sign Up",
                                on_click=AuthState.toggle_auth_tab,
                                class_name=rx.cond(
                                    ~AuthState.show_login,
                                    "flex-1 py-4 text-sm font-black text-teal-600 border-b-2 border-teal-500",
                                    "flex-1 py-4 text-sm font-bold text-gray-400 border-b-2 border-transparent hover:text-gray-600",
                                ),
                            ),
                            class_name="flex border-b border-gray-100 mb-8",
                        ),
                        rx.cond(
                            AuthState.show_login,
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h2(
                                        "Welcome Back",
                                        class_name="text-2xl font-black text-gray-900 mb-2",
                                    ),
                                    rx.el.p(
                                        "Save more on your healthcare today.",
                                        class_name="text-gray-500 text-sm mb-8",
                                    ),
                                    class_name="text-center",
                                ),
                                rx.el.form(
                                    rx.el.div(
                                        rx.el.label(
                                            "Email Address",
                                            class_name="block text-xs font-black text-gray-400 uppercase tracking-widest mb-2",
                                        ),
                                        rx.el.div(
                                            rx.icon(
                                                "mail",
                                                class_name="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400",
                                            ),
                                            rx.el.input(
                                                name="email",
                                                placeholder="Enter your email",
                                                class_name="w-full pl-12 pr-4 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                            ),
                                            class_name="relative",
                                        ),
                                        class_name="mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.label(
                                                "Password",
                                                class_name="text-xs font-black text-gray-400 uppercase tracking-widest",
                                            ),
                                            rx.el.a(
                                                "Forgot?",
                                                href="#",
                                                class_name="text-xs font-bold text-teal-600 hover:text-teal-700",
                                            ),
                                            class_name="flex justify-between items-center mb-2",
                                        ),
                                        rx.el.div(
                                            rx.icon(
                                                "lock",
                                                class_name="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400",
                                            ),
                                            rx.el.input(
                                                name="password",
                                                type=rx.cond(
                                                    AuthState.show_password,
                                                    "text",
                                                    "password",
                                                ),
                                                placeholder="••••••••",
                                                class_name="w-full pl-12 pr-12 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                            ),
                                            rx.el.button(
                                                rx.icon(
                                                    rx.cond(
                                                        AuthState.show_password,
                                                        "eye-off",
                                                        "eye",
                                                    ),
                                                    class_name="h-4 w-4 text-gray-400",
                                                ),
                                                on_click=AuthState.toggle_password_visibility,
                                                type="button",
                                                class_name="absolute right-4 top-1/2 -translate-y-1/2 hover:text-teal-600",
                                            ),
                                            class_name="relative",
                                        ),
                                        class_name="mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            rx.el.input(
                                                type="checkbox",
                                                class_name="mr-2 rounded border-gray-300 text-teal-600 focus:ring-teal-500",
                                            ),
                                            rx.el.span(
                                                "Remember me",
                                                class_name="text-sm text-gray-600 font-medium",
                                            ),
                                            class_name="flex items-center cursor-pointer",
                                        ),
                                        class_name="mb-8",
                                    ),
                                    rx.cond(
                                        AuthState.login_error != "",
                                        rx.el.div(
                                            rx.icon(
                                                "circle_alert",
                                                class_name="h-4 w-4 mr-2",
                                            ),
                                            AuthState.login_error,
                                            class_name="flex items-center p-3 bg-red-50 text-red-600 text-xs font-bold rounded-xl mb-6",
                                        ),
                                    ),
                                    rx.el.button(
                                        "Sign In",
                                        type="submit",
                                        class_name="w-full py-4 bg-gradient-to-r from-teal-500 to-emerald-500 text-white font-black rounded-xl shadow-lg shadow-teal-500/20 hover:opacity-90 transition-all",
                                    ),
                                    on_submit=AuthState.handle_login,
                                ),
                                rx.el.div(
                                    rx.el.div(class_name="h-px bg-gray-100 flex-1"),
                                    rx.el.span(
                                        "OR",
                                        class_name="px-4 text-[10px] font-black text-gray-300",
                                    ),
                                    rx.el.div(class_name="h-px bg-gray-100 flex-1"),
                                    class_name="flex items-center my-8",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "Demo Access:",
                                        class_name="text-[10px] font-black text-gray-400 uppercase mb-2",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Email: demo@medsaver.com",
                                            class_name="text-xs font-bold text-teal-800",
                                        ),
                                        rx.el.p(
                                            "Pass: demo123",
                                            class_name="text-xs font-bold text-teal-800",
                                        ),
                                        class_name="p-3 bg-teal-50 rounded-xl border border-teal-100",
                                    ),
                                ),
                                class_name="animate-in fade-in slide-in-from-left-4 duration-300",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h2(
                                        "Create Account",
                                        class_name="text-2xl font-black text-gray-900 mb-2",
                                    ),
                                    rx.el.p(
                                        "Join 10,000+ users saving on meds.",
                                        class_name="text-gray-500 text-sm mb-8",
                                    ),
                                    class_name="text-center",
                                ),
                                rx.el.form(
                                    rx.el.div(
                                        rx.el.label(
                                            "Full Name",
                                            class_name="block text-xs font-black text-gray-400 uppercase tracking-widest mb-2",
                                        ),
                                        rx.el.input(
                                            name="name",
                                            placeholder="John Doe",
                                            class_name="w-full px-4 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                        ),
                                        class_name="mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            "Email Address",
                                            class_name="block text-xs font-black text-gray-400 uppercase tracking-widest mb-2",
                                        ),
                                        rx.el.input(
                                            name="email",
                                            type="email",
                                            placeholder="john@example.com",
                                            class_name="w-full px-4 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                        ),
                                        class_name="mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            "Phone Number",
                                            class_name="block text-xs font-black text-gray-400 uppercase tracking-widest mb-2",
                                        ),
                                        rx.el.input(
                                            name="phone",
                                            placeholder="+91-0000000000",
                                            class_name="w-full px-4 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                        ),
                                        class_name="mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            "Create Password",
                                            class_name="block text-xs font-black text-gray-400 uppercase tracking-widest mb-2",
                                        ),
                                        rx.el.input(
                                            name="password",
                                            type="password",
                                            placeholder="Min. 6 characters",
                                            class_name="w-full px-4 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                        ),
                                        class_name="mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.label(
                                            "Confirm Password",
                                            class_name="block text-xs font-black text-gray-400 uppercase tracking-widest mb-2",
                                        ),
                                        rx.el.input(
                                            name="confirm_password",
                                            type="password",
                                            placeholder="••••••••",
                                            class_name="w-full px-4 py-3 bg-gray-50 border border-gray-100 rounded-xl focus:ring-2 focus:ring-teal-500/20 focus:border-teal-500 outline-none transition-all",
                                        ),
                                        class_name="mb-8",
                                    ),
                                    rx.cond(
                                        AuthState.signup_error != "",
                                        rx.el.div(
                                            rx.icon(
                                                "circle_alert",
                                                class_name="h-4 w-4 mr-2",
                                            ),
                                            AuthState.signup_error,
                                            class_name="flex items-center p-3 bg-red-50 text-red-600 text-xs font-bold rounded-xl mb-6",
                                        ),
                                    ),
                                    rx.el.button(
                                        "Create Account",
                                        type="submit",
                                        class_name="w-full py-4 bg-gradient-to-r from-teal-500 to-emerald-500 text-white font-black rounded-xl shadow-lg shadow-teal-500/20 hover:opacity-90 transition-all",
                                    ),
                                    on_submit=AuthState.handle_signup,
                                ),
                                class_name="animate-in fade-in slide-in-from-right-4 duration-300",
                            ),
                        ),
                        class_name="bg-white/80 backdrop-blur-2xl p-8 md:p-12 rounded-[2.5rem] shadow-[0_20px_50px_rgba(0,0,0,0.05)] border border-white/50 w-full max-w-md",
                    ),
                    class_name="flex-1 flex flex-col items-center justify-center p-4 min-h-[calc(100vh-64px)]",
                )
            ),
        ),
        class_name="min-h-screen bg-white font-['Inter']",
    )


def stat_card(icon_name: str, value: str, label: str, delay: str = "") -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon_name, class_name="h-6 w-6 text-white"),
            class_name="p-3 bg-gradient-to-br from-teal-500 to-emerald-500 rounded-2xl mb-4 w-fit shadow-md",
        ),
        rx.el.h3(
            value,
            class_name="text-4xl font-black gradient-text tabular-nums tracking-tight",
        ),
        rx.el.p(label, class_name="text-gray-500 font-semibold mt-1"),
        class_name=f"p-6 glass-card hover-lift card-shine rounded-3xl animate-fade-in-up{delay}",
    )


def step_card(icon_name: str, title: str, desc: str, step_num: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                step_num,
                class_name="absolute -top-3 -right-3 h-8 w-8 bg-gradient-to-r from-teal-500 to-emerald-500 text-white rounded-full flex items-center justify-center font-black text-sm border-4 border-white shadow-sm z-10",
            ),
            rx.icon(icon_name, class_name="h-8 w-8 text-white"),
            class_name="relative h-16 w-16 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-2xl flex items-center justify-center mb-6 shadow-lg shadow-teal-500/20 group-hover:scale-110 transition-transform duration-300",
        ),
        rx.el.h4(title, class_name="text-xl font-bold text-gray-900 mb-3"),
        rx.el.p(desc, class_name="text-gray-500 text-sm leading-relaxed"),
        class_name="relative p-8 flex flex-col items-center text-center glass-card rounded-3xl hover-lift group animate-fade-in-up",
    )


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    class_name="absolute top-0 left-10 w-[400px] h-[400px] bg-teal-300/20 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-float"
                ),
                rx.el.div(
                    class_name="absolute top-20 right-10 w-[400px] h-[400px] bg-emerald-200/30 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-float-delayed"
                ),
                rx.el.div(
                    class_name="absolute -bottom-8 left-40 w-[400px] h-[400px] bg-cyan-100/20 rounded-full mix-blend-multiply filter blur-3xl opacity-70 animate-float-slow"
                ),
                class_name="absolute inset-0 overflow-hidden pointer-events-none z-0",
            ),
            rx.el.div(
                rx.icon(
                    "pill",
                    class_name="absolute top-1/4 left-1/4 h-8 w-8 text-teal-400/40 animate-bounce-gentle rotate-45",
                ),
                rx.icon(
                    "activity",
                    class_name="absolute top-1/3 right-1/4 h-10 w-10 text-emerald-400/30 animate-float-delayed",
                ),
                rx.icon(
                    "heart-pulse",
                    class_name="absolute bottom-1/4 left-1/3 h-6 w-6 text-cyan-400/40 animate-float",
                ),
                class_name="absolute inset-0 pointer-events-none z-0",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            rx.icon(
                                "sparkles", class_name="h-4 w-4 mr-2 text-teal-500"
                            ),
                            "Healthcare for All",
                            class_name="flex items-center px-4 py-1.5 rounded-full bg-white/60 backdrop-blur-md border border-teal-200 text-teal-700 text-sm font-bold uppercase tracking-wider shadow-sm animate-shimmer",
                        ),
                        class_name="flex justify-center mb-6 animate-fade-in-up-1",
                    ),
                    rx.el.h1(
                        "Find ",
                        rx.el.span("Affordable Medicine", class_name="gradient-text"),
                        " Alternatives",
                        class_name="text-5xl md:text-7xl font-extrabold text-gray-900 mt-4 leading-tight tracking-tight animate-fade-in-up-2",
                    ),
                    rx.el.p(
                        "Switch to high-quality generic medicines and save up to 90% on your healthcare costs. Verified by Government standards.",
                        class_name="text-xl text-gray-600 mt-8 max-w-2xl mx-auto leading-relaxed animate-fade-in-up-3",
                    ),
                    rx.el.div(search_section(), class_name="animate-fade-in-up-4 mt-8"),
                    rx.el.div(
                        rx.el.p(
                            "Trusted by 10,000+ users",
                            class_name="text-sm font-bold text-gray-500 mb-3",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.image(
                                    src="https://api.dicebear.com/9.x/notionists/svg?seed=user1",
                                    class_name="size-8 rounded-full border-2 border-white -ml-2 first:ml-0 bg-teal-50",
                                ),
                                rx.image(
                                    src="https://api.dicebear.com/9.x/notionists/svg?seed=user2",
                                    class_name="size-8 rounded-full border-2 border-white -ml-2 bg-emerald-50",
                                ),
                                rx.image(
                                    src="https://api.dicebear.com/9.x/notionists/svg?seed=user3",
                                    class_name="size-8 rounded-full border-2 border-white -ml-2 bg-cyan-50",
                                ),
                                rx.image(
                                    src="https://api.dicebear.com/9.x/notionists/svg?seed=user4",
                                    class_name="size-8 rounded-full border-2 border-white -ml-2 bg-blue-50",
                                ),
                                class_name="flex",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "star",
                                    class_name="h-4 w-4 text-yellow-400 fill-yellow-400",
                                ),
                                rx.icon(
                                    "star",
                                    class_name="h-4 w-4 text-yellow-400 fill-yellow-400",
                                ),
                                rx.icon(
                                    "star",
                                    class_name="h-4 w-4 text-yellow-400 fill-yellow-400",
                                ),
                                rx.icon(
                                    "star",
                                    class_name="h-4 w-4 text-yellow-400 fill-yellow-400",
                                ),
                                rx.icon(
                                    "star",
                                    class_name="h-4 w-4 text-yellow-400 fill-yellow-400",
                                ),
                                class_name="flex gap-1 ml-4",
                            ),
                            class_name="flex items-center justify-center",
                        ),
                        class_name="mt-12 flex flex-col items-center animate-fade-in-up-4",
                    ),
                    class_name="text-center py-24 px-4 relative z-10",
                ),
                class_name="max-w-7xl mx-auto",
            ),
            class_name="relative bg-gradient-to-b from-gray-50/50 to-white overflow-hidden",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    stat_card(
                        "database",
                        MedicineState.medicines.length().to_string(),
                        "Medicines Indexed",
                        "-1",
                    ),
                    stat_card("trending-down", "90%", "Max Savings", "-2"),
                    stat_card("map-pin", "100+", "Verified Pharmacies", "-3"),
                    stat_card(
                        "message_circle_check", "Verified", "Jan Aushadhi Quality", "-4"
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 relative z-20",
                ),
                class_name="max-w-7xl mx-auto px-4 -mt-16",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "How MedSaver Works",
                            class_name="text-4xl font-black text-center text-gray-900 mb-4",
                        ),
                        rx.el.div(
                            class_name="h-1.5 w-24 bg-gradient-to-r from-teal-500 to-emerald-500 mx-auto rounded-full mb-16"
                        ),
                        class_name="text-center",
                    ),
                    rx.el.div(
                        rx.el.div(
                            class_name="hidden md:block absolute top-1/2 left-[10%] right-[10%] h-0.5 bg-gradient-to-r from-teal-200 via-emerald-200 to-cyan-200 -translate-y-1/2 z-0"
                        ),
                        step_card(
                            "search",
                            "Search Medicine",
                            "Enter your prescribed brand name to find its salt composition.",
                            "1",
                        ),
                        step_card(
                            "git-compare",
                            "Compare Options",
                            "View generic alternatives with significant price differences.",
                            "2",
                        ),
                        step_card(
                            "map-pin",
                            "Get at Pharmacy",
                            "Find nearby Jan Aushadhi or verified stores stocking the alternative.",
                            "3",
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-3 gap-12 relative",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "View Affordability Insights",
                            rx.icon(
                                "arrow-right",
                                class_name="h-5 w-5 ml-2 group-hover:translate-x-1 transition-transform",
                            ),
                            on_click=lambda: MedicineState.set_nav("/insights"),
                            class_name="mt-20 px-8 py-4 bg-gradient-to-r from-teal-500 to-emerald-500 text-white font-bold rounded-2xl hover:opacity-90 transition-all mx-auto flex items-center justify-center w-fit shadow-xl shadow-teal-500/20 group hover-lift",
                        ),
                        class_name="text-center",
                    ),
                    class_name="py-24",
                ),
                class_name="max-w-7xl mx-auto px-4",
            )
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "TRUSTED AND VERIFIED BY",
                        class_name="text-center text-gray-400 text-sm font-black tracking-[0.2em] mb-10",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "shield-check", class_name="h-6 w-6 text-teal-500 mr-2"
                            ),
                            "PMBJP Approved",
                            class_name="flex items-center text-gray-500 font-bold text-lg bg-white px-6 py-3 rounded-2xl shadow-sm border border-gray-100 animate-fade-in-up-1",
                        ),
                        rx.el.div(
                            rx.icon(
                                "message_circle_check",
                                class_name="h-6 w-6 text-emerald-500 mr-2",
                            ),
                            "WHO Standard",
                            class_name="flex items-center text-gray-500 font-bold text-lg bg-white px-6 py-3 rounded-2xl shadow-sm border border-gray-100 animate-fade-in-up-2",
                        ),
                        rx.el.div(
                            rx.icon(
                                "badge-check", class_name="h-6 w-6 text-cyan-500 mr-2"
                            ),
                            "Ministry of Health",
                            class_name="flex items-center text-gray-500 font-bold text-lg bg-white px-6 py-3 rounded-2xl shadow-sm border border-gray-100 animate-fade-in-up-3",
                        ),
                        rx.el.div(
                            rx.icon("award", class_name="h-6 w-6 text-blue-500 mr-2"),
                            "DCGI Certified",
                            class_name="flex items-center text-gray-500 font-bold text-lg bg-white px-6 py-3 rounded-2xl shadow-sm border border-gray-100 animate-fade-in-up-4",
                        ),
                        class_name="flex flex-wrap justify-center items-center gap-6",
                    ),
                    class_name="py-16 border-t border-gray-100",
                ),
                class_name="max-w-7xl mx-auto px-4",
            )
        ),
        footer(),
        chat_widget(),
        on_mount=PharmacyState.request_geolocation,
        class_name="min-h-screen bg-white font-['Inter']",
    )


def results_page() -> rx.Component:
    TOOLTIP_PROPS = {
        "content_style": {
            "background": "white",
            "borderColor": "#F3F4F6",
            "borderRadius": "1rem",
            "boxShadow": "0 20px 25px -5px rgba(0, 0, 0, 0.1)",
            "fontFamily": "Inter",
            "fontSize": "0.75rem",
            "padding": "12px",
            "border": "none",
        },
        "cursor": {"fill": "transparent"},
        "separator": "",
    }
    return rx.el.main(
        navbar(),
        rx.el.div(
            rx.cond(
                SmartFeaturesState.overpay_data["show_alert"].to(bool),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "triangle_alert",
                                class_name="h-12 w-12 text-red-600 mr-4 animate-bounce",
                            ),
                            rx.el.div(
                                rx.el.h3(
                                    "🚨 OVERPAY ALERT",
                                    class_name="text-2xl font-black text-red-900 mb-1",
                                ),
                                rx.el.p(
                                    "You are currently overpaying by ₹",
                                    SmartFeaturesState.overpay_data[
                                        "per_strip"
                                    ].to_string(),
                                    " per strip for ",
                                    MedicineState.selected_medicine["brand_name"],
                                    class_name="text-red-800 font-bold",
                                ),
                                rx.cond(
                                    SmartFeaturesState.overpay_data["severity"]
                                    == "critical",
                                    rx.el.p(
                                        "📅 You could save ₹",
                                        SmartFeaturesState.overpay_data[
                                            "per_year"
                                        ].to_string(),
                                        "/year — equivalent to ",
                                        SmartFeaturesState.overpay_data[
                                            "grocery_days"
                                        ].to_string(),
                                        " days of groceries",
                                        class_name="text-amber-800 font-black mt-2",
                                    ),
                                ),
                                rx.cond(
                                    SmartFeaturesState.overpay_data["severity"]
                                    == "significant",
                                    rx.el.p(
                                        "💸 Significant monthly overpayment of ₹",
                                        SmartFeaturesState.overpay_data[
                                            "per_month"
                                        ].to_string(),
                                        " detected",
                                        class_name="text-amber-700 font-bold mt-1",
                                    ),
                                ),
                                rx.el.p(
                                    "See verified alternatives below ↓",
                                    class_name="text-red-600 text-xs font-black uppercase mt-4 tracking-widest",
                                ),
                            ),
                            class_name="flex items-start",
                        ),
                        class_name="max-w-7xl mx-auto px-4",
                    ),
                    class_name="bg-gradient-to-r from-red-50 to-amber-50 border-l-8 border-red-500 p-8 rounded-2xl mb-8 shadow-2xl animate-fade-in-up",
                ),
            ),
            rx.cond(
                SmartFeaturesState.is_nti_drug,
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "triangle-alert", class_name="h-6 w-6 text-red-700 mr-3"
                        ),
                        rx.el.p(
                            "⚠️ NTI Drug — This medicine has a Narrow Therapeutic Index. Doctor approval required before switching to any alternative.",
                            class_name="text-red-900 font-black",
                        ),
                        class_name="flex items-center justify-center bg-red-100 border-2 border-red-200 p-4 rounded-2xl mb-8",
                    ),
                    class_name="max-w-7xl mx-auto px-4",
                ),
            ),
            rx.cond(
                MedicineState.price_alert_active,
                rx.el.div(
                    rx.icon(
                        "zap", class_name="h-6 w-6 text-amber-600 mr-3 animate-pulse"
                    ),
                    rx.el.p(
                        "⚡ High Savings Opportunity: Save ",
                        MedicineState.savings_percentage.to_string(),
                        "% by switching to the generic equivalent!",
                        class_name="text-amber-900 font-black",
                    ),
                    class_name="bg-amber-50 border-b border-amber-100 p-5 flex items-center justify-center mb-8 sticky top-16 z-30 backdrop-blur-md bg-amber-50/90",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("arrow-left", class_name="h-4 w-4 mr-2"),
                        "Back to Search",
                        on_click=lambda: MedicineState.set_nav("/search"),
                        class_name="text-gray-400 hover:text-teal-600 flex items-center mb-8 font-bold transition-colors",
                    ),
                    rx.el.h1(
                        "Alternatives for ",
                        rx.el.span(
                            MedicineState.selected_medicine["brand_name"],
                            class_name="gradient-text",
                        ),
                        class_name="text-4xl font-black text-gray-900 tracking-tight",
                    ),
                    class_name="mb-12",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Prescribed Brand",
                                                class_name="text-[10px] font-black text-gray-400 uppercase tracking-[0.2em] mb-1",
                                            ),
                                            rx.el.h2(
                                                MedicineState.selected_medicine[
                                                    "brand_name"
                                                ],
                                                class_name="text-3xl font-black text-gray-900 mb-1",
                                            ),
                                            rx.el.p(
                                                "By "
                                                + MedicineState.selected_medicine[
                                                    "manufacturer"
                                                ],
                                                class_name="text-sm text-gray-500 font-medium",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.icon(
                                                rx.match(
                                                    MedicineState.selected_medicine[
                                                        "dosage_form"
                                                    ],
                                                    ("Tablet", "pill"),
                                                    ("Capsule", "pill"),
                                                    ("Syrup", "droplet"),
                                                    ("Injection", "syringe"),
                                                    "pill",
                                                ),
                                                class_name="h-4 w-4 mr-2 text-gray-600",
                                            ),
                                            rx.el.span(
                                                MedicineState.selected_medicine[
                                                    "dosage_form"
                                                ],
                                                " - ",
                                                MedicineState.selected_medicine[
                                                    "dosage_strength"
                                                ],
                                            ),
                                            class_name="flex items-center px-4 py-2 bg-gray-100 text-gray-700 text-xs font-black rounded-full",
                                        ),
                                        class_name="flex justify-between items-start mb-8",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Therapeutic Category",
                                                class_name="text-xs font-black text-gray-400 uppercase mb-2",
                                            ),
                                            rx.el.p(
                                                MedicineState.selected_medicine[
                                                    "therapeutic_category"
                                                ],
                                                class_name="text-sm font-bold text-gray-700 bg-gray-50 px-3 py-2 rounded-xl",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "Salt Composition",
                                                class_name="text-xs font-black text-teal-600 uppercase mb-2 mt-6",
                                            ),
                                            rx.el.p(
                                                MedicineState.selected_medicine[
                                                    "salt_composition"
                                                ],
                                                class_name="text-sm font-bold text-teal-900 bg-teal-50 px-4 py-3 rounded-xl border border-teal-100",
                                            ),
                                        ),
                                        class_name="mb-10",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Regulatory & Safety",
                                            class_name="text-xs font-black text-gray-400 uppercase mb-4",
                                        ),
                                        rx.el.div(
                                            rx.el.div(
                                                rx.icon(
                                                    "shield-check",
                                                    class_name="h-5 w-5 text-blue-600 mr-2",
                                                ),
                                                rx.el.span(
                                                    MedicineState.selected_medicine[
                                                        "regulatory_status"
                                                    ],
                                                    class_name="text-xs font-black text-blue-900",
                                                ),
                                                class_name="flex items-center p-3 bg-blue-50/50 rounded-xl flex-1",
                                            ),
                                            rx.cond(
                                                MedicineState.selected_medicine[
                                                    "bioequivalence_verified"
                                                ],
                                                rx.el.div(
                                                    rx.icon(
                                                        "circle-check-big",
                                                        class_name="h-5 w-5 text-emerald-600 mr-2",
                                                    ),
                                                    rx.el.span(
                                                        "Verified Bio",
                                                        class_name="text-xs font-black text-emerald-900",
                                                    ),
                                                    class_name="flex items-center p-3 bg-emerald-50/50 rounded-xl flex-1",
                                                ),
                                            ),
                                            rx.el.div(
                                                rx.icon(
                                                    "badge-check",
                                                    class_name="h-5 w-5 text-teal-600 mr-2",
                                                ),
                                                rx.el.span(
                                                    "Safe Sub",
                                                    class_name="text-xs font-black text-teal-900",
                                                ),
                                                class_name="flex items-center p-3 bg-teal-50/50 rounded-xl flex-1",
                                            ),
                                            class_name="flex gap-3 flex-wrap",
                                        ),
                                    ),
                                    class_name="p-8 bg-white border border-gray-100 rounded-3xl shadow-sm",
                                ),
                                rx.el.div(
                                    rx.el.h3(
                                        "Price Comparison (₹)",
                                        class_name="text-lg font-black text-gray-900 mb-6 mt-10",
                                    ),
                                    rx.el.div(
                                        rx.recharts.bar_chart(
                                            rx.recharts.cartesian_grid(
                                                horizontal=True,
                                                vertical=False,
                                                stroke_dasharray="3 3",
                                                stroke="#f3f4f6",
                                            ),
                                            rx.recharts.graphing_tooltip(
                                                **TOOLTIP_PROPS
                                            ),
                                            rx.recharts.bar(
                                                data_key="price",
                                                fill="#0d9488",
                                                radius=[6, 6, 0, 0],
                                            ),
                                            rx.recharts.x_axis(
                                                data_key="name",
                                                axis_line=False,
                                                tick_line=False,
                                                custom_attrs={
                                                    "fontSize": "9px",
                                                    "fontWeight": "600",
                                                },
                                            ),
                                            rx.recharts.y_axis(
                                                axis_line=False,
                                                tick_line=False,
                                                custom_attrs={"fontSize": "9px"},
                                            ),
                                            data=MedicineState.chart_data,
                                            width="100%",
                                            height=200,
                                            margin={
                                                "top": 10,
                                                "right": 10,
                                                "left": -20,
                                                "bottom": 0,
                                            },
                                        ),
                                        class_name="bg-white p-6 rounded-3xl border border-gray-100 shadow-sm",
                                    ),
                                ),
                            ),
                            class_name="col-span-1",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "GENERIC ALTERNATIVE FOUND",
                                                class_name="text-[10px] font-black text-teal-600 uppercase tracking-[0.2em] mb-1",
                                            ),
                                            rx.el.h2(
                                                MedicineState.selected_medicine[
                                                    "generic_name"
                                                ],
                                                class_name="text-3xl font-black text-gray-900 mb-6",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "YOU SAVE",
                                                class_name="text-[10px] text-green-700 font-black uppercase mb-1",
                                            ),
                                            rx.el.p(
                                                "₹"
                                                + MedicineState.savings_amount.to_string(),
                                                class_name="text-4xl font-black text-green-600",
                                            ),
                                            class_name="bg-green-50/50 px-6 py-4 rounded-2xl border border-green-100",
                                        ),
                                        class_name="flex justify-between items-center mb-10",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.icon(
                                                "message_circle_check",
                                                class_name="h-4 w-4 mr-2",
                                            ),
                                            "Same Form",
                                            class_name="flex items-center px-4 py-2 bg-emerald-50 text-emerald-700 text-xs font-black rounded-full shadow-sm border border-emerald-100",
                                        ),
                                        rx.el.div(
                                            rx.icon(
                                                "contact", class_name="h-4 w-4 mr-2"
                                            ),
                                            "Verified Generic",
                                            class_name="flex items-center px-4 py-2 bg-blue-50 text-blue-700 text-xs font-black rounded-full shadow-sm border border-blue-100",
                                        ),
                                        rx.cond(
                                            MedicineState.selected_medicine[
                                                "is_jan_aushadhi"
                                            ],
                                            rx.el.div(
                                                rx.el.div(
                                                    rx.icon(
                                                        "star",
                                                        class_name="h-4 w-4 mr-2 fill-purple-700",
                                                    ),
                                                    "Jan Aushadhi",
                                                    class_name="flex items-center px-4 py-2 bg-purple-50 text-purple-700 text-xs font-black rounded-full shadow-sm border border-purple-100",
                                                )
                                            ),
                                        ),
                                        class_name="flex flex-wrap gap-3 mb-12",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Brand Price",
                                                class_name="text-xs font-black text-gray-400",
                                            ),
                                            rx.el.p(
                                                "₹"
                                                + MedicineState.selected_medicine[
                                                    "brand_price"
                                                ].to_string(),
                                                class_name="text-xl text-gray-300 line-through font-bold",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "Generic Price",
                                                class_name="text-xs font-black text-teal-600",
                                            ),
                                            rx.el.p(
                                                "₹"
                                                + MedicineState.selected_medicine[
                                                    "generic_price"
                                                ].to_string(),
                                                class_name="text-5xl font-black text-teal-600 tracking-tighter",
                                            ),
                                        ),
                                        class_name="flex gap-12 items-end mb-10",
                                    ),
                                    rx.el.button(
                                        "Find at Nearby Pharmacy",
                                        rx.icon("map-pin", class_name="h-5 w-5 ml-2"),
                                        on_click=lambda: MedicineState.set_nav(
                                            "/pharmacies"
                                        ),
                                        class_name="w-full py-5 bg-gradient-to-r from-teal-600 to-emerald-500 text-white font-black text-lg rounded-2xl hover:opacity-90 transition-all shadow-xl shadow-teal-500/20 flex items-center justify-center",
                                    ),
                                ),
                                class_name="p-10 bg-white border-4 border-teal-500 rounded-[2.5rem] shadow-2xl shadow-teal-100 mb-10 animate-fade-in-up",
                            ),
                            rx.el.div(
                                rx.el.h3(
                                    "Affordability Insights",
                                    class_name="text-xl font-black text-gray-900 mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Annual Savings Potential",
                                                class_name="text-xs font-black text-teal-600 uppercase tracking-widest mb-1",
                                            ),
                                            rx.el.p(
                                                "₹"
                                                + MedicineState.annual_savings.to_string(),
                                                class_name="text-3xl font-black text-teal-700",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.el.span(
                                                MedicineState.savings_tier,
                                                class_name=rx.match(
                                                    MedicineState.savings_tier,
                                                    (
                                                        "Gold",
                                                        "bg-amber-100 text-amber-700",
                                                    ),
                                                    (
                                                        "Silver",
                                                        "bg-gray-100 text-gray-600",
                                                    ),
                                                    (
                                                        "Bronze",
                                                        "bg-orange-100 text-orange-700",
                                                    ),
                                                    "bg-teal-100 text-teal-700",
                                                ),
                                            ),
                                            class_name="px-4 py-2 rounded-xl text-sm font-black shadow-sm",
                                        ),
                                        class_name="flex justify-between items-center mb-8 p-6 bg-teal-50/50 rounded-3xl border border-teal-100",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Monthly Cost (Brand)",
                                                class_name="text-xs font-bold text-gray-400",
                                            ),
                                            rx.el.p(
                                                "₹"
                                                + MedicineState.monthly_brand_cost.to_string(),
                                                class_name="text-lg font-bold text-gray-500 line-through",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "Monthly Cost (Generic)",
                                                class_name="text-xs font-black text-teal-600",
                                            ),
                                            rx.el.p(
                                                "₹"
                                                + MedicineState.monthly_generic_cost.to_string(),
                                                class_name="text-lg font-black text-teal-600",
                                            ),
                                        ),
                                        class_name="flex justify-between items-center mb-6",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            class_name="bg-teal-500 h-2.5 rounded-full",
                                            style={
                                                "width": MedicineState.savings_percentage.to_string()
                                                + "%"
                                            },
                                        ),
                                        class_name="w-full bg-gray-100 rounded-full h-2.5 mb-2",
                                    ),
                                    rx.el.p(
                                        MedicineState.savings_percentage.to_string()
                                        + "% more affordable",
                                        class_name="text-xs text-right font-black text-teal-600",
                                    ),
                                    class_name="p-8 bg-white border border-gray-100 rounded-3xl shadow-sm",
                                ),
                            ),
                            class_name="col-span-1",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-10",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Multi-Brand Comparison & Safety Score",
                            class_name="text-2xl font-black text-gray-900 mb-8 mt-16 text-center",
                        ),
                        rx.el.div(
                            rx.el.table(
                                rx.el.thead(
                                    rx.el.tr(
                                        rx.el.th(
                                            "Brand / Product",
                                            class_name="text-left py-5 px-6 text-xs font-black text-gray-400 uppercase tracking-widest border-b border-gray-100",
                                        ),
                                        rx.el.th(
                                            "Manufacturer",
                                            class_name="text-left py-5 px-6 text-xs font-black text-gray-400 uppercase tracking-widest border-b border-gray-100",
                                        ),
                                        rx.el.th(
                                            "Price",
                                            class_name="text-right py-5 px-6 text-xs font-black text-gray-400 uppercase tracking-widest border-b border-gray-100",
                                        ),
                                        rx.el.th(
                                            "Confidence Score",
                                            class_name="text-center py-5 px-6 text-xs font-black text-gray-400 uppercase tracking-widest border-b border-gray-100",
                                        ),
                                    )
                                ),
                                rx.el.tbody(
                                    rx.foreach(
                                        SmartFeaturesState.alternatives_with_confidence,
                                        lambda alt: rx.el.tr(
                                            rx.el.td(
                                                rx.el.div(
                                                    rx.el.span(
                                                        alt["name"],
                                                        class_name="font-bold text-gray-900",
                                                    ),
                                                    rx.cond(
                                                        alt["is_generic"],
                                                        rx.el.span(
                                                            "GENERIC",
                                                            class_name="ml-3 px-2 py-0.5 bg-green-100 text-green-700 text-[9px] font-black rounded-full",
                                                        ),
                                                    ),
                                                    class_name="flex items-center",
                                                ),
                                                class_name="py-5 px-6 border-b border-gray-50",
                                            ),
                                            rx.el.td(
                                                alt["manufacturer"],
                                                class_name="py-5 px-6 text-sm font-medium text-gray-500 border-b border-gray-50",
                                            ),
                                            rx.el.td(
                                                "₹" + alt["price"].to_string(),
                                                class_name="py-5 px-6 text-right font-black text-teal-600 border-b border-gray-50",
                                            ),
                                            rx.el.td(
                                                rx.el.div(
                                                    rx.el.div(
                                                        rx.el.span(
                                                            alt[
                                                                "confidence_score"
                                                            ].to_string()
                                                            + "% "
                                                            + alt[
                                                                "confidence_emoji"
                                                            ].to_string()
                                                        ),
                                                        class_name=rx.match(
                                                            alt["confidence_color"],
                                                            (
                                                                "green",
                                                                "px-3 py-1 bg-green-100 text-green-700 border border-green-200 rounded-full text-[10px] font-black shadow-sm",
                                                            ),
                                                            (
                                                                "yellow",
                                                                "px-3 py-1 bg-yellow-100 text-yellow-700 border border-yellow-200 rounded-full text-[10px] font-black shadow-sm",
                                                            ),
                                                            (
                                                                "orange",
                                                                "px-3 py-1 bg-orange-100 text-orange-700 border border-orange-200 rounded-full text-[10px] font-black shadow-sm",
                                                            ),
                                                            (
                                                                "red",
                                                                "px-3 py-1 bg-red-100 text-red-700 border border-red-200 rounded-full text-[10px] font-black shadow-sm",
                                                            ),
                                                            "px-3 py-1 bg-gray-100 text-gray-700 border border-gray-200 rounded-full text-[10px] font-black shadow-sm",
                                                        ),
                                                    ),
                                                    rx.el.span(
                                                        alt["confidence_label"],
                                                        class_name="text-[9px] text-gray-400 font-bold mt-1 block",
                                                    ),
                                                    class_name="flex flex-col items-center",
                                                ),
                                                class_name="py-5 px-6 text-center border-b border-gray-50",
                                            ),
                                            class_name="hover:bg-teal-50/30 transition-colors",
                                        ),
                                    )
                                ),
                                class_name="min-w-full table-auto",
                            ),
                            class_name="bg-white rounded-[2rem] border border-gray-100 overflow-hidden shadow-sm overflow-x-auto",
                        ),
                        class_name="mb-16",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "shopping-cart",
                                    class_name="h-8 w-8 text-teal-600 p-2 bg-teal-50 rounded-xl",
                                ),
                                rx.el.div(
                                    rx.el.h3(
                                        "Online Store Price Comparison",
                                        class_name="text-2xl font-black text-gray-900",
                                    ),
                                    rx.el.p(
                                        "Real-time AI analysis of prices from 1mg, PharmEasy, Netmeds, Apollo, and more.",
                                        class_name="text-sm text-gray-500 font-medium",
                                    ),
                                ),
                                class_name="flex items-center gap-4 mb-8",
                            ),
                            rx.cond(
                                AICompareState.ai_loading,
                                rx.el.div(
                                    rx.spinner(
                                        size="3", class_name="text-teal-600 mb-6"
                                    ),
                                    rx.el.p(
                                        "Scanning online inventories...",
                                        class_name="text-teal-700 font-black animate-pulse",
                                    ),
                                    rx.el.div(
                                        rx.foreach(
                                            rx.Var.range(4),
                                            lambda i: rx.el.div(
                                                class_name="h-14 bg-gray-50 rounded-2xl mb-4 animate-pulse border border-gray-100"
                                            ),
                                        ),
                                        class_name="w-full mt-10 max-w-4xl mx-auto",
                                    ),
                                    class_name="flex flex-col items-center py-12",
                                ),
                                rx.cond(
                                    AICompareState.ai_error != "",
                                    rx.el.div(
                                        rx.el.div(
                                            rx.icon(
                                                "info",
                                                class_name="h-5 w-5 text-blue-600 mr-3 shrink-0",
                                            ),
                                            rx.el.p(
                                                "To unlock AI-powered price analysis, please configure your API key in Settings.",
                                                class_name="text-blue-900 text-sm font-bold",
                                            ),
                                            class_name="flex items-center justify-center bg-blue-50/80 p-5 rounded-2xl border border-blue-100 mb-8",
                                        ),
                                        rx.el.div(
                                            rx.el.a(
                                                "Check 1mg.com",
                                                href="https://www.1mg.com",
                                                target="_blank",
                                                class_name="px-6 py-3 bg-white border border-gray-200 text-gray-700 font-black rounded-2xl hover:bg-gray-50 transition-all text-center text-sm shadow-sm",
                                            ),
                                            rx.el.a(
                                                "Check PharmEasy",
                                                href="https://pharmeasy.in",
                                                target="_blank",
                                                class_name="px-6 py-3 bg-white border border-gray-200 text-gray-700 font-black rounded-2xl hover:bg-gray-50 transition-all text-center text-sm shadow-sm",
                                            ),
                                            rx.el.a(
                                                "Check Netmeds",
                                                href="https://www.netmeds.com",
                                                target="_blank",
                                                class_name="px-6 py-3 bg-white border border-gray-200 text-gray-700 font-black rounded-2xl hover:bg-gray-50 transition-all text-center text-sm shadow-sm",
                                            ),
                                            rx.el.a(
                                                "Check Apollo",
                                                href="https://www.apollopharmacy.in",
                                                target="_blank",
                                                class_name="px-6 py-3 bg-white border border-gray-200 text-gray-700 font-black rounded-2xl hover:bg-gray-50 transition-all text-center text-sm shadow-sm",
                                            ),
                                            class_name="grid grid-cols-2 lg:grid-cols-4 gap-4",
                                        ),
                                    ),
                                    rx.cond(
                                        AICompareState.ai_comparison_result != "",
                                        rx.el.div(
                                            rx.el.div(
                                                rx.markdown(
                                                    AICompareState.ai_comparison_result,
                                                    class_name="prose prose-teal max-w-none text-sm font-medium",
                                                ),
                                                class_name="p-8 bg-gray-50/30 rounded-3xl border border-gray-100",
                                            ),
                                            rx.el.div(
                                                rx.el.div(
                                                    rx.icon(
                                                        "sparkles",
                                                        class_name="h-4 w-4 mr-2 text-teal-500 animate-shimmer",
                                                    ),
                                                    "Live Insights by Gemini Flash AI",
                                                    class_name="flex items-center text-xs text-gray-400 font-black uppercase tracking-widest",
                                                ),
                                                rx.el.button(
                                                    rx.icon(
                                                        "refresh-cw",
                                                        class_name="h-4 w-4 mr-2",
                                                    ),
                                                    "Update Prices",
                                                    on_click=[
                                                        AICompareState.check_api_key,
                                                        AICompareState.fetch_online_prices,
                                                    ],
                                                    class_name="flex items-center text-xs text-teal-600 font-black hover:text-teal-800 transition-colors",
                                                ),
                                                class_name="flex justify-between items-center mt-8 pt-6 border-t border-gray-100",
                                            ),
                                        ),
                                        rx.cond(
                                            ~AICompareState.has_fetched,
                                            rx.el.div(
                                                rx.el.button(
                                                    rx.icon(
                                                        "sparkles",
                                                        class_name="h-5 w-5 mr-3",
                                                    ),
                                                    "Fetch Real-time Prices",
                                                    on_click=[
                                                        AICompareState.check_api_key,
                                                        AICompareState.fetch_online_prices,
                                                    ],
                                                    class_name="flex items-center justify-center px-10 py-4 bg-teal-600 text-white font-black rounded-2xl hover:bg-teal-700 transition-all shadow-lg shadow-teal-500/20 mx-auto",
                                                ),
                                                class_name="py-12",
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                        class_name="w-full bg-white border border-teal-100 rounded-[2.5rem] shadow-sm p-10 mt-16 border-t-8 border-t-teal-500",
                    ),
                    rx.cond(
                        SmartFeaturesState.doctor_explanation["has_data"].to(bool),
                        rx.el.div(
                            rx.el.h3(
                                "🩺 Explain Like a Doctor",
                                class_name="text-2xl font-black text-gray-900 mb-6",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "activity",
                                            class_name="h-6 w-6 text-teal-600 mr-3",
                                        ),
                                        rx.el.h4(
                                            "What it does",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                        class_name="flex items-center mb-2",
                                    ),
                                    rx.el.p(
                                        SmartFeaturesState.doctor_explanation[
                                            "what_it_does"
                                        ].to(str),
                                        class_name="text-gray-600 pl-9",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "file-text",
                                            class_name="h-6 w-6 text-teal-600 mr-3",
                                        ),
                                        rx.el.h4(
                                            "Why it's prescribed",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                        class_name="flex items-center mb-2",
                                    ),
                                    rx.el.p(
                                        SmartFeaturesState.doctor_explanation[
                                            "why_prescribed"
                                        ].to(str),
                                        class_name="text-gray-600 pl-9",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "microscope",
                                            class_name="h-6 w-6 text-teal-600 mr-3",
                                        ),
                                        rx.el.h4(
                                            "How it works",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                        class_name="flex items-center mb-2",
                                    ),
                                    rx.el.p(
                                        SmartFeaturesState.doctor_explanation[
                                            "how_it_works"
                                        ].to(str),
                                        class_name="text-gray-600 pl-9",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "shield-check",
                                            class_name="h-6 w-6 text-emerald-600 mr-3",
                                        ),
                                        rx.el.h4(
                                            "Is the generic safe?",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                        class_name="flex items-center mb-2",
                                    ),
                                    rx.el.p(
                                        SmartFeaturesState.doctor_explanation[
                                            "generic_safe"
                                        ].to(str),
                                        class_name="text-emerald-700 font-medium pl-9",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.icon(
                                            "triangle-alert",
                                            class_name="h-6 w-6 text-amber-600 mr-3",
                                        ),
                                        rx.el.h4(
                                            "Watch out for",
                                            class_name="text-lg font-bold text-gray-900",
                                        ),
                                        class_name="flex items-center mb-2",
                                    ),
                                    rx.el.p(
                                        SmartFeaturesState.doctor_explanation[
                                            "watch_out"
                                        ].to(str),
                                        class_name="text-amber-700 pl-9",
                                    ),
                                    class_name="mb-6",
                                ),
                                class_name="grid grid-cols-1 md:grid-cols-2 gap-x-8 gap-y-2",
                            ),
                            rx.el.p(
                                "This is general information. Always follow your doctor's prescription.",
                                class_name="text-xs text-gray-400 text-center mt-6 pt-4 border-t border-gray-100",
                            ),
                            class_name="bg-white p-8 rounded-[2.5rem] border border-gray-100 shadow-sm mt-12 mb-8",
                        ),
                    ),
                    rx.el.div(
                        rx.cond(
                            SmartFeaturesState.price_trend_data["has_data"].to(bool),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h3(
                                        "📊 Price Trend",
                                        class_name="text-2xl font-black text-gray-900",
                                    ),
                                    rx.el.div(
                                        SmartFeaturesState.price_trend_data[
                                            "trend_icon"
                                        ].to(str),
                                        " ",
                                        SmartFeaturesState.price_trend_data[
                                            "change_pct"
                                        ].to(str),
                                        "% ",
                                        SmartFeaturesState.price_trend_data["trend"].to(
                                            str
                                        ),
                                        class_name="px-3 py-1 rounded-full text-sm font-bold bg-gray-100 text-gray-700 flex items-center",
                                    ),
                                    class_name="flex justify-between items-center mb-6",
                                ),
                                rx.cond(
                                    SmartFeaturesState.price_trend_data["alert"].to(str)
                                    != "",
                                    rx.el.div(
                                        SmartFeaturesState.price_trend_data["alert"].to(
                                            str
                                        ),
                                        class_name="bg-red-50 text-red-700 p-3 rounded-xl text-sm font-bold mb-6",
                                    ),
                                ),
                                rx.recharts.line_chart(
                                    rx.recharts.cartesian_grid(
                                        stroke_dasharray="3 3",
                                        horizontal=True,
                                        vertical=False,
                                    ),
                                    rx.recharts.graphing_tooltip(separator=""),
                                    rx.recharts.line(
                                        data_key="brand",
                                        stroke="#ef4444",
                                        name="Brand Price",
                                        type_="monotone",
                                    ),
                                    rx.recharts.line(
                                        data_key="generic",
                                        stroke="#0d9488",
                                        name="Generic Price",
                                        type_="monotone",
                                    ),
                                    rx.recharts.x_axis(
                                        data_key="month",
                                        tick_line=False,
                                        axis_line=False,
                                        custom_attrs={"fontSize": "12px"},
                                    ),
                                    rx.recharts.y_axis(
                                        tick_line=False,
                                        axis_line=False,
                                        custom_attrs={"fontSize": "12px"},
                                    ),
                                    data=SmartFeaturesState.price_trend_data[
                                        "history"
                                    ].to(list),
                                    width="100%",
                                    height=250,
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.span(
                                            class_name="w-3 h-3 rounded-full bg-red-500 mr-2 inline-block"
                                        ),
                                        rx.el.span(
                                            "Brand Price",
                                            class_name="text-xs text-gray-600 font-bold",
                                        ),
                                        class_name="flex items-center",
                                    ),
                                    rx.el.div(
                                        rx.el.span(
                                            class_name="w-3 h-3 rounded-full bg-teal-600 mr-2 inline-block"
                                        ),
                                        rx.el.span(
                                            "Generic Price",
                                            class_name="text-xs text-gray-600 font-bold",
                                        ),
                                        class_name="flex items-center",
                                    ),
                                    class_name="flex justify-center gap-6 mt-4",
                                ),
                                class_name="bg-white p-8 rounded-[2.5rem] border border-gray-100 shadow-sm h-full",
                            ),
                        ),
                        rx.cond(
                            SmartFeaturesState.cost_optimizer_data["has_data"].to(bool),
                            rx.el.div(
                                rx.el.h3(
                                    "💰 Monthly Cost Optimizer",
                                    class_name="text-2xl font-black text-gray-900 mb-6",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "Dosage: ",
                                        SmartFeaturesState.cost_optimizer_data[
                                            "doses_per_day"
                                        ].to(str),
                                        " per day",
                                        class_name="text-sm text-gray-500 font-bold mb-4",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.p(
                                                "Current Brand",
                                                class_name="text-xs text-gray-400 font-bold uppercase",
                                            ),
                                            rx.el.p(
                                                "₹",
                                                SmartFeaturesState.cost_optimizer_data[
                                                    "brand_monthly"
                                                ].to(str),
                                                "/mo",
                                                class_name="text-xl font-bold text-gray-900 line-through",
                                            ),
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "Best Generic",
                                                class_name="text-xs text-teal-600 font-bold uppercase",
                                            ),
                                            rx.el.p(
                                                "₹",
                                                SmartFeaturesState.cost_optimizer_data[
                                                    "generic_monthly"
                                                ].to(str),
                                                "/mo",
                                                class_name="text-2xl font-black text-teal-600",
                                            ),
                                        ),
                                        class_name="flex justify-between items-center p-4 bg-gray-50 rounded-2xl mb-4",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "Monthly Savings",
                                            class_name="text-sm font-bold text-gray-700",
                                        ),
                                        rx.el.p(
                                            "₹",
                                            SmartFeaturesState.cost_optimizer_data[
                                                "monthly_savings"
                                            ].to(str),
                                            class_name="text-xl font-black text-green-600",
                                        ),
                                        class_name="flex justify-between items-center p-4 border border-gray-100 rounded-2xl mb-6",
                                    ),
                                    rx.cond(
                                        SmartFeaturesState.cost_optimizer_data[
                                            "is_chronic"
                                        ].to(bool),
                                        rx.el.div(
                                            rx.el.p(
                                                "Annual Projected Savings",
                                                class_name="text-sm font-bold text-green-800 mb-1",
                                            ),
                                            rx.el.p(
                                                "₹",
                                                SmartFeaturesState.cost_optimizer_data[
                                                    "annual_savings"
                                                ].to(str),
                                                class_name="text-4xl font-black text-green-600",
                                            ),
                                            class_name="bg-green-50 p-6 rounded-2xl border border-green-100 text-center",
                                        ),
                                        rx.el.div(
                                            rx.el.p(
                                                "Course Savings",
                                                class_name="text-sm font-bold text-green-800 mb-1",
                                            ),
                                            rx.el.p(
                                                "₹",
                                                SmartFeaturesState.cost_optimizer_data[
                                                    "monthly_savings"
                                                ].to(str),
                                                class_name="text-3xl font-black text-green-600",
                                            ),
                                            class_name="bg-green-50 p-6 rounded-2xl border border-green-100 text-center",
                                        ),
                                    ),
                                ),
                                class_name="bg-white p-8 rounded-[2.5rem] border border-gray-100 shadow-sm h-full",
                            ),
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-10 mt-8 mb-16",
                    ),
                    rx.cond(
                        SmartFeaturesState.drug_interactions.length() > 0,
                        rx.el.div(
                            rx.el.h3(
                                "⚠️ Drug Interaction Check",
                                class_name="text-2xl font-black text-gray-900 mb-6",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    SmartFeaturesState.drug_interactions,
                                    lambda interaction: rx.el.div(
                                        rx.el.div(
                                            rx.el.span(
                                                rx.match(
                                                    interaction["severity"],
                                                    ("severe", "🔴 Severe"),
                                                    ("moderate", "🟠 Moderate"),
                                                    "🟡 Mild",
                                                ),
                                                class_name="font-black mr-2",
                                            ),
                                            rx.el.span(
                                                interaction["drug_a"],
                                                " + ",
                                                interaction["drug_b"],
                                                class_name="font-bold",
                                            ),
                                            class_name="mb-2",
                                        ),
                                        rx.el.p(
                                            interaction["effect"],
                                            class_name="text-sm mb-1",
                                        ),
                                        rx.el.p(
                                            "Advice: ",
                                            interaction["advice"],
                                            class_name="text-sm font-medium",
                                        ),
                                        class_name=rx.match(
                                            interaction["severity"],
                                            (
                                                "severe",
                                                "bg-red-50 text-red-900 border-l-4 border-red-500 p-4 mb-4 rounded-r-xl",
                                            ),
                                            (
                                                "moderate",
                                                "bg-orange-50 text-orange-900 border-l-4 border-orange-500 p-4 mb-4 rounded-r-xl",
                                            ),
                                            "bg-yellow-50 text-yellow-900 border-l-4 border-yellow-500 p-4 mb-4 rounded-r-xl",
                                        ),
                                    ),
                                ),
                                rx.el.p(
                                    "This is an automated check — always consult your doctor or pharmacist.",
                                    class_name="text-xs text-gray-500 mt-4",
                                ),
                                class_name="bg-white p-8 rounded-[2.5rem] border border-gray-100 shadow-sm mb-16",
                            ),
                        ),
                    ),
                    rx.cond(
                        SmartFeaturesState.community_trust["has_data"].to(bool),
                        rx.el.div(
                            rx.el.h3(
                                "🤝 Community Trust Signals",
                                class_name="text-2xl font-black text-gray-900 mb-6",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.icon(
                                        "message_circle_check",
                                        class_name="h-5 w-5 text-green-500 mr-2",
                                    ),
                                    rx.el.span(
                                        SmartFeaturesState.community_trust[
                                            "confirmed_works"
                                        ].to(str),
                                        " users confirmed: 'Generic worked fine for me'",
                                        class_name="font-medium text-gray-700",
                                    ),
                                    class_name="flex items-center mb-4",
                                ),
                                rx.el.div(
                                    rx.icon(
                                        "map-pin",
                                        class_name="h-5 w-5 text-blue-500 mr-2",
                                    ),
                                    rx.el.span(
                                        SmartFeaturesState.community_trust[
                                            "confirmed_available"
                                        ].to(str),
                                        " users confirmed: 'Available nearby'",
                                        class_name="font-medium text-gray-700",
                                    ),
                                    class_name="flex items-center mb-4",
                                ),
                                rx.el.div(
                                    rx.icon(
                                        "star",
                                        class_name="h-5 w-5 text-yellow-400 fill-yellow-400 mr-2",
                                    ),
                                    rx.el.span(
                                        "Community rating: ",
                                        SmartFeaturesState.community_trust["rating"].to(
                                            str
                                        ),
                                        "/5 based on ",
                                        SmartFeaturesState.community_trust[
                                            "total_reports"
                                        ].to(str),
                                        " reports",
                                        class_name="font-medium text-gray-700",
                                    ),
                                    class_name="flex items-center mb-4",
                                ),
                                rx.cond(
                                    SmartFeaturesState.community_trust[
                                        "issues_count"
                                    ].to(int)
                                    > 0,
                                    rx.el.div(
                                        rx.icon(
                                            "flag",
                                            class_name="h-5 w-5 text-red-500 mr-2",
                                        ),
                                        rx.el.span(
                                            SmartFeaturesState.community_trust[
                                                "issue_text"
                                            ].to(str),
                                            class_name="font-medium text-red-700",
                                        ),
                                        class_name="flex items-center mb-4 bg-red-50 p-2 rounded-xl",
                                    ),
                                ),
                                rx.el.p(
                                    "Community reports are user experiences, not medical endorsements.",
                                    class_name="text-xs text-gray-500 mt-4",
                                ),
                                class_name="bg-white p-8 rounded-[2.5rem] border border-gray-100 shadow-sm",
                            ),
                            class_name="mb-16",
                        ),
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 py-16",
            ),
        ),
        footer(),
        chat_widget(),
        on_mount=[
            MedicineState.on_load_results,
            AICompareState.check_api_key,
            AICompareState.clear_comparison,
        ],
        class_name="min-h-screen bg-gray-50 font-['Inter']",
    )


def pharmacies_page() -> rx.Component:
    return rx.el.main(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Find Nearby Pharmacies",
                    class_name="text-3xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Locate generic medical stores and Jan Aushadhi Kendras near you.",
                    class_name="text-gray-500",
                ),
                class_name="mb-8 text-center",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "map-pin",
                            class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 h-5 w-5",
                        ),
                        rx.el.input(
                            placeholder="Search by city or area (e.g., Mumbai, Bangalore...)",
                            on_change=PharmacyState.update_city_search.debounce(300),
                            class_name="w-full pl-12 pr-4 py-4 rounded-2xl border-2 border-gray-100 focus:border-teal-500 focus:ring-4 focus:ring-teal-100 outline-none text-lg transition-all shadow-sm",
                            default_value=PharmacyState.city_search,
                        ),
                        class_name="relative flex-1",
                    ),
                    rx.el.button(
                        rx.cond(
                            PharmacyState.location_status == "allowed",
                            rx.el.span(
                                rx.icon("map-pin", class_name="h-5 w-5 mr-2"),
                                "Your Location",
                                class_name="flex items-center",
                            ),
                            rx.cond(
                                PharmacyState.location_status == "denied",
                                rx.el.span(
                                    rx.icon("crosshair", class_name="h-5 w-5 mr-2"),
                                    "Location Denied - Enable in Browser Settings",
                                    class_name="flex items-center",
                                ),
                                rx.el.span(
                                    rx.icon("crosshair", class_name="h-5 w-5 mr-2"),
                                    "Use My Location",
                                    class_name="flex items-center",
                                ),
                            ),
                        ),
                        on_click=PharmacyState.request_geolocation,
                        class_name=rx.cond(
                            PharmacyState.location_status == "allowed",
                            "px-6 py-4 bg-teal-100 text-teal-800 font-bold rounded-2xl hover:bg-teal-200 transition-all flex items-center shrink-0 shadow-sm border border-teal-200",
                            rx.cond(
                                PharmacyState.location_status == "denied",
                                "px-6 py-4 bg-red-100 text-red-800 font-bold rounded-2xl hover:bg-red-200 transition-all flex items-center shrink-0 shadow-sm border border-red-200",
                                "px-6 py-4 bg-gradient-to-r from-teal-500 to-emerald-500 text-white font-bold rounded-2xl hover:opacity-90 transition-all flex items-center shrink-0 shadow-md",
                            ),
                        ),
                    ),
                    class_name="flex flex-col md:flex-row gap-4 w-full",
                ),
                rx.el.div(
                    rx.icon(
                        "pill",
                        class_name="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 h-5 w-5",
                    ),
                    rx.el.input(
                        placeholder="Search medicine to check availability...",
                        on_change=PharmacyState.update_medicine_search.debounce(300),
                        class_name="w-full pl-12 pr-4 py-4 rounded-2xl border-2 border-gray-100 focus:border-teal-500 focus:ring-4 focus:ring-teal-100 outline-none text-lg transition-all shadow-sm",
                    ),
                    class_name="relative w-full mt-4",
                ),
                rx.cond(
                    PharmacyState.show_city_suggestions
                    & (PharmacyState.filtered_city_suggestions.length() > 0),
                    rx.el.div(
                        rx.foreach(
                            PharmacyState.filtered_city_suggestions,
                            lambda c: rx.el.div(
                                rx.el.span(
                                    c["name"], class_name="font-semibold text-gray-900"
                                ),
                                rx.el.span(
                                    "View pharmacies →",
                                    class_name="text-xs text-teal-600 font-bold",
                                ),
                                on_click=lambda: PharmacyState.select_city(c),
                                class_name="flex justify-between items-center p-4 hover:bg-teal-50 cursor-pointer border-b border-gray-50 last:border-0 transition-colors",
                            ),
                        ),
                        class_name="absolute top-full left-0 right-0 mt-2 bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden z-40",
                    ),
                ),
                class_name="relative w-full max-w-2xl mx-auto mb-12",
            ),
            rx.el.div(
                rx.cond(
                    PharmacyState.selected_city != "",
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "City: ", class_name="text-teal-700 font-medium"
                            ),
                            rx.el.span(
                                PharmacyState.selected_city,
                                class_name="font-bold text-teal-900",
                            ),
                            rx.el.button(
                                rx.icon("x", class_name="h-4 w-4"),
                                on_click=PharmacyState.clear_city_search,
                                class_name="ml-2 p-1 hover:bg-teal-200 rounded-full transition-colors text-teal-700",
                            ),
                            class_name="inline-flex items-center px-4 py-2 bg-teal-100 rounded-full text-sm mb-4 shadow-sm",
                        ),
                        rx.el.p(
                            "Showing ",
                            PharmacyState.nearby_pharmacy_count.to_string(),
                            " pharmacies in ",
                            PharmacyState.selected_city,
                            class_name="text-gray-500 font-medium ml-2",
                        ),
                        class_name="flex items-center gap-4",
                    ),
                    rx.el.p(
                        "Showing all ",
                        PharmacyState.nearby_pharmacy_count.to_string(),
                        " pharmacies across India",
                        class_name="text-gray-500 font-medium mb-4",
                    ),
                )
            ),
            rx.el.div(
                rx.el.input(
                    placeholder="Search pharmacies...",
                    on_change=PharmacyState.set_search_filter,
                    class_name="flex-1 px-4 py-2 border border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 outline-none",
                ),
                rx.el.div(
                    rx.icon(
                        "chevron-down",
                        class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                    ),
                    rx.el.select(
                        rx.el.option("All Types", value="All"),
                        rx.el.option(
                            "Jan Aushadhi Kendra", value="Jan Aushadhi Kendra"
                        ),
                        rx.el.option("Generic Store", value="Generic Store"),
                        rx.el.option("Medical Store", value="Medical Store"),
                        on_change=PharmacyState.set_type_filter,
                        class_name="w-full appearance-none bg-white px-4 py-2 pr-10 border border-gray-200 rounded-xl outline-none focus:ring-2 focus:ring-teal-500",
                    ),
                    class_name="relative",
                ),
                rx.el.div(
                    rx.icon(
                        "chevron-down",
                        class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                    ),
                    rx.el.select(
                        rx.el.option("Nearest First", value="distance"),
                        rx.el.option("Highest Rated", value="rating"),
                        on_change=PharmacyState.set_sort_by,
                        class_name="w-full appearance-none bg-white px-4 py-2 pr-10 border border-gray-200 rounded-xl outline-none focus:ring-2 focus:ring-teal-500",
                    ),
                    class_name="relative",
                ),
                rx.cond(
                    PharmacyState.location_status == "allowed",
                    rx.el.div(
                        rx.icon(
                            "chevron-down",
                            class_name="absolute right-3 top-1/2 -translate-y-1/2 h-4 w-4 text-gray-400 pointer-events-none",
                        ),
                        rx.el.select(
                            rx.el.option("Radius: All", value="All"),
                            rx.el.option("Within 5 km", value="5"),
                            rx.el.option("Within 10 km", value="10"),
                            rx.el.option("Within 25 km", value="25"),
                            on_change=PharmacyState.set_radius_filter,
                            class_name="w-full appearance-none bg-white px-4 py-2 pr-10 border border-gray-200 rounded-xl outline-none focus:ring-2 focus:ring-teal-500",
                        ),
                        class_name="relative",
                    ),
                ),
                class_name="flex flex-col md:flex-row gap-4 mb-8",
            ),
            rx.cond(
                PharmacyState.medicine_search.length() >= 2,
                rx.el.div(
                    rx.icon("info", class_name="h-5 w-5 mr-2"),
                    rx.el.span(
                        PharmacyState.filtered_pharmacies.length().to_string(),
                        " pharmacies stock ",
                        PharmacyState.medicine_search,
                        class_name="font-bold",
                    ),
                    class_name="flex items-center justify-center p-4 bg-teal-50 text-teal-800 rounded-2xl mb-6 border border-teal-100 shadow-sm",
                ),
            ),
            rx.match(
                PharmacyState.location_status,
                (
                    "detecting",
                    rx.el.div(
                        rx.spinner(size="2", class_name="mr-2"),
                        "Detecting your location...",
                        class_name="flex items-center justify-center p-4 bg-teal-50 text-teal-700 rounded-2xl mb-6 font-bold animate-pulse border border-teal-100 shadow-sm",
                    ),
                ),
                (
                    "allowed",
                    rx.el.div(
                        rx.icon("map-pin", class_name="h-5 w-5 mr-2"),
                        "Location detected — showing pharmacies near you",
                        class_name="flex items-center justify-center p-4 bg-green-50 text-green-700 rounded-2xl mb-6 font-bold border border-green-100 shadow-sm",
                    ),
                ),
                (
                    "denied",
                    rx.el.div(
                        rx.icon("circle_alert", class_name="h-5 w-5 mr-2"),
                        "Location access denied — using Delhi as fallback. Search for your city above.",
                        class_name="flex items-center justify-center p-4 bg-gray-50 text-gray-600 rounded-2xl mb-6 font-bold border border-gray-200",
                    ),
                ),
                (
                    "error",
                    rx.el.div(
                        rx.icon("triangle_alert", class_name="h-5 w-5 mr-2"),
                        "Error detecting location — showing all pharmacies",
                        class_name="flex items-center justify-center p-4 bg-red-50 text-red-600 rounded-2xl mb-6 font-bold border border-red-100",
                    ),
                ),
                rx.el.div(
                    rx.icon("info", class_name="h-5 w-5 mr-2"),
                    "Ready to find pharmacies. Click 'Use My Location' or search for a city.",
                    class_name="flex items-center justify-center p-4 bg-blue-50 text-blue-700 rounded-2xl mb-6 font-bold border border-blue-100 shadow-sm",
                ),
            ),
            rx.el.div(
                rxe.map(
                    rxe.map.tile_layer(
                        url="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}",
                        attribution='&copy; <a href="https://maps.google.com">Google Maps</a>',
                        max_zoom=20,
                    ),
                    rx.cond(
                        (PharmacyState.location_status == "allowed")
                        & (PharmacyState.user_lat != 0),
                        rxe.map.marker(
                            rxe.map.popup(
                                rx.el.div(
                                    "📍 You are here",
                                    class_name="font-bold text-blue-700 text-sm p-1",
                                )
                            ),
                            position=rxe.map.latlng(
                                lat=PharmacyState.user_lat, lng=PharmacyState.user_lng
                            ),
                        ),
                    ),
                    rx.foreach(
                        PharmacyState.pharmacies,
                        lambda p: rxe.map.marker(
                            rxe.map.popup(
                                rx.el.div(
                                    rx.el.p(
                                        p["name"], class_name="font-bold text-gray-900"
                                    ),
                                    rx.el.p(
                                        p["type"],
                                        class_name="text-sm text-teal-600 font-medium",
                                    ),
                                    rx.el.p(
                                        p["city"],
                                        class_name="text-xs text-gray-500 mb-2",
                                    ),
                                    rx.el.a(
                                        "Get Directions",
                                        href=f"https://www.google.com/maps/dir/?api=1&destination={p['lat'].to_string()},{p['lng'].to_string()}",
                                        target="_blank",
                                        class_name="block w-full text-center px-3 py-1.5 bg-teal-600 text-white text-[10px] font-bold rounded-lg hover:bg-teal-700 transition-colors shadow-sm",
                                    ),
                                    class_name="min-w-[150px] p-1",
                                )
                            ),
                            position=rxe.map.latlng(lat=p["lat"], lng=p["lng"]),
                        ),
                    ),
                    id="pharmacy-map",
                    center=PharmacyState.map_center,
                    zoom=5.0,
                    height="100%",
                    width="100%",
                ),
                class_name="w-full h-[400px] rounded-2xl border-2 border-gray-100 mb-12 relative overflow-hidden",
            ),
            rx.cond(
                PharmacyState.smart_ranked_pharmacies.length() > 0,
                rx.el.div(
                    rx.foreach(
                        PharmacyState.smart_ranked_pharmacies,
                        lambda p: rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    p["name"],
                                    class_name="text-xl font-bold text-gray-900",
                                ),
                                rx.el.span(
                                    p["type"],
                                    class_name=rx.match(
                                        p["type"],
                                        (
                                            "Jan Aushadhi Kendra",
                                            "px-2 py-1 bg-purple-100 text-purple-700 text-xs font-bold rounded-full",
                                        ),
                                        (
                                            "Generic Store",
                                            "px-2 py-1 bg-teal-100 text-teal-700 text-xs font-bold rounded-full",
                                        ),
                                        "px-2 py-1 bg-blue-100 text-blue-700 text-xs font-bold rounded-full",
                                    ),
                                ),
                                class_name="flex justify-between items-start mb-2",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    "Smart Score: ",
                                    p["smart_score"].to(str),
                                    class_name="text-xs font-black text-white bg-gradient-to-r from-teal-500 to-emerald-500 px-2 py-1 rounded-md",
                                ),
                                class_name="mb-2",
                            ),
                            rx.el.p(
                                p["address"],
                                ", ",
                                p["city"],
                                " • ",
                                p["distance_km"].to_string(),
                                " km away",
                                class_name="text-sm text-gray-500 mb-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.icon("phone", class_name="h-4 w-4 mr-2"),
                                    rx.el.span(
                                        p["phone"], class_name="text-sm font-medium"
                                    ),
                                    class_name="flex items-center text-gray-600",
                                ),
                                rx.el.div(
                                    rx.icon(
                                        "star",
                                        class_name="h-4 w-4 text-yellow-400 mr-1 fill-yellow-400",
                                    ),
                                    rx.el.span(
                                        p["rating"],
                                        class_name="text-sm font-bold text-gray-700",
                                    ),
                                    class_name="flex items-center",
                                ),
                                rx.cond(
                                    p["is_open"],
                                    rx.el.span(
                                        "Open",
                                        class_name="text-xs font-bold text-green-600 bg-green-50 px-2 py-1 rounded-md",
                                    ),
                                    rx.el.span(
                                        "Closed",
                                        class_name="text-xs font-bold text-red-600 bg-red-50 px-2 py-1 rounded-md",
                                    ),
                                ),
                                class_name="flex justify-between items-center mb-2",
                            ),
                            rx.cond(
                                (PharmacyState.medicine_search.length() >= 2)
                                & (PharmacyState.matched_medicine_ids.length() > 0),
                                rx.el.div(
                                    rx.icon("check", class_name="h-4 w-4 mr-1"),
                                    "Medicine Available",
                                    class_name="flex items-center text-xs font-bold text-green-700 bg-green-50 px-2 py-1 rounded-md mb-6 w-fit border border-green-200",
                                ),
                                rx.el.div(class_name="mb-6"),
                            ),
                            rx.el.div(
                                rx.el.button(
                                    "Report Availability",
                                    on_click=lambda: PharmacyState.open_report_modal(
                                        p["id"]
                                    ),
                                    class_name="flex-1 py-2 border border-teal-600 text-teal-600 font-bold rounded-xl hover:bg-teal-50 transition-colors",
                                ),
                                rx.el.a(
                                    "Get Directions",
                                    href=rx.cond(
                                        (PharmacyState.location_status == "allowed")
                                        & (PharmacyState.user_lat != 0),
                                        f"https://www.google.com/maps/dir/?api=1&origin={PharmacyState.user_lat.to_string()},{PharmacyState.user_lng.to_string()}&destination={p['lat'].to_string()},{p['lng'].to_string()}&travelmode=driving",
                                        f"https://www.google.com/maps/dir/?api=1&destination={p['lat'].to_string()},{p['lng'].to_string()}",
                                    ),
                                    target="_blank",
                                    class_name="flex-1 py-2 bg-teal-600 text-white font-bold rounded-xl text-center hover:bg-teal-700 transition-colors shadow-md",
                                ),
                                class_name="flex gap-4",
                            ),
                            on_click=lambda: PharmacyState.fly_to_pharmacy(
                                p["lat"], p["lng"]
                            ),
                            class_name="p-6 bg-white border border-gray-100 rounded-2xl shadow-sm hover:shadow-md transition-all cursor-pointer",
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                ),
                rx.el.div(
                    rx.el.p(
                        "No pharmacies match your filters.",
                        class_name="text-center text-gray-500 py-12",
                    )
                ),
            ),
            rx.cond(
                PharmacyState.reports.length() > 0,
                rx.el.div(
                    rx.el.h2(
                        "Recent Community Reports",
                        class_name="text-2xl font-bold text-gray-900 mt-16 mb-6",
                    ),
                    rx.el.div(
                        rx.foreach(
                            PharmacyState.reports,
                            lambda r: rx.el.div(
                                rx.el.p(
                                    r["medicine_name"],
                                    class_name="font-bold text-gray-900",
                                ),
                                rx.el.p(
                                    "at ",
                                    r["pharmacy_name"],
                                    class_name="text-sm text-gray-500",
                                ),
                                rx.el.span(
                                    r["status"],
                                    class_name=rx.match(
                                        r["status"],
                                        (
                                            "Available",
                                            "text-green-600 font-bold text-sm bg-green-50 px-2 py-1 rounded mt-2 inline-block",
                                        ),
                                        (
                                            "Unavailable",
                                            "text-red-600 font-bold text-sm bg-red-50 px-2 py-1 rounded mt-2 inline-block",
                                        ),
                                        "text-yellow-600 font-bold text-sm bg-yellow-50 px-2 py-1 rounded mt-2 inline-block",
                                    ),
                                ),
                                rx.el.p(
                                    r["timestamp"],
                                    class_name="text-xs text-gray-400 mt-2",
                                ),
                                class_name="p-4 border border-gray-100 rounded-xl bg-gray-50",
                            ),
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4",
                    ),
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 py-12",
        ),
        rx.cond(
            PharmacyState.show_report_modal,
            rx.el.div(
                rx.el.div(
                    class_name="fixed inset-0 bg-black/50 backdrop-blur-sm z-40",
                    on_click=PharmacyState.toggle_report_modal,
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Report Medicine Availability",
                            class_name="text-xl font-bold mb-4",
                        ),
                        rx.el.input(
                            placeholder="Medicine Name...",
                            on_change=PharmacyState.set_report_medicine_name,
                            class_name="w-full px-4 py-2 border rounded-xl mb-4 focus:ring-teal-500 outline-none",
                        ),
                        rx.el.select(
                            rx.el.option("Available", value="Available"),
                            rx.el.option("Limited Stock", value="Limited Stock"),
                            rx.el.option("Unavailable", value="Unavailable"),
                            on_change=PharmacyState.set_report_status,
                            class_name="w-full px-4 py-2 border rounded-xl mb-6 outline-none appearance-none",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                on_click=PharmacyState.toggle_report_modal,
                                class_name="px-4 py-2 text-gray-600 font-medium hover:bg-gray-100 rounded-xl transition-colors",
                            ),
                            rx.el.button(
                                "Submit Report",
                                on_click=PharmacyState.submit_report,
                                class_name="px-4 py-2 bg-teal-600 text-white font-bold rounded-xl shadow-md hover:bg-teal-700 transition-colors",
                            ),
                            class_name="flex justify-end gap-2",
                        ),
                        class_name="bg-white p-6 rounded-2xl shadow-2xl relative z-50 w-full max-w-md animate-in zoom-in-95 duration-200",
                    ),
                    class_name="fixed inset-0 z-50 flex items-center justify-center p-4",
                ),
            ),
        ),
        footer(),
        chat_widget(),
        on_mount=PharmacyState.request_geolocation,
        class_name="min-h-screen bg-white font-['Inter']",
    )


def search_page_view() -> rx.Component:
    return rx.el.main(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Advanced Medicine Search",
                    class_name="text-4xl font-black text-gray-900 text-center mb-8 animate-fade-in-up",
                ),
                rx.el.div(
                    rx.icon(
                        "search",
                        class_name="absolute left-6 top-1/2 -translate-y-1/2 text-teal-500 h-6 w-6 z-10",
                    ),
                    rx.el.input(
                        placeholder="Search by brand, generic name, or composition...",
                        on_change=SearchPageState.update_search_text.debounce(300),
                        class_name="w-full px-16 py-5 rounded-2xl border-2 border-gray-100 focus:border-teal-500 outline-none text-xl transition-all shadow-sm bg-white/80 backdrop-blur-xl",
                    ),
                    rx.el.div(
                        class_name="absolute inset-0 rounded-2xl border-4 border-teal-400/0 focus-within:border-teal-400/30 animate-pulse pointer-events-none"
                    ),
                    class_name="relative w-full max-w-3xl mx-auto group mb-12",
                ),
                rx.el.div(
                    rx.foreach(
                        SearchPageState.categories,
                        lambda cat: rx.el.button(
                            cat,
                            on_click=lambda: SearchPageState.set_category(cat),
                            class_name=rx.cond(
                                SearchPageState.category_filter == cat,
                                "px-6 py-2.5 bg-gradient-to-r from-teal-600 to-emerald-500 text-white font-bold rounded-full shadow-lg shadow-teal-500/20 transform scale-105 transition-all",
                                "px-6 py-2.5 bg-white text-gray-600 font-semibold rounded-full border border-gray-100 hover:bg-gray-50 hover:scale-105 transition-all shadow-sm",
                            ),
                        ),
                    ),
                    class_name="flex flex-wrap justify-center gap-3 mb-16 max-w-5xl mx-auto",
                ),
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        rx.el.span(
                            SearchPageState.search_results.length().to_string(),
                            class_name="text-teal-600 font-black",
                        ),
                        " medicines found matching your criteria",
                        class_name="text-gray-500 font-bold mb-8 text-lg",
                    ),
                    rx.cond(
                        SearchPageState.search_results.length() > 0,
                        rx.el.div(
                            rx.foreach(
                                SearchPageState.search_results,
                                lambda m: rx.el.div(
                                    rx.el.div(
                                        rx.el.div(
                                            rx.el.h3(
                                                m["brand_name"],
                                                class_name="text-xl font-black text-gray-900",
                                            ),
                                            rx.el.div(
                                                rx.icon(
                                                    rx.match(
                                                        m["dosage_form"],
                                                        ("Tablet", "pill"),
                                                        ("Capsule", "pill"),
                                                        ("Syrup", "droplet"),
                                                        ("Injection", "syringe"),
                                                        "pill",
                                                    ),
                                                    class_name="h-4 w-4 text-gray-400",
                                                ),
                                                class_name="p-1.5 bg-gray-50 rounded-lg",
                                            ),
                                            class_name="flex justify-between items-start mb-1",
                                        ),
                                        rx.el.div(
                                            rx.cond(
                                                (
                                                    m["brand_price"].to(float)
                                                    - m["generic_price"].to(float)
                                                )
                                                / m["brand_price"].to(float)
                                                * 100
                                                > 50,
                                                rx.el.span(
                                                    "Price Alert",
                                                    class_name="text-[9px] uppercase font-black bg-red-50 text-red-600 px-2 py-0.5 rounded-full mr-2",
                                                ),
                                            ),
                                            rx.cond(
                                                (
                                                    m["brand_price"].to(float)
                                                    - m["generic_price"].to(float)
                                                )
                                                / m["brand_price"].to(float)
                                                * 100
                                                > 80,
                                                rx.el.span(
                                                    "Best Value",
                                                    class_name="text-[9px] uppercase font-black bg-green-50 text-green-600 px-2 py-0.5 rounded-full mr-2",
                                                ),
                                            ),
                                            rx.cond(
                                                m["is_jan_aushadhi"],
                                                rx.el.span(
                                                    "Gov Approved",
                                                    class_name="text-[9px] uppercase font-black bg-blue-50 text-blue-600 px-2 py-0.5 rounded-full",
                                                ),
                                            ),
                                            class_name="flex gap-1 mb-4 flex-wrap",
                                        ),
                                        rx.el.p(
                                            m["generic_name"],
                                            class_name="text-sm font-bold text-teal-700 mb-1",
                                        ),
                                        rx.el.p(
                                            m["salt_composition"],
                                            class_name="text-xs text-gray-400 font-medium mb-6 line-clamp-1",
                                        ),
                                        rx.el.div(
                                            rx.el.div(
                                                rx.el.p(
                                                    "₹" + m["brand_price"].to_string(),
                                                    class_name="text-xs text-gray-400 line-through font-bold",
                                                ),
                                                rx.el.p(
                                                    "₹"
                                                    + m["generic_price"].to_string(),
                                                    class_name="text-2xl font-black text-teal-600",
                                                ),
                                                class_name="flex flex-col",
                                            ),
                                            rx.el.div(
                                                class_name=rx.match(
                                                    (
                                                        m["brand_price"].to(float)
                                                        - m["generic_price"].to(float)
                                                    )
                                                    / m["brand_price"].to(float)
                                                    * 100
                                                    > 80,
                                                    (
                                                        True,
                                                        "h-2.5 w-2.5 rounded-full bg-yellow-400 shadow-[0_0_8px_rgba(250,204,21,0.5)]",
                                                    ),
                                                    rx.match(
                                                        (
                                                            m["brand_price"].to(float)
                                                            - m["generic_price"].to(
                                                                float
                                                            )
                                                        )
                                                        / m["brand_price"].to(float)
                                                        * 100
                                                        > 60,
                                                        (
                                                            True,
                                                            "h-2.5 w-2.5 rounded-full bg-gray-300",
                                                        ),
                                                        rx.match(
                                                            (
                                                                m["brand_price"].to(
                                                                    float
                                                                )
                                                                - m["generic_price"].to(
                                                                    float
                                                                )
                                                            )
                                                            / m["brand_price"].to(float)
                                                            * 100
                                                            > 40,
                                                            (
                                                                True,
                                                                "h-2.5 w-2.5 rounded-full bg-orange-300",
                                                            ),
                                                            "h-2.5 w-2.5 rounded-full bg-teal-400",
                                                        ),
                                                    ),
                                                )
                                            ),
                                            class_name="flex justify-between items-end mb-6",
                                        ),
                                        rx.el.button(
                                            "Compare Online Prices ⚡",
                                            on_click=lambda: SearchPageState.select_search_result(
                                                m
                                            ),
                                            class_name="w-full py-2.5 bg-teal-50 text-teal-700 font-bold rounded-xl hover:bg-teal-100 transition-colors text-xs",
                                        ),
                                    ),
                                    on_click=lambda: SearchPageState.select_search_result(
                                        m
                                    ),
                                    class_name="group p-6 bg-white border border-gray-100 rounded-2xl shadow-sm hover:shadow-xl hover:border-teal-300 hover:-translate-y-1.5 transition-all duration-300 cursor-pointer animate-fade-in-up",
                                ),
                            ),
                            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    "search-x",
                                    class_name="h-20 w-20 text-gray-200 mx-auto mb-6",
                                ),
                                rx.el.h3(
                                    "No medicines found",
                                    class_name="text-2xl font-black text-gray-900 mb-2",
                                ),
                                rx.el.p(
                                    "We couldn't find anything matching your search. Try broadening your filters or checking for typos.",
                                    class_name="text-gray-500 max-w-sm mx-auto font-medium",
                                ),
                                class_name="text-center py-24 bg-gray-50/50 rounded-3xl border-2 border-dashed border-gray-100",
                            ),
                            class_name="w-full animate-fade-in-up",
                        ),
                    ),
                    class_name="max-w-7xl mx-auto",
                ),
                class_name="bg-white px-4 py-16",
            ),
        ),
        footer(),
        chat_widget(),
        class_name="min-h-screen bg-gray-50 font-['Inter']",
    )


def insight_stat_card(
    icon_name: str, value: str, label: str, bg_color: str, text_color: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon_name, class_name=f"h-6 w-6 {text_color}"),
            class_name=f"p-3 {bg_color} rounded-2xl mb-4 w-fit shadow-sm",
        ),
        rx.el.h3(value, class_name="text-4xl font-black text-gray-900 tracking-tight"),
        rx.el.p(
            label,
            class_name="text-sm text-gray-500 font-bold uppercase tracking-wider mt-1",
        ),
        class_name="p-6 bg-white rounded-2xl shadow-sm hover:shadow-lg border border-gray-100 flex-1 hover-lift transition-all animate-fade-in-up",
    )


def top_saving_card(medicine: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(medicine["brand_name"], class_name="font-bold text-gray-900"),
                rx.icon("arrow-right", class_name="h-4 w-4 text-gray-400 mx-2"),
                rx.el.p(medicine["generic_name"], class_name="font-bold text-teal-700"),
                class_name="flex items-center flex-wrap",
            ),
            rx.cond(
                medicine["savings_pct"].to(float) > 50,
                rx.el.span(
                    "Price Alert",
                    class_name="px-2 py-0.5 bg-red-100 text-red-700 text-[10px] font-bold rounded-full uppercase",
                ),
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "₹" + medicine["brand_price"].to_string(),
                    class_name="text-sm text-gray-400 line-through",
                ),
                rx.el.p(
                    "₹" + medicine["generic_price"].to_string(),
                    class_name="text-xl font-black text-teal-600",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "Save " + medicine["savings_pct"].to_string() + "%",
                    class_name="text-xs text-green-700 font-black uppercase tracking-wider",
                ),
                rx.el.p(
                    "₹" + medicine["savings_amount"].to_string(),
                    class_name="text-2xl font-black text-green-600",
                ),
                class_name="text-right bg-green-50 px-4 py-2 rounded-xl border border-green-100",
            ),
            class_name="flex justify-between items-end mb-4",
        ),
        rx.el.div(
            rx.el.span(
                medicine["category"],
                class_name="text-xs font-bold text-gray-600 bg-gray-100 px-3 py-1 rounded-full",
            ),
            rx.el.span(
                medicine["tier"],
                class_name=rx.match(
                    medicine["tier"],
                    (
                        "Gold",
                        "text-xs font-black text-yellow-700 bg-yellow-100 px-3 py-1 rounded-full ml-2",
                    ),
                    (
                        "Silver",
                        "text-xs font-black text-gray-700 bg-gray-200 px-3 py-1 rounded-full ml-2",
                    ),
                    (
                        "Bronze",
                        "text-xs font-black text-orange-700 bg-orange-100 px-3 py-1 rounded-full ml-2",
                    ),
                    "text-xs font-black text-teal-700 bg-teal-100 px-3 py-1 rounded-full ml-2",
                ),
            ),
            class_name="flex items-center mt-2",
        ),
        on_click=lambda: DashboardState.navigate_to_medicine(medicine["id"]),
        class_name="p-6 bg-white rounded-2xl border border-gray-100 shadow-sm hover:shadow-xl hover:border-teal-300 transition-all cursor-pointer hover-lift animate-fade-in-up",
    )


def insights_page() -> rx.Component:
    return rx.el.main(
        navbar(),
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Affordability Insights Dashboard",
                    class_name="text-3xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Analytics and potential savings based on our medicine database.",
                    class_name="text-gray-500",
                ),
                class_name="mb-10",
            ),
            rx.el.div(
                insight_stat_card(
                    "database",
                    DashboardState.all_medicines.length().to_string(),
                    "Total Medicines Indexed",
                    "bg-teal-50",
                    "text-teal-600",
                ),
                insight_stat_card(
                    "trending-down",
                    DashboardState.avg_savings_percentage.to_string() + "%",
                    "Average Savings",
                    "bg-green-50",
                    "text-green-600",
                ),
                insight_stat_card(
                    "shield-check",
                    DashboardState.jan_aushadhi_count.to_string(),
                    "Jan Aushadhi Approved",
                    "bg-purple-50",
                    "text-purple-600",
                ),
                insight_stat_card(
                    "zap",
                    DashboardState.high_alert_count.to_string(),
                    "Price Alerts Active (>50% save)",
                    "bg-yellow-50",
                    "text-yellow-600",
                ),
                class_name="flex flex-col md:flex-row gap-6 mb-12",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Top Savings Opportunities",
                        class_name="text-xl font-bold text-gray-900 mb-1",
                    ),
                    rx.el.p(
                        "Medicines where you can save the most by switching to generics",
                        class_name="text-sm text-gray-500 mb-6",
                    ),
                    rx.el.div(
                        rx.foreach(
                            DashboardState.top_savings_medicines, top_saving_card
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-4",
                    ),
                    class_name="col-span-1 lg:col-span-2",
                ),
                rx.el.div(
                    rx.el.h2(
                        "Average Savings by Category",
                        class_name="text-xl font-bold text-gray-900 mb-6",
                    ),
                    rx.el.div(
                        rx.recharts.bar_chart(
                            rx.recharts.cartesian_grid(
                                horizontal=False, vertical=True, class_name="opacity-25"
                            ),
                            rx.recharts.graphing_tooltip(
                                content_style={"borderRadius": "0.5rem"}
                            ),
                            rx.recharts.bar(
                                data_key="avg_savings",
                                fill="#0d9488",
                                radius=[0, 4, 4, 0],
                            ),
                            rx.recharts.x_axis(
                                type_="number", axis_line=False, tick_line=False
                            ),
                            rx.recharts.y_axis(
                                data_key="category",
                                type_="category",
                                width=100,
                                axis_line=False,
                                tick_line=False,
                                custom_attrs={"fontSize": "12px"},
                            ),
                            data=DashboardState.category_savings,
                            layout="vertical",
                            width="100%",
                            height=350,
                            margin={"top": 10, "right": 30, "left": 20, "bottom": 5},
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm mb-8",
                    ),
                    rx.el.h2(
                        "Generic Price Distribution",
                        class_name="text-xl font-bold text-gray-900 mb-6",
                    ),
                    rx.el.div(
                        rx.recharts.bar_chart(
                            rx.recharts.cartesian_grid(
                                horizontal=True, vertical=False, class_name="opacity-25"
                            ),
                            rx.recharts.graphing_tooltip(
                                content_style={"borderRadius": "0.5rem"}
                            ),
                            rx.recharts.bar(
                                data_key="count", fill="#14b8a6", radius=[4, 4, 0, 0]
                            ),
                            rx.recharts.x_axis(
                                data_key="range",
                                axis_line=False,
                                tick_line=False,
                                custom_attrs={"fontSize": "12px"},
                            ),
                            rx.recharts.y_axis(axis_line=False, tick_line=False),
                            data=DashboardState.price_distribution,
                            width="100%",
                            height=250,
                            margin={"top": 10, "right": 10, "left": -20, "bottom": 0},
                        ),
                        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm",
                    ),
                    class_name="col-span-1",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12",
            ),
            rx.el.div(
                rx.el.h2(
                    "Compare Medicines Side-by-Side",
                    class_name="text-2xl font-bold text-gray-900 mb-2",
                ),
                rx.el.p(
                    "Select up to 3 medicines to compare all attributes",
                    class_name="text-gray-500 mb-6",
                ),
                rx.el.div(
                    rx.foreach(
                        DashboardState.all_medicines,
                        lambda m: rx.el.button(
                            m["brand_name"],
                            on_click=lambda: DashboardState.toggle_compare(m["id"]),
                            class_name=rx.cond(
                                DashboardState.compare_ids.contains(m["id"]),
                                "px-4 py-2 bg-teal-600 text-white font-bold rounded-full shadow-sm border-2 border-teal-600",
                                "px-4 py-2 bg-white text-gray-600 font-medium rounded-full border-2 border-gray-200 hover:border-teal-300 transition-colors",
                            ),
                        ),
                    ),
                    class_name="flex flex-wrap gap-3 mb-6",
                ),
                rx.el.div(
                    rx.el.p(
                        DashboardState.compare_ids.length().to_string() + "/3 selected",
                        class_name="text-sm font-medium text-gray-500",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Clear",
                            on_click=DashboardState.clear_compare,
                            class_name="px-4 py-2 text-gray-500 hover:text-gray-700 font-medium",
                        ),
                        rx.el.button(
                            "Compare Now",
                            on_click=DashboardState.toggle_compare_modal,
                            disabled=DashboardState.compare_ids.length() == 0,
                            class_name="px-6 py-2 bg-teal-600 text-white font-bold rounded-xl disabled:opacity-50 disabled:cursor-not-allowed hover:bg-teal-700 transition-colors",
                        ),
                        class_name="flex gap-2",
                    ),
                    class_name="flex justify-between items-center p-4 bg-gray-50 rounded-xl",
                ),
                class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm mb-12",
            ),
            rx.cond(
                DashboardState.show_compare_modal
                & (DashboardState.compare_medicines.length() > 0),
                rx.el.div(
                    rx.el.h3(
                        "Comparison View",
                        class_name="text-xl font-bold text-gray-900 mb-6",
                    ),
                    rx.el.div(
                        rx.foreach(
                            DashboardState.compare_medicines,
                            lambda m: rx.el.div(
                                rx.el.div(
                                    rx.el.h4(
                                        m["brand_name"],
                                        class_name="text-lg font-bold text-gray-900",
                                    ),
                                    rx.el.p(
                                        m["generic_name"],
                                        class_name="text-sm text-teal-600 font-bold",
                                    ),
                                    class_name="mb-4 pb-4 border-b border-gray-100",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "Composition",
                                        class_name="text-xs text-gray-400 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        m["salt_composition"],
                                        class_name="text-sm font-medium mb-4",
                                    ),
                                    rx.el.p(
                                        "Dosage",
                                        class_name="text-xs text-gray-400 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        f"{m['dosage_form'].to(str)} - {m['dosage_strength'].to(str)}",
                                        class_name="text-sm font-medium mb-4",
                                    ),
                                    rx.el.p(
                                        "Category",
                                        class_name="text-xs text-gray-400 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        m["category"],
                                        class_name="text-sm font-medium mb-4",
                                    ),
                                    rx.el.p(
                                        "Brand Price",
                                        class_name="text-xs text-gray-400 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        "₹" + m["brand_price"].to_string(),
                                        class_name="text-sm font-medium text-gray-500 line-through mb-4",
                                    ),
                                    rx.el.p(
                                        "Generic Price",
                                        class_name="text-xs text-teal-600 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        "₹" + m["generic_price"].to_string(),
                                        class_name="text-xl font-black text-teal-600 mb-4",
                                    ),
                                    rx.el.p(
                                        "Savings",
                                        class_name="text-xs text-green-600 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        f"₹{(m['brand_price'].to(float) - m['generic_price'].to(float)).to_string()} ({((m['brand_price'].to(float) - m['generic_price'].to(float)) / m['brand_price'].to(float) * 100).to_string()} %)",
                                        class_name="text-sm font-bold text-green-600 mb-4",
                                    ),
                                    rx.el.p(
                                        "Jan Aushadhi",
                                        class_name="text-xs text-gray-400 font-bold uppercase mb-1",
                                    ),
                                    rx.cond(
                                        m["is_jan_aushadhi"],
                                        rx.el.p(
                                            "Available",
                                            class_name="text-sm font-bold text-purple-600 mb-4",
                                        ),
                                        rx.el.p(
                                            "No", class_name="text-sm font-medium mb-4"
                                        ),
                                    ),
                                    rx.el.p(
                                        "Approval",
                                        class_name="text-xs text-gray-400 font-bold uppercase mb-1",
                                    ),
                                    rx.el.p(
                                        m["regulatory_status"],
                                        class_name="text-sm font-medium",
                                    ),
                                ),
                                class_name="p-6 bg-white rounded-2xl border border-gray-200 shadow-md flex-1",
                            ),
                        ),
                        class_name="flex flex-col md:flex-row gap-6",
                    ),
                    class_name="mb-12 p-6 bg-gray-50 rounded-2xl",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 py-12",
        ),
        footer(),
        chat_widget(),
        class_name="min-h-screen bg-white font-['Inter'] flex flex-col",
    )


def wrapped_scanner_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        scanner_page(),
        footer(),
        chat_widget(),
        class_name="min-h-screen bg-white font-['Inter'] flex flex-col",
    )


def shop_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Online Medicine Store — Get Generic Medicines Delivered",
                    class_name="text-3xl md:text-5xl font-black text-white text-center py-16 bg-gradient-to-r from-teal-600 to-emerald-500 rounded-3xl shadow-xl shadow-teal-500/20",
                ),
                class_name="max-w-7xl mx-auto px-4 py-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.input(
                        placeholder="Search products...",
                        on_change=ShopState.update_shop_search.debounce(300),
                        class_name="flex-1 px-6 py-3 bg-white border border-gray-200 rounded-xl focus:ring-2 focus:ring-teal-500 outline-none",
                    ),
                    rx.el.select(
                        rx.el.option("All Categories", value="All"),
                        rx.el.option("Analgesic", value="Analgesic"),
                        rx.el.option("Antibiotic", value="Antibiotic"),
                        rx.el.option("Pain Relief", value="Pain Relief"),
                        on_change=ShopState.set_shop_category,
                        class_name="px-6 py-3 bg-white border border-gray-200 rounded-xl outline-none appearance-none",
                    ),
                    rx.el.select(
                        rx.el.option("Best Savings", value="savings"),
                        rx.el.option("Price: Low to High", value="price_low"),
                        rx.el.option("Price: High to Low", value="price_high"),
                        rx.el.option("Name A-Z", value="name"),
                        on_change=ShopState.set_shop_sort,
                        class_name="px-6 py-3 bg-white border border-gray-200 rounded-xl outline-none appearance-none",
                    ),
                    class_name="flex flex-col md:flex-row gap-4 max-w-7xl mx-auto px-4 mb-8",
                ),
                rx.el.div(
                    rx.foreach(
                        ShopState.shop_medicines,
                        lambda m: rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    m["generic_name"],
                                    class_name="text-xl font-black text-gray-900 mb-1",
                                ),
                                rx.el.p(
                                    f"Brand: {m['brand_name']}",
                                    class_name="text-sm font-bold text-gray-500 mb-4",
                                ),
                                rx.el.div(
                                    rx.el.span(
                                        m["dosage_form"],
                                        class_name="px-3 py-1 bg-gray-100 text-gray-600 text-xs font-bold rounded-full mr-2",
                                    ),
                                    rx.cond(
                                        m["is_jan_aushadhi"],
                                        rx.el.span(
                                            "Jan Aushadhi",
                                            class_name="px-3 py-1 bg-purple-100 text-purple-700 text-xs font-bold rounded-full",
                                        ),
                                    ),
                                    class_name="flex items-center mb-6",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        "₹" + m["brand_price"].to_string(),
                                        class_name="text-gray-400 line-through text-sm font-bold",
                                    ),
                                    rx.el.p(
                                        "₹" + m["generic_price"].to_string(),
                                        class_name="text-3xl font-black text-teal-600",
                                    ),
                                    class_name="mb-6",
                                ),
                                rx.el.button(
                                    "Add to Cart",
                                    on_click=lambda: ShopState.add_to_cart(m),
                                    class_name="w-full py-3 bg-teal-500 text-white font-bold rounded-xl hover:bg-teal-600 transition-colors",
                                ),
                                class_name="p-6 bg-white rounded-2xl shadow-sm border border-gray-100 hover:shadow-xl hover:border-teal-200 transition-all",
                            )
                        ),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-7xl mx-auto px-4",
                ),
                class_name="mb-24",
            ),
            rx.cond(
                ShopState.cart_count > 0,
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                ShopState.cart_count.to_string(),
                                " items",
                                class_name="text-white font-bold",
                            ),
                            rx.el.span(" | ", class_name="text-teal-200 mx-4"),
                            rx.el.span(
                                "₹" + ShopState.cart_total.to_string(),
                                class_name="text-white font-black text-xl",
                            ),
                            class_name="flex items-center",
                        ),
                        rx.el.button(
                            "View Cart →",
                            on_click=lambda: rx.redirect("/cart"),
                            class_name="px-6 py-2 bg-white text-teal-600 font-bold rounded-full hover:bg-gray-50",
                        ),
                        class_name="max-w-4xl mx-auto flex justify-between items-center bg-gray-900 p-4 rounded-2xl shadow-2xl",
                    ),
                    class_name="fixed bottom-8 left-0 w-full px-4 z-40 animate-in slide-in-from-bottom-10",
                ),
            ),
        ),
        footer(),
        chat_widget(),
        class_name="min-h-screen bg-gray-50 font-['Inter'] flex flex-col",
    )


def cart_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "Your Cart", class_name="text-4xl font-black text-gray-900 mb-8"
                ),
                rx.cond(
                    ShopState.cart_count > 0,
                    rx.el.div(
                        rx.el.div(
                            rx.foreach(
                                ShopState.cart_items,
                                lambda item: rx.el.div(
                                    rx.el.div(
                                        rx.el.h3(
                                            item["generic_name"],
                                            class_name="font-bold text-gray-900 text-lg",
                                        ),
                                        rx.el.p(
                                            item["salt_composition"],
                                            class_name="text-xs text-gray-500 mb-2",
                                        ),
                                        rx.el.p(
                                            "₹" + item["price"].to_string(),
                                            class_name="font-black text-teal-600",
                                        ),
                                        class_name="flex-1",
                                    ),
                                    rx.el.div(
                                        rx.el.button(
                                            rx.icon("minus", class_name="w-4 h-4"),
                                            on_click=lambda: ShopState.decrement_qty(
                                                item["id"]
                                            ),
                                            class_name="p-2 bg-gray-100 rounded-lg hover:bg-gray-200",
                                        ),
                                        rx.el.span(
                                            item["quantity"].to_string(),
                                            class_name="font-bold px-4",
                                        ),
                                        rx.el.button(
                                            rx.icon("plus", class_name="w-4 h-4"),
                                            on_click=lambda: ShopState.increment_qty(
                                                item["id"]
                                            ),
                                            class_name="p-2 bg-gray-100 rounded-lg hover:bg-gray-200",
                                        ),
                                        class_name="flex items-center",
                                    ),
                                    rx.el.div(
                                        rx.el.p(
                                            "₹"
                                            + (
                                                item["price"] * item["quantity"]
                                            ).to_string(),
                                            class_name="font-black text-gray-900 w-24 text-right",
                                        ),
                                        rx.el.button(
                                            rx.icon(
                                                "trash",
                                                class_name="w-5 h-5 text-red-500",
                                            ),
                                            on_click=lambda: ShopState.remove_from_cart(
                                                item["id"]
                                            ),
                                            class_name="ml-4 p-2 hover:bg-red-50 rounded-lg",
                                        ),
                                        class_name="flex items-center justify-end",
                                    ),
                                    class_name="flex flex-col md:flex-row items-center justify-between p-6 bg-white rounded-2xl mb-4 shadow-sm border border-gray-100",
                                ),
                            ),
                            class_name="lg:col-span-2",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    "Order Summary", class_name="font-bold text-xl mb-6"
                                ),
                                rx.el.div(
                                    rx.el.span("Brand Equivalent Cost:"),
                                    rx.el.span(
                                        "₹" + ShopState.cart_brand_total.to_string(),
                                        class_name="line-through text-gray-400",
                                    ),
                                    class_name="flex justify-between text-gray-500 mb-2",
                                ),
                                rx.el.div(
                                    rx.el.span("Generic Cost:"),
                                    rx.el.span(
                                        "₹" + ShopState.cart_total.to_string(),
                                        class_name="font-bold",
                                    ),
                                    class_name="flex justify-between text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    rx.el.span("You Save:"),
                                    rx.el.span(
                                        "₹" + ShopState.cart_savings.to_string(),
                                        class_name="font-black",
                                    ),
                                    class_name="flex justify-between text-green-600 bg-green-50 p-3 rounded-xl mb-4",
                                ),
                                rx.el.div(
                                    rx.el.span("Delivery Fee:"),
                                    rx.el.span(
                                        rx.cond(
                                            ShopState.delivery_fee == 0.0,
                                            "FREE",
                                            "₹" + ShopState.delivery_fee.to_string(),
                                        ),
                                        class_name="font-bold",
                                    ),
                                    class_name="flex justify-between text-gray-600 mb-6 pb-6 border-b",
                                ),
                                rx.el.div(
                                    rx.el.span(
                                        "Total Amount:", class_name="text-lg font-bold"
                                    ),
                                    rx.el.span(
                                        "₹" + ShopState.order_total.to_string(),
                                        class_name="text-2xl font-black text-teal-600",
                                    ),
                                    class_name="flex justify-between items-center mb-8",
                                ),
                                rx.el.button(
                                    "Proceed to Checkout",
                                    on_click=ShopState.go_to_checkout,
                                    class_name="w-full py-4 bg-teal-600 text-white font-black rounded-xl hover:bg-teal-700 shadow-lg shadow-teal-600/20",
                                ),
                                class_name="p-8 bg-white rounded-3xl shadow-sm border border-gray-100",
                            ),
                            class_name="lg:col-span-1",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
                    ),
                    rx.el.div(
                        rx.icon(
                            "shopping-bag",
                            class_name="h-24 w-24 text-gray-200 mx-auto mb-6",
                        ),
                        rx.el.h3(
                            "Your cart is empty",
                            class_name="text-2xl font-bold text-gray-900 mb-4",
                        ),
                        rx.el.p(
                            "Looks like you haven't added any generic medicines yet.",
                            class_name="text-gray-500 mb-8",
                        ),
                        rx.el.button(
                            "Browse Medicines",
                            on_click=lambda: rx.redirect("/shop"),
                            class_name="px-8 py-3 bg-teal-600 text-white font-bold rounded-full",
                        ),
                        class_name="text-center py-32",
                    ),
                ),
                class_name="max-w-7xl mx-auto px-4 py-12",
            )
        ),
        footer(),
        chat_widget(),
        class_name="min-h-screen bg-gray-50 font-['Inter'] flex flex-col",
    )


def checkout_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            rx.cond(
                ShopState.order_placed,
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "message_circle_check",
                            class_name="h-24 w-24 text-green-500 mx-auto mb-6 animate-bounce",
                        ),
                        rx.el.h1(
                            "Order Placed Successfully!",
                            class_name="text-4xl font-black text-gray-900 mb-4",
                        ),
                        rx.el.p(
                            "Order ID: #" + ShopState.last_order_id,
                            class_name="text-lg font-bold text-gray-500 mb-8",
                        ),
                        rx.el.button(
                            "Continue Shopping",
                            on_click=ShopState.continue_shopping,
                            class_name="px-8 py-4 bg-teal-600 text-white font-black rounded-xl hover:bg-teal-700 transition-colors",
                        ),
                        class_name="bg-white p-12 rounded-3xl shadow-xl max-w-2xl mx-auto text-center",
                    ),
                    class_name="py-24 px-4",
                ),
                rx.el.div(
                    rx.el.h1(
                        "Checkout", class_name="text-3xl font-black text-gray-900 mb-8"
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    "Delivery Address",
                                    class_name="text-xl font-bold mb-6",
                                ),
                                rx.el.div(
                                    rx.el.input(
                                        placeholder="Full Name",
                                        name="name",
                                        class_name="w-full p-3 bg-gray-50 rounded-xl mb-4 outline-none focus:ring-2 focus:ring-teal-500",
                                    ),
                                    rx.el.input(
                                        placeholder="Phone Number",
                                        name="phone",
                                        class_name="w-full p-3 bg-gray-50 rounded-xl mb-4 outline-none focus:ring-2 focus:ring-teal-500",
                                    ),
                                    rx.el.input(
                                        placeholder="Street Address",
                                        name="address",
                                        class_name="w-full p-3 bg-gray-50 rounded-xl mb-4 outline-none focus:ring-2 focus:ring-teal-500",
                                    ),
                                    rx.el.div(
                                        rx.el.input(
                                            placeholder="City",
                                            name="city",
                                            class_name="w-full p-3 bg-gray-50 rounded-xl outline-none focus:ring-2 focus:ring-teal-500",
                                        ),
                                        rx.el.input(
                                            placeholder="PIN Code",
                                            name="pincode",
                                            class_name="w-full p-3 bg-gray-50 rounded-xl outline-none focus:ring-2 focus:ring-teal-500",
                                        ),
                                        class_name="grid grid-cols-2 gap-4 mb-4",
                                    ),
                                    class_name="mb-8",
                                ),
                                rx.el.h3(
                                    "Payment Method",
                                    class_name="text-xl font-bold mb-6",
                                ),
                                rx.el.div(
                                    rx.el.label(
                                        rx.el.input(
                                            type="radio",
                                            name="payment_method",
                                            value="cod",
                                            default_checked=ShopState.payment_method
                                            == "cod",
                                            class_name="mr-3 text-teal-600 focus:ring-teal-500",
                                        ),
                                        rx.el.span(
                                            "Cash on Delivery (COD)",
                                            class_name="font-bold",
                                        ),
                                        class_name="flex items-center p-4 border rounded-xl mb-4 cursor-pointer hover:bg-gray-50",
                                    ),
                                    rx.el.label(
                                        rx.el.input(
                                            type="radio",
                                            name="payment_method",
                                            value="upi",
                                            default_checked=ShopState.payment_method
                                            == "upi",
                                            class_name="mr-3 text-teal-600 focus:ring-teal-500",
                                        ),
                                        rx.el.span(
                                            "UPI Payment", class_name="font-bold"
                                        ),
                                        class_name="flex items-center p-4 border rounded-xl mb-4 cursor-pointer hover:bg-gray-50",
                                    ),
                                ),
                                class_name="p-8 bg-white rounded-3xl shadow-sm",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.h3(
                                        "Order Summary",
                                        class_name="text-xl font-bold mb-6",
                                    ),
                                    rx.foreach(
                                        ShopState.cart_items,
                                        lambda item: rx.el.div(
                                            rx.el.span(
                                                item["generic_name"]
                                                + " (x"
                                                + item["quantity"].to_string()
                                                + ")",
                                                class_name="text-sm text-gray-600",
                                            ),
                                            rx.el.span(
                                                "₹"
                                                + (
                                                    item["price"] * item["quantity"]
                                                ).to_string(),
                                                class_name="font-bold",
                                            ),
                                            class_name="flex justify-between items-center mb-3",
                                        ),
                                    ),
                                    rx.el.div(class_name="h-px bg-gray-200 my-4"),
                                    rx.el.div(
                                        rx.el.span(
                                            "Total Amount:",
                                            class_name="text-lg font-bold",
                                        ),
                                        rx.el.span(
                                            "₹" + ShopState.order_total.to_string(),
                                            class_name="text-2xl font-black text-teal-600",
                                        ),
                                        class_name="flex justify-between items-center mb-8",
                                    ),
                                    rx.cond(
                                        ShopState.checkout_error != "",
                                        rx.el.p(
                                            ShopState.checkout_error,
                                            class_name="text-red-500 text-sm font-bold mb-4 bg-red-50 p-3 rounded-lg",
                                        ),
                                    ),
                                    rx.el.button(
                                        "Place Order",
                                        type="submit",
                                        class_name="w-full py-4 bg-gradient-to-r from-teal-500 to-emerald-500 text-white font-black rounded-xl shadow-lg hover:opacity-90 transition-opacity",
                                    ),
                                    class_name="p-8 bg-white rounded-3xl shadow-sm sticky top-24",
                                )
                            ),
                            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8",
                        ),
                        on_submit=ShopState.place_order,
                    ),
                    class_name="max-w-5xl mx-auto px-4 py-8",
                ),
            )
        ),
        footer(),
        chat_widget(),
        class_name="min-h-screen bg-gray-50 font-['Inter'] flex flex-col",
    )


global_styles = """
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}
@keyframes shimmer {
  0% { background-position: -200% center; }
  100% { background-position: 200% center; }
}
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 20px rgba(13,148,136,0.1); }
  50% { box-shadow: 0 0 40px rgba(13,148,136,0.3); }
}
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
@keyframes pulse-ring {
  0% { transform: scale(0.95); opacity: 0.5; }
  50% { transform: scale(1); opacity: 1; }
  100% { transform: scale(0.95); opacity: 0.5; }
}
@keyframes bounce-gentle {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
.animate-float { animation: float 6s ease-in-out infinite; }
.animate-float-delayed { animation: float 6s ease-in-out infinite 2s; }
.animate-float-slow { animation: float 8s ease-in-out infinite 1s; }
.animate-shimmer { 
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
  background-size: 200% 100%;
  animation: shimmer 3s ease-in-out infinite; 
}
.animate-glow-pulse { animation: glow-pulse 3s ease-in-out infinite; }
.animate-fade-in-up { animation: fade-in-up 0.6s ease-out forwards; }
.animate-fade-in-up-1 { animation: fade-in-up 0.6s ease-out 0.1s forwards; opacity: 0; }
.animate-fade-in-up-2 { animation: fade-in-up 0.6s ease-out 0.2s forwards; opacity: 0; }
.animate-fade-in-up-3 { animation: fade-in-up 0.6s ease-out 0.3s forwards; opacity: 0; }
.animate-fade-in-up-4 { animation: fade-in-up 0.6s ease-out 0.4s forwards; opacity: 0; }
.animate-bounce-gentle { animation: bounce-gentle 2s ease-in-out infinite; }
.gradient-text {
  background: linear-gradient(135deg, #0d9488, #10b981, #06b6d4);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.glass-card {
  background: rgba(255,255,255,0.8);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.5);
}
.hover-lift {
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}
.hover-lift:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px -12px rgba(13,148,136,0.15);
  border-color: rgba(13,148,136,0.3);
}
.card-shine {
  position: relative;
  overflow: hidden;
}
.card-shine::after {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(
    to bottom right,
    rgba(255,255,255,0) 0%,
    rgba(255,255,255,0) 40%,
    rgba(255,255,255,0.4) 50%,
    rgba(255,255,255,0) 60%,
    rgba(255,255,255,0) 100%
  );
  transform: rotate(30deg);
  transition: transform 0.6s;
  pointer-events: none;
}
.card-shine:hover::after {
  transform: rotate(30deg) translateY(-100%);
}
"""
app = rxe.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            rel="stylesheet",
            href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
            integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=",
            cross_origin="",
        ),
        rx.el.style(global_styles),
    ],
)
app.add_page(index, route="/")
app.add_page(shop_page, route="/shop")
app.add_page(cart_page, route="/cart")
app.add_page(checkout_page, route="/checkout", on_load=AuthState.require_auth)
app.add_page(results_page, route="/results")
app.add_page(search_page_view, route="/search")
app.add_page(wrapped_scanner_page, route="/scan")
app.add_page(pharmacies_page, route="/pharmacies")
app.add_page(insights_page, route="/insights")
app.add_page(login_page, route="/login")