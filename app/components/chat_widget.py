import reflex as rx
from app.states.chat_state import ChatState


def chat_message(msg: dict) -> rx.Component:
    return rx.el.div(
        rx.cond(
            msg["role"] == "bot",
            rx.el.div(
                rx.icon(
                    "bot",
                    class_name="h-6 w-6 text-teal-600 mt-1 shrink-0 p-1 bg-teal-50 rounded-full shadow-sm",
                ),
                rx.el.div(
                    rx.markdown(msg["content"]),
                    class_name="bg-gray-100 text-gray-800 p-3 rounded-2xl rounded-tl-sm text-sm prose prose-sm max-w-none prose-p:my-1 shadow-sm",
                ),
                class_name="flex gap-2 max-w-[85%]",
            ),
            rx.el.div(
                rx.el.p(
                    msg["content"],
                    class_name="bg-gradient-to-br from-teal-500 to-teal-600 text-white p-3 rounded-2xl rounded-tr-sm text-sm shadow-md",
                ),
                class_name="flex gap-2 max-w-[85%] ml-auto",
            ),
        ),
        class_name="mb-4 animate-in fade-in slide-in-from-bottom-2 duration-300",
    )


def typing_indicator() -> rx.Component:
    return rx.el.div(
        rx.icon(
            "bot",
            class_name="h-6 w-6 text-teal-600 mt-1 shrink-0 p-1 bg-teal-50 rounded-full shadow-sm",
        ),
        rx.el.div(
            rx.el.div(
                class_name="w-2 h-2 bg-teal-400 rounded-full animate-bounce",
                style={"animationDelay": "0ms"},
            ),
            rx.el.div(
                class_name="w-2 h-2 bg-teal-500 rounded-full animate-bounce",
                style={"animationDelay": "150ms"},
            ),
            rx.el.div(
                class_name="w-2 h-2 bg-teal-600 rounded-full animate-bounce",
                style={"animationDelay": "300ms"},
            ),
            class_name="bg-gray-100 p-4 rounded-2xl rounded-tl-sm flex gap-1.5 items-center h-[38px] shadow-sm",
        ),
        class_name="flex gap-2 mb-4 animate-in fade-in",
    )


def suggested_chip(question: str) -> rx.Component:
    return rx.el.button(
        question,
        on_click=lambda: ChatState.send_suggested_question(question),
        class_name="whitespace-nowrap px-4 py-2 bg-white border border-teal-100 text-teal-700 text-xs font-bold rounded-full hover:bg-teal-50 hover:border-teal-300 hover:-translate-y-0.5 transition-all shadow-sm shrink-0",
    )


def chat_widget() -> rx.Component:
    return rx.el.div(
        rx.cond(
            ChatState.is_open,
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "sparkles",
                                class_name="h-5 w-5 text-white animate-pulse",
                            ),
                            class_name="bg-white/20 p-2 rounded-xl shadow-inner",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "MedSaver Assistant",
                                class_name="text-white font-black leading-tight tracking-wide",
                            ),
                            rx.el.p(
                                "Online and ready to help",
                                class_name="text-teal-100 text-xs font-medium",
                            ),
                        ),
                        class_name="flex items-center gap-3",
                    ),
                    rx.el.button(
                        rx.icon(
                            "x",
                            class_name="h-5 w-5 text-teal-100 hover:text-white transition-colors",
                        ),
                        on_click=ChatState.toggle_chat,
                        class_name="hover:bg-white/20 p-1.5 rounded-xl transition-all",
                    ),
                    class_name="bg-gradient-to-r from-teal-600 via-teal-500 to-emerald-500 p-5 rounded-t-2xl flex justify-between items-center shadow-md z-10",
                ),
                rx.el.div(
                    rx.foreach(ChatState.messages, chat_message),
                    rx.cond(ChatState.is_typing, typing_indicator()),
                    class_name="p-5 h-96 overflow-y-auto bg-gray-50 flex-1 scroll-smooth",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.foreach(ChatState.suggested_questions, suggested_chip),
                        class_name="flex overflow-x-auto gap-2 p-3 bg-white border-t border-gray-100 no-scrollbar",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.input(
                                placeholder="Ask anything about medicines...",
                                name="message",
                                class_name="flex-1 bg-gray-50 border border-gray-200 rounded-2xl px-4 py-3.5 text-sm focus:outline-none focus:border-teal-500 focus:ring-4 focus:ring-teal-500/20 focus:bg-white transition-all shadow-inner",
                            ),
                            rx.el.button(
                                rx.icon("send", class_name="h-4 w-4 ml-0.5"),
                                type="submit",
                                class_name="bg-gradient-to-br from-teal-500 to-teal-600 text-white p-3.5 rounded-2xl hover:opacity-90 hover:scale-105 transition-all shadow-md flex items-center justify-center",
                            ),
                            class_name="flex gap-2 items-center",
                        ),
                        on_submit=ChatState.handle_submit,
                        reset_on_submit=True,
                        class_name="p-4 bg-white rounded-b-2xl border-t border-gray-50",
                    ),
                    class_name="shadow-[0_-10px_20px_-10px_rgba(0,0,0,0.05)] z-10 relative",
                ),
                class_name="fixed bottom-24 right-6 w-[360px] md:w-[420px] bg-white rounded-2xl shadow-[0_20px_60px_-15px_rgba(13,148,136,0.3)] border border-gray-100/50 z-50 flex flex-col animate-in slide-in-from-bottom-8 fade-in duration-300 origin-bottom-right",
            ),
        ),
        rx.el.button(
            rx.icon("message_circle", class_name="h-7 w-7"),
            rx.el.div(
                class_name="absolute inset-0 rounded-full border-2 border-teal-400 animate-ping opacity-75 duration-1000"
            ),
            on_click=ChatState.toggle_chat,
            class_name="fixed bottom-6 right-6 h-16 w-16 bg-gradient-to-br from-teal-500 to-teal-600 text-white rounded-full flex items-center justify-center shadow-[0_10px_25px_-5px_rgba(13,148,136,0.5)] hover:scale-110 hover:shadow-[0_15px_35px_-5px_rgba(13,148,136,0.6)] transition-all z-50",
        ),
    )