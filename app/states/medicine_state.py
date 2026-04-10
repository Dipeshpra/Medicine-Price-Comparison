import reflex as rx
from typing import TypedDict


class AlternativeBrand(TypedDict):
    name: str
    price: float
    manufacturer: str


class Medicine(TypedDict):
    id: int
    brand_name: str
    generic_name: str
    salt_composition: str
    brand_price: float
    generic_price: float
    manufacturer: str
    category: str
    is_jan_aushadhi: bool
    is_gov_approved: bool
    dosage_form: str
    dosage_strength: str
    therapeutic_category: str
    regulatory_status: str
    bioequivalence_verified: bool
    typical_dosage_frequency: str
    doses_per_day: int
    typical_course_days: int
    alternative_brands: list[AlternativeBrand]


class MedicineState(rx.State):
    medicines: list[Medicine] = [
        {
            "id": 1,
            "brand_name": "Crocin",
            "generic_name": "Paracetamol",
            "salt_composition": "Paracetamol 500mg",
            "brand_price": 30.5,
            "generic_price": 2.45,
            "manufacturer": "GSK",
            "category": "Analgesic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "500mg",
            "therapeutic_category": "Analgesic & Antipyretic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "3 times/day",
            "doses_per_day": 3,
            "typical_course_days": 5,
            "alternative_brands": [
                {"name": "Dolo 500", "price": 29.0, "manufacturer": "Micro Labs"},
                {"name": "Calpol 500", "price": 28.0, "manufacturer": "GSK"},
                {"name": "P-500", "price": 8.0, "manufacturer": "Cipla"},
            ],
        },
        {
            "id": 2,
            "brand_name": "Augmentin",
            "generic_name": "Amoxicillin + Clavulanic Acid",
            "salt_composition": "Amoxicillin 500mg + Clavulanic Acid 125mg",
            "brand_price": 220.0,
            "generic_price": 55.2,
            "manufacturer": "GSK",
            "category": "Antibiotic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "625mg",
            "therapeutic_category": "Broad-spectrum Antibiotic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 7,
            "alternative_brands": [
                {"name": "Moxikind-CV 625", "price": 160.0, "manufacturer": "Mankind"},
                {"name": "Advent 625", "price": 150.0, "manufacturer": "Cipla"},
                {"name": "Clavam 625", "price": 180.0, "manufacturer": "Alkem"},
            ],
        },
        {
            "id": 3,
            "brand_name": "Combiflam",
            "generic_name": "Ibuprofen + Paracetamol",
            "salt_composition": "Ibuprofen 400mg + Paracetamol 325mg",
            "brand_price": 45.0,
            "generic_price": 5.1,
            "manufacturer": "Sanofi",
            "category": "Pain Relief",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "400mg/325mg",
            "therapeutic_category": "NSAID & Analgesic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 5,
            "alternative_brands": [
                {"name": "Ibugesic Plus", "price": 35.0, "manufacturer": "Cipla"},
                {"name": "Flexon", "price": 28.0, "manufacturer": "Aristo"},
            ],
        },
        {
            "id": 4,
            "brand_name": "Dolo 650",
            "generic_name": "Paracetamol",
            "salt_composition": "Paracetamol 650mg",
            "brand_price": 32.0,
            "generic_price": 2.8,
            "manufacturer": "Micro Labs",
            "category": "Antipyretic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "650mg",
            "therapeutic_category": "Analgesic & Antipyretic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "3 times/day",
            "doses_per_day": 3,
            "typical_course_days": 5,
            "alternative_brands": [
                {"name": "Crocin 650", "price": 30.0, "manufacturer": "GSK"},
                {"name": "Calpol 650", "price": 29.0, "manufacturer": "GSK"},
            ],
        },
        {
            "id": 5,
            "brand_name": "Pan 40",
            "generic_name": "Pantoprazole",
            "salt_composition": "Pantoprazole 40mg",
            "brand_price": 145.0,
            "generic_price": 12.5,
            "manufacturer": "Alkem",
            "category": "Antacid",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "40mg",
            "therapeutic_category": "Proton Pump Inhibitor",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 14,
            "alternative_brands": [
                {"name": "Pantodac 40", "price": 110.0, "manufacturer": "Zydus"},
                {"name": "Pantocid 40", "price": 120.0, "manufacturer": "Sun Pharma"},
                {"name": "Pensec 40", "price": 80.0, "manufacturer": "Cipla"},
            ],
        },
        {
            "id": 6,
            "brand_name": "Voveran",
            "generic_name": "Diclofenac",
            "salt_composition": "Diclofenac 50mg",
            "brand_price": 85.0,
            "generic_price": 8.0,
            "manufacturer": "Novartis",
            "category": "NSAID",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "50mg",
            "therapeutic_category": "NSAID & Pain Relief",
            "regulatory_status": "DCGI Approved",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 5,
            "alternative_brands": [
                {"name": "Reactin 50", "price": 40.0, "manufacturer": "Cipla"},
                {
                    "name": "Dicloran 50",
                    "price": 35.0,
                    "manufacturer": "J.B. Chemicals",
                },
            ],
        },
        {
            "id": 7,
            "brand_name": "Azithral 500",
            "generic_name": "Azithromycin",
            "salt_composition": "Azithromycin 500mg",
            "brand_price": 110.0,
            "generic_price": 24.0,
            "manufacturer": "Alembic",
            "category": "Antibiotic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "500mg",
            "therapeutic_category": "Macrolide Antibiotic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 3,
            "alternative_brands": [
                {"name": "Azee 500", "price": 105.0, "manufacturer": "Cipla"},
                {"name": "Zithrox 500", "price": 85.0, "manufacturer": "Macleods"},
            ],
        },
        {
            "id": 8,
            "brand_name": "Zyrtec",
            "generic_name": "Cetirizine",
            "salt_composition": "Cetirizine 10mg",
            "brand_price": 25.0,
            "generic_price": 1.8,
            "manufacturer": "Dr. Reddy's",
            "category": "Antiallergic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "10mg",
            "therapeutic_category": "Antihistamine",
            "regulatory_status": "DCGI Approved",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 10,
            "alternative_brands": [
                {"name": "Alerid 10", "price": 18.0, "manufacturer": "Cipla"},
                {"name": "Okacet 10", "price": 15.0, "manufacturer": "Cipla"},
                {"name": "Cetzine 10", "price": 16.0, "manufacturer": "Dr. Reddy's"},
            ],
        },
        {
            "id": 9,
            "brand_name": "Glycomet 500",
            "generic_name": "Metformin",
            "salt_composition": "Metformin 500mg",
            "brand_price": 65.0,
            "generic_price": 6.5,
            "manufacturer": "USV",
            "category": "Antidiabetic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "500mg",
            "therapeutic_category": "Biguanide Antidiabetic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 30,
            "alternative_brands": [
                {"name": "Gluconorm 500", "price": 55.0, "manufacturer": "Lupin"},
                {"name": "Cetapin 500", "price": 45.0, "manufacturer": "Sanofi"},
            ],
        },
        {
            "id": 10,
            "brand_name": "Telma 40",
            "generic_name": "Telmisartan",
            "salt_composition": "Telmisartan 40mg",
            "brand_price": 180.0,
            "generic_price": 15.0,
            "manufacturer": "Glenmark",
            "category": "Antihypertensive",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "40mg",
            "therapeutic_category": "Angiotensin II Receptor Blocker",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 30,
            "alternative_brands": [
                {"name": "Tazloc 40", "price": 120.0, "manufacturer": "USV"},
                {"name": "Telmikind 40", "price": 90.0, "manufacturer": "Mankind"},
                {"name": "Telvas 40", "price": 85.0, "manufacturer": "Aristo"},
            ],
        },
        {
            "id": 11,
            "brand_name": "Omez",
            "generic_name": "Omeprazole",
            "salt_composition": "Omeprazole 20mg",
            "brand_price": 55.0,
            "generic_price": 4.5,
            "manufacturer": "Dr. Reddy's",
            "category": "Gastrointestinal",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Capsule",
            "dosage_strength": "20mg",
            "therapeutic_category": "Proton Pump Inhibitor",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 14,
            "alternative_brands": [
                {"name": "Ocid 20", "price": 45.0, "manufacturer": "Zydus"},
                {"name": "Omecip 20", "price": 35.0, "manufacturer": "Cipla"},
            ],
        },
        {
            "id": 12,
            "brand_name": "Thyronorm",
            "generic_name": "Levothyroxine",
            "salt_composition": "Levothyroxine 50mcg",
            "brand_price": 160.0,
            "generic_price": 45.0,
            "manufacturer": "Abbott",
            "category": "Hormonal",
            "is_jan_aushadhi": False,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "50mcg",
            "therapeutic_category": "Thyroid Hormone Replacement",
            "regulatory_status": "DCGI Approved",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 30,
            "alternative_brands": [
                {"name": "Eltroxin 50", "price": 145.0, "manufacturer": "GSK"},
                {"name": "Thyrox 50", "price": 110.0, "manufacturer": "Macleods"},
            ],
        },
        {
            "id": 13,
            "brand_name": "Liv 52",
            "generic_name": "Himalaya Herbal Blend",
            "salt_composition": "Herbal Extracts",
            "brand_price": 120.0,
            "generic_price": 90.0,
            "manufacturer": "Himalaya",
            "category": "Liver Support",
            "is_jan_aushadhi": False,
            "is_gov_approved": True,
            "dosage_form": "Syrup",
            "dosage_strength": "200ml",
            "therapeutic_category": "Hepatoprotective",
            "regulatory_status": "AYUSH Approved",
            "bioequivalence_verified": False,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 30,
            "alternative_brands": [
                {"name": "Amlycure DS", "price": 135.0, "manufacturer": "Aimil"},
                {"name": "Livomyn", "price": 100.0, "manufacturer": "Charak"},
            ],
        },
        {
            "id": 14,
            "brand_name": "Calpol 500",
            "generic_name": "Paracetamol",
            "salt_composition": "Paracetamol 500mg",
            "brand_price": 28.0,
            "generic_price": 2.45,
            "manufacturer": "GSK",
            "category": "Antipyretic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "500mg",
            "therapeutic_category": "Analgesic & Antipyretic",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "3 times/day",
            "doses_per_day": 3,
            "typical_course_days": 5,
            "alternative_brands": [
                {"name": "Crocin 500", "price": 30.5, "manufacturer": "GSK"},
                {"name": "Dolo 500", "price": 29.0, "manufacturer": "Micro Labs"},
            ],
        },
        {
            "id": 15,
            "brand_name": "Avil 25",
            "generic_name": "Pheniramine Maleate",
            "salt_composition": "Pheniramine 25mg",
            "brand_price": 15.0,
            "generic_price": 1.2,
            "manufacturer": "Sanofi",
            "category": "Antihistamine",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "25mg",
            "therapeutic_category": "Antihistamine",
            "regulatory_status": "DCGI Approved",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 5,
            "alternative_brands": [
                {
                    "name": "Pheniramine 25 (Generic)",
                    "price": 1.2,
                    "manufacturer": "Various",
                }
            ],
        },
        {
            "id": 16,
            "brand_name": "Ascoril LS",
            "generic_name": "Ambroxol + Levosalbutamol",
            "salt_composition": "Ambroxol + Levosalbutamol + Guaiphenesin",
            "brand_price": 115.0,
            "generic_price": 35.0,
            "manufacturer": "Glenmark",
            "category": "Cough Syrup",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Syrup",
            "dosage_strength": "100ml",
            "therapeutic_category": "Expectorant & Bronchodilator",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "3 times/day",
            "doses_per_day": 3,
            "typical_course_days": 5,
            "alternative_brands": [
                {"name": "Asthalin AX", "price": 90.0, "manufacturer": "Cipla"},
                {"name": "Macbery LS", "price": 85.0, "manufacturer": "Macleods"},
            ],
        },
        {
            "id": 17,
            "brand_name": "Allegra 120",
            "generic_name": "Fexofenadine",
            "salt_composition": "Fexofenadine 120mg",
            "brand_price": 195.0,
            "generic_price": 45.0,
            "manufacturer": "Sanofi",
            "category": "Antiallergic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "120mg",
            "therapeutic_category": "Non-sedating Antihistamine",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 10,
            "alternative_brands": [
                {"name": "Fexigra 120", "price": 120.0, "manufacturer": "Cipla"},
                {"name": "Hifenac 120", "price": 110.0, "manufacturer": "Macleods"},
            ],
        },
        {
            "id": 18,
            "brand_name": "Betadine",
            "generic_name": "Povidone Iodine",
            "salt_composition": "Povidone Iodine 5%",
            "brand_price": 110.0,
            "generic_price": 40.0,
            "manufacturer": "Win-Medicare",
            "category": "Antiseptic",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Ointment",
            "dosage_strength": "15g",
            "therapeutic_category": "Topical Antiseptic",
            "regulatory_status": "DCGI Approved",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Twice daily",
            "doses_per_day": 2,
            "typical_course_days": 7,
            "alternative_brands": [
                {"name": "Wokadine", "price": 85.0, "manufacturer": "Wockhardt"},
                {"name": "Povicidal", "price": 60.0, "manufacturer": "Cipla"},
            ],
        },
        {
            "id": 19,
            "brand_name": "Ecosprin 75",
            "generic_name": "Aspirin",
            "salt_composition": "Aspirin 75mg",
            "brand_price": 5.0,
            "generic_price": 1.5,
            "manufacturer": "USV",
            "category": "Blood Thinner",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "75mg",
            "therapeutic_category": "Antiplatelet Agent",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 30,
            "alternative_brands": [
                {"name": "Asa 75", "price": 4.0, "manufacturer": "Zydus"},
                {"name": "Sprin 75", "price": 3.5, "manufacturer": "Alkem"},
            ],
        },
        {
            "id": 20,
            "brand_name": "Atorva 10",
            "generic_name": "Atorvastatin",
            "salt_composition": "Atorvastatin 10mg",
            "brand_price": 95.0,
            "generic_price": 12.0,
            "manufacturer": "Zydus",
            "category": "Cholesterol",
            "is_jan_aushadhi": True,
            "is_gov_approved": True,
            "dosage_form": "Tablet",
            "dosage_strength": "10mg",
            "therapeutic_category": "Statin / Lipid Lowering",
            "regulatory_status": "DCGI + WHO-GMP",
            "bioequivalence_verified": True,
            "typical_dosage_frequency": "Once daily",
            "doses_per_day": 1,
            "typical_course_days": 30,
            "alternative_brands": [
                {"name": "Lipvas 10", "price": 65.0, "manufacturer": "Cipla"},
                {"name": "Storvas 10", "price": 55.0, "manufacturer": "Sun Pharma"},
                {"name": "Atorlip 10", "price": 70.0, "manufacturer": "Cipla"},
            ],
        },
    ]
    search_query: str = ""
    selected_medicine: Medicine = {}
    show_suggestions: bool = False
    active_nav: str = "/"
    is_mobile_menu_open: bool = False

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    @rx.var
    def filtered_suggestions(self) -> list[Medicine]:
        if not self.search_query or len(self.search_query) < 2:
            return []
        q = self.search_query.lower()
        return [
            m
            for m in self.medicines
            if q in m["brand_name"].lower() or q in m["generic_name"].lower()
        ][:8]

    @rx.var
    def savings_amount(self) -> float:
        if not self.selected_medicine:
            return 0.0
        return round(
            self.selected_medicine["brand_price"]
            - self.selected_medicine["generic_price"],
            2,
        )

    @rx.var
    def savings_percentage(self) -> float:
        if (
            not self.selected_medicine
            or self.selected_medicine.get("brand_price", 0) == 0
        ):
            return 0.0
        return round(
            self.savings_amount / self.selected_medicine["brand_price"] * 100, 1
        )

    @rx.var
    def monthly_brand_cost(self) -> float:
        if not self.selected_medicine:
            return 0.0
        return round(
            self.selected_medicine.get("brand_price", 0)
            * self.selected_medicine.get("doses_per_day", 1)
            * 30,
            2,
        )

    @rx.var
    def monthly_generic_cost(self) -> float:
        if not self.selected_medicine:
            return 0.0
        return round(
            self.selected_medicine.get("generic_price", 0)
            * self.selected_medicine.get("doses_per_day", 1)
            * 30,
            2,
        )

    @rx.var
    def annual_savings(self) -> float:
        return round((self.monthly_brand_cost - self.monthly_generic_cost) * 12, 2)

    @rx.var
    def savings_tier(self) -> str:
        if self.savings_percentage > 80:
            return "Gold"
        elif self.savings_percentage > 60:
            return "Silver"
        elif self.savings_percentage > 40:
            return "Bronze"
        return "Standard"

    @rx.var
    def substitution_safety(self) -> str:
        return "Safe Substitute - Same Salt Composition"

    @rx.var
    def sorted_alternatives(self) -> list[dict[str, str | float]]:
        if not self.selected_medicine:
            return []
        alts = []
        alts.append(
            {
                "name": self.selected_medicine["brand_name"],
                "price": self.selected_medicine["brand_price"],
                "manufacturer": self.selected_medicine["manufacturer"],
                "is_prescribed": True,
                "is_generic": False,
            }
        )
        alts.append(
            {
                "name": self.selected_medicine["generic_name"] + " (Generic)",
                "price": self.selected_medicine["generic_price"],
                "manufacturer": "Various (Jan Aushadhi)"
                if self.selected_medicine["is_jan_aushadhi"]
                else "Various",
                "is_prescribed": False,
                "is_generic": True,
            }
        )
        for a in self.selected_medicine.get("alternative_brands", []):
            alts.append(
                {
                    "name": a["name"],
                    "price": a["price"],
                    "manufacturer": a["manufacturer"],
                    "is_prescribed": False,
                    "is_generic": False,
                }
            )
        return sorted(alts, key=lambda x: x["price"])

    @rx.var
    def cheapest_brand(self) -> dict[str, str | float]:
        opts = self.sorted_alternatives
        if opts:
            return opts[0]
        return {}

    @rx.var
    def price_alert_active(self) -> bool:
        return self.savings_percentage > 50

    @rx.var
    def chart_data(self) -> list[dict[str, str | float]]:
        if not self.selected_medicine:
            return []
        return [
            {"name": item["name"], "price": item["price"]}
            for item in self.sorted_alternatives
        ]

    @rx.event
    def update_search(self, val: str):
        self.search_query = val
        self.show_suggestions = True

    @rx.event
    def select_medicine(self, medicine: dict[str, str | int | float | bool | list]):
        if hasattr(medicine, "to"):
            self.selected_medicine = medicine.to(dict)
        else:
            self.selected_medicine = dict(medicine)
        brand = medicine["brand_name"]
        self.search_query = brand.to(str) if hasattr(brand, "to") else str(brand)
        self.show_suggestions = False
        return rx.redirect("/results")

    @rx.event
    def set_nav(self, route: str):
        self.active_nav = route
        return rx.redirect(route)

    @rx.event
    def hide_suggestions(self):
        self.show_suggestions = False

    @rx.event
    def on_load_results(self):
        if not self.selected_medicine:
            return rx.redirect("/")

    @rx.event
    def reset_search(self):
        self.search_query = ""
        self.selected_medicine = {}
        self.show_suggestions = False