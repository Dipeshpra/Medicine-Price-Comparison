import reflex as rx
from app.states.scan_state import ScanState
from app.states.medicine_state import Medicine


def scanned_medicine_card(medicine: Medicine) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Brand Detected",
                    class_name="text-xs font-bold text-gray-400 uppercase",
                ),
                rx.el.h3(
                    medicine["brand_name"], class_name="text-xl font-bold text-gray-900"
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "Generic Alternative",
                    class_name="text-xs font-bold text-teal-600 uppercase text-right",
                ),
                rx.el.h3(
                    medicine["generic_name"],
                    class_name="text-xl font-bold text-teal-700 text-right",
                ),
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Brand Price: ",
                    rx.el.span(
                        "₹" + medicine["brand_price"].to_string(),
                        class_name="line-through",
                    ),
                    class_name="text-sm text-gray-500",
                ),
                rx.el.p(
                    "Generic Price: ",
                    rx.el.span(
                        "₹" + medicine["generic_price"].to_string(),
                        class_name="font-bold",
                    ),
                    class_name="text-sm text-gray-900",
                ),
            ),
            rx.el.div(
                rx.el.p(
                    "Save", class_name="text-xs text-green-700 font-bold uppercase mb-1"
                ),
                rx.el.p(
                    "₹",
                    (
                        medicine["brand_price"].to(float)
                        - medicine["generic_price"].to(float)
                    ).to_string(),
                    class_name="text-xl font-black text-green-600",
                ),
                class_name="bg-green-50 px-4 py-2 rounded-xl text-center",
            ),
            class_name="flex justify-between items-end mb-6",
        ),
        rx.el.button(
            "View Details & Compare",
            on_click=lambda: ScanState.select_scanned_medicine(medicine),
            class_name="w-full py-3 bg-teal-50 text-teal-700 font-bold rounded-xl hover:bg-teal-100 transition-colors",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow",
    )


def scanner_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Scan Prescription",
                        class_name="text-4xl font-black text-gray-900 mb-3",
                    ),
                    rx.el.p(
                        "Upload your prescription or medicine box to instantly find affordable generic alternatives using our smart OCR engine.",
                        class_name="text-gray-500 font-medium",
                    ),
                    class_name="text-center mb-12",
                ),
                rx.upload.root(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "scan-line",
                                class_name="h-16 w-16 text-teal-500 mb-6 animate-pulse",
                            ),
                            rx.el.p(
                                "Click or drop your prescription image here",
                                class_name="text-xl font-bold text-gray-800 mb-2",
                            ),
                            rx.el.p(
                                "Secure processing • Supports JPG, PNG, WEBP",
                                class_name="text-sm text-gray-400 font-medium",
                            ),
                            class_name="flex flex-col items-center justify-center py-16 px-10 border-4 border-dashed border-teal-200 bg-teal-50/20 rounded-[2.5rem] cursor-pointer hover:bg-teal-50/40 transition-all duration-300 hover:border-teal-400 group",
                        )
                    ),
                    id="prescription_upload",
                    accept={
                        "image/png": [".png"],
                        "image/jpeg": [".jpg", ".jpeg"],
                        "image/webp": [".webp"],
                    },
                    max_files=1,
                    on_drop=ScanState.handle_upload(
                        rx.upload_files(upload_id="prescription_upload")
                    ),
                    class_name="mb-10 shadow-2xl shadow-teal-500/5",
                ),
                rx.cond(
                    ScanState.processing,
                    rx.el.div(
                        rx.spinner(size="3", class_name="text-teal-600 mb-6"),
                        rx.el.p(
                            "Analyzing your prescription...",
                            class_name="text-teal-700 font-black animate-pulse text-lg",
                        ),
                        class_name="flex flex-col items-center py-16 bg-white rounded-3xl border border-gray-100 shadow-sm",
                    ),
                ),
                rx.cond(
                    (ScanState.uploaded_image != "") & ~ScanState.processing,
                    rx.el.div(
                        rx.el.h2(
                            "Detected Medicines",
                            class_name="text-2xl font-black text-gray-900 mb-8 flex items-center",
                        ),
                        rx.cond(
                            ScanState.detected_medicines.length() > 0,
                            rx.el.div(
                                rx.foreach(
                                    ScanState.detected_medicines, scanned_medicine_card
                                ),
                                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "search-x",
                                    class_name="h-12 w-12 text-gray-200 mb-4 mx-auto",
                                ),
                                rx.el.p(
                                    "We couldn't detect any recognized medicines in the uploaded image. Please ensure the image is clear.",
                                    class_name="text-gray-500 font-bold max-w-sm mx-auto",
                                ),
                                class_name="text-center p-16 bg-gray-50/50 rounded-3xl border border-gray-100",
                            ),
                        ),
                        rx.el.details(
                            rx.el.summary(
                                "View Raw OCR Text",
                                class_name="cursor-pointer text-xs font-black text-teal-600 uppercase tracking-widest mt-12 mb-4 hover:text-teal-700 transition-colors",
                            ),
                            rx.el.div(
                                ScanState.raw_text,
                                class_name="p-6 bg-gray-900 text-teal-400 rounded-2xl text-xs font-mono whitespace-pre-wrap max-h-64 overflow-y-auto border border-gray-800 shadow-inner",
                            ),
                        ),
                        class_name="mt-16 animate-fade-in-up",
                    ),
                ),
                class_name="max-w-4xl mx-auto",
            ),
            class_name="max-w-7xl mx-auto",
        ),
        class_name="py-20 px-4 bg-white min-h-[70vh]",
    )