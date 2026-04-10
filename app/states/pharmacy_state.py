import reflex as rx
from typing import TypedDict
import time
from reflex_enterprise.components.map.types import LatLng, latlng


class Pharmacy(TypedDict):
    id: int
    name: str
    address: str
    city: str
    distance_km: float
    phone: str
    type: str
    lat: float
    lng: float
    rating: float
    is_open: bool
    available_medicines: list[int]


class PharmacyState(rx.State):
    user_lat: float = 0.0
    user_lng: float = 0.0
    location_status: str = "idle"
    loading_pharmacies: bool = False
    default_city: str = "Delhi"
    INDIAN_CITIES = [
        {"name": "Delhi", "lat": 28.6139, "lng": 77.209},
        {"name": "Mumbai", "lat": 19.076, "lng": 72.8777},
        {"name": "Bangalore", "lat": 12.9716, "lng": 77.5946},
        {"name": "Chennai", "lat": 13.0827, "lng": 80.2707},
        {"name": "Kolkata", "lat": 22.5726, "lng": 88.3639},
        {"name": "Hyderabad", "lat": 17.385, "lng": 78.4867},
        {"name": "Pune", "lat": 18.5204, "lng": 73.8567},
        {"name": "Ahmedabad", "lat": 23.0225, "lng": 72.5714},
        {"name": "Jaipur", "lat": 26.9124, "lng": 75.7873},
        {"name": "Lucknow", "lat": 26.8467, "lng": 80.9462},
        {"name": "Noida", "lat": 28.5355, "lng": 77.391},
        {"name": "Gurgaon", "lat": 28.4595, "lng": 77.0266},
    ]
    pharmacies: list[Pharmacy] = [
        {
            "id": 1,
            "name": "Jan Aushadhi Kendra - Sector 15",
            "address": "Shop No. 4, Main Market, Sector 15",
            "city": "Delhi",
            "distance_km": 1.2,
            "phone": "+91-9876543210",
            "type": "Jan Aushadhi Kendra",
            "lat": 28.7041,
            "lng": 77.1025,
            "rating": 4.8,
            "is_open": True,
            "available_medicines": [1, 2, 4, 7, 10],
        },
        {
            "id": 2,
            "name": "Apollo Pharmacy",
            "address": "Ground Floor, City Center Mall",
            "city": "Delhi",
            "distance_km": 2.5,
            "phone": "+91-11-23456789",
            "type": "Medical Store",
            "lat": 28.6139,
            "lng": 77.209,
            "rating": 4.5,
            "is_open": True,
            "available_medicines": [1, 3, 5, 8],
        },
        {
            "id": 3,
            "name": "MedPlus Pharmacy",
            "address": "Near Metro Station, Dwarka",
            "city": "Delhi",
            "distance_km": 3.1,
            "phone": "+91-9988776655",
            "type": "Medical Store",
            "lat": 28.5823,
            "lng": 77.05,
            "rating": 4.2,
            "is_open": False,
            "available_medicines": [2, 6, 9, 11],
        },
        {
            "id": 4,
            "name": "Generic Aarogya Store",
            "address": "Block C, Vasant Kunj",
            "city": "Delhi",
            "distance_km": 4.0,
            "phone": "+91-8877665544",
            "type": "Generic Store",
            "lat": 28.5293,
            "lng": 77.1539,
            "rating": 4.6,
            "is_open": True,
            "available_medicines": [1, 2, 4, 6, 12],
        },
        {
            "id": 5,
            "name": "Pradhan Mantri Jan Aushadhi Kendra",
            "address": "Hospital Road, Rohini",
            "city": "Delhi",
            "distance_km": 5.2,
            "phone": "+91-7766554433",
            "type": "Jan Aushadhi Kendra",
            "lat": 28.7366,
            "lng": 77.113,
            "rating": 4.9,
            "is_open": True,
            "available_medicines": [1, 4, 7, 9, 14, 15],
        },
        {
            "id": 6,
            "name": "Wellness Medicals",
            "address": "Main Bazar, Lajpat Nagar",
            "city": "Delhi",
            "distance_km": 6.5,
            "phone": "+91-6655443322",
            "type": "Medical Store",
            "lat": 28.5677,
            "lng": 77.2433,
            "rating": 4.1,
            "is_open": True,
            "available_medicines": [3, 5, 8, 10, 16],
        },
        {
            "id": 7,
            "name": "Sanjivani Generic Meds",
            "address": "Opp. SBI Bank, Janakpuri",
            "city": "Delhi",
            "distance_km": 7.0,
            "phone": "+91-5544332211",
            "type": "Generic Store",
            "lat": 28.6219,
            "lng": 77.0878,
            "rating": 4.4,
            "is_open": True,
            "available_medicines": [2, 4, 6, 8, 17],
        },
        {
            "id": 8,
            "name": "Care Pharmacy",
            "address": "Sector 18 Market",
            "city": "Noida",
            "distance_km": 8.2,
            "phone": "+91-4433221100",
            "type": "Medical Store",
            "lat": 28.5708,
            "lng": 77.3271,
            "rating": 4.3,
            "is_open": True,
            "available_medicines": [1, 5, 9, 11, 13],
        },
        {
            "id": 9,
            "name": "Jan Aushadhi Kendra - Kalkaji",
            "address": "Central Market, Kalkaji",
            "city": "Delhi",
            "distance_km": 9.1,
            "phone": "+91-3322110099",
            "type": "Jan Aushadhi Kendra",
            "lat": 28.5401,
            "lng": 77.257,
            "rating": 4.7,
            "is_open": False,
            "available_medicines": [1, 2, 4, 7, 10, 14, 18],
        },
        {
            "id": 10,
            "name": "LifeCare Generics",
            "address": "Near Civil Hospital",
            "city": "Delhi",
            "distance_km": 10.5,
            "phone": "+91-2211009988",
            "type": "Generic Store",
            "lat": 28.6616,
            "lng": 77.2273,
            "rating": 4.5,
            "is_open": True,
            "available_medicines": [3, 6, 9, 12, 19],
        },
        {
            "id": 11,
            "name": "City Pharmacy",
            "address": "Connaught Place",
            "city": "Delhi",
            "distance_km": 12.0,
            "phone": "+91-1100998877",
            "type": "Medical Store",
            "lat": 28.6315,
            "lng": 77.2167,
            "rating": 4.6,
            "is_open": True,
            "available_medicines": [1, 2, 3, 5, 8, 11, 20],
        },
        {
            "id": 12,
            "name": "Jan Aushadhi Kendra - East",
            "address": "Preet Vihar",
            "city": "Delhi",
            "distance_km": 14.3,
            "phone": "+91-9988112233",
            "type": "Jan Aushadhi Kendra",
            "lat": 28.6389,
            "lng": 77.2965,
            "rating": 4.8,
            "is_open": True,
            "available_medicines": [1, 4, 7, 9, 10, 14],
        },
        {
            "id": 13,
            "name": "Jan Aushadhi Kendra - Andheri",
            "address": "Andheri East Station Road",
            "city": "Mumbai",
            "distance_km": 1.5,
            "phone": "+91-9876541230",
            "type": "Jan Aushadhi Kendra",
            "lat": 19.1136,
            "lng": 72.8697,
            "rating": 4.7,
            "is_open": True,
            "available_medicines": [1, 3, 5, 7],
        },
        {
            "id": 14,
            "name": "Bandra Generics",
            "address": "Hill Road, Bandra West",
            "city": "Mumbai",
            "distance_km": 3.0,
            "phone": "+91-9988771122",
            "type": "Generic Store",
            "lat": 19.0596,
            "lng": 72.8295,
            "rating": 4.5,
            "is_open": True,
            "available_medicines": [2, 4, 6, 8],
        },
        {
            "id": 15,
            "name": "Dadar Medical Center",
            "address": "Dadar TT Circle",
            "city": "Mumbai",
            "distance_km": 4.5,
            "phone": "+91-8877662233",
            "type": "Medical Store",
            "lat": 19.0178,
            "lng": 72.8478,
            "rating": 4.3,
            "is_open": True,
            "available_medicines": [9, 10, 11, 12],
        },
        {
            "id": 16,
            "name": "Borivali Health Pharmacy",
            "address": "SV Road, Borivali West",
            "city": "Mumbai",
            "distance_km": 8.0,
            "phone": "+91-7766553344",
            "type": "Medical Store",
            "lat": 19.2307,
            "lng": 72.8567,
            "rating": 4.6,
            "is_open": False,
            "available_medicines": [13, 14, 15, 16],
        },
        {
            "id": 17,
            "name": "Thane Jan Aushadhi",
            "address": "Gokhale Road, Thane West",
            "city": "Mumbai",
            "distance_km": 12.5,
            "phone": "+91-6655442211",
            "type": "Jan Aushadhi Kendra",
            "lat": 19.197,
            "lng": 72.9635,
            "rating": 4.8,
            "is_open": True,
            "available_medicines": [17, 18, 19, 20],
        },
        {
            "id": 18,
            "name": "Koramangala Generics",
            "address": "80ft Road, Koramangala 4th Block",
            "city": "Bangalore",
            "distance_km": 2.0,
            "phone": "+91-9123456780",
            "type": "Generic Store",
            "lat": 12.9352,
            "lng": 77.6245,
            "rating": 4.6,
            "is_open": True,
            "available_medicines": [1, 2, 3, 4],
        },
        {
            "id": 19,
            "name": "Whitefield Medicals",
            "address": "ITPL Main Road",
            "city": "Bangalore",
            "distance_km": 15.0,
            "phone": "+91-9234567890",
            "type": "Medical Store",
            "lat": 12.9698,
            "lng": 77.7499,
            "rating": 4.2,
            "is_open": True,
            "available_medicines": [5, 6, 7, 8],
        },
        {
            "id": 20,
            "name": "Jayanagar Jan Aushadhi",
            "address": "4th Block, Jayanagar",
            "city": "Bangalore",
            "distance_km": 4.5,
            "phone": "+91-9345678901",
            "type": "Jan Aushadhi Kendra",
            "lat": 12.9299,
            "lng": 77.5824,
            "rating": 4.9,
            "is_open": True,
            "available_medicines": [9, 10, 11, 12],
        },
        {
            "id": 21,
            "name": "MG Road Pharmacy",
            "address": "Brigade Road Junction",
            "city": "Bangalore",
            "distance_km": 1.0,
            "phone": "+91-9456789012",
            "type": "Medical Store",
            "lat": 12.9719,
            "lng": 77.601,
            "rating": 4.4,
            "is_open": False,
            "available_medicines": [13, 14, 15, 16],
        },
        {
            "id": 22,
            "name": "T Nagar Generics",
            "address": "Pondy Bazaar",
            "city": "Chennai",
            "distance_km": 3.5,
            "phone": "+91-9567890123",
            "type": "Generic Store",
            "lat": 13.0382,
            "lng": 80.2364,
            "rating": 4.5,
            "is_open": True,
            "available_medicines": [17, 18, 19, 20],
        },
        {
            "id": 23,
            "name": "Anna Nagar Jan Aushadhi",
            "address": "2nd Avenue",
            "city": "Chennai",
            "distance_km": 5.0,
            "phone": "+91-9678901234",
            "type": "Jan Aushadhi Kendra",
            "lat": 13.085,
            "lng": 80.2101,
            "rating": 4.8,
            "is_open": True,
            "available_medicines": [1, 3, 5, 7],
        },
        {
            "id": 24,
            "name": "Adyar Medicals",
            "address": "LB Road",
            "city": "Chennai",
            "distance_km": 7.5,
            "phone": "+91-9789012345",
            "type": "Medical Store",
            "lat": 13.0012,
            "lng": 80.2565,
            "rating": 4.3,
            "is_open": True,
            "available_medicines": [2, 4, 6, 8],
        },
        {
            "id": 25,
            "name": "Tambaram Health Pharmacy",
            "address": "Mudichur Road",
            "city": "Chennai",
            "distance_km": 20.0,
            "phone": "+91-9890123456",
            "type": "Medical Store",
            "lat": 12.9249,
            "lng": 80.1,
            "rating": 4.1,
            "is_open": False,
            "available_medicines": [9, 10, 11, 12],
        },
        {
            "id": 26,
            "name": "Salt Lake Jan Aushadhi",
            "address": "Sector V",
            "city": "Kolkata",
            "distance_km": 6.0,
            "phone": "+91-8123456789",
            "type": "Jan Aushadhi Kendra",
            "lat": 22.5801,
            "lng": 88.4378,
            "rating": 4.7,
            "is_open": True,
            "available_medicines": [13, 14, 15, 16],
        },
        {
            "id": 27,
            "name": "Park Street Pharmacy",
            "address": "Park Street Crossing",
            "city": "Kolkata",
            "distance_km": 1.5,
            "phone": "+91-8234567890",
            "type": "Medical Store",
            "lat": 22.5535,
            "lng": 88.3516,
            "rating": 4.5,
            "is_open": True,
            "available_medicines": [17, 18, 19, 20],
        },
        {
            "id": 28,
            "name": "Howrah Generic Meds",
            "address": "Near Howrah Station",
            "city": "Kolkata",
            "distance_km": 4.0,
            "phone": "+91-8345678901",
            "type": "Generic Store",
            "lat": 22.5833,
            "lng": 88.3167,
            "rating": 4.4,
            "is_open": True,
            "available_medicines": [1, 2, 3, 4],
        },
        {
            "id": 29,
            "name": "Banjara Hills Medicals",
            "address": "Road No. 1",
            "city": "Hyderabad",
            "distance_km": 5.0,
            "phone": "+91-7123456789",
            "type": "Medical Store",
            "lat": 17.4156,
            "lng": 78.4347,
            "rating": 4.2,
            "is_open": True,
            "available_medicines": [5, 6, 7, 8],
        },
        {
            "id": 30,
            "name": "Secunderabad Jan Aushadhi",
            "address": "SD Road",
            "city": "Hyderabad",
            "distance_km": 8.0,
            "phone": "+91-7234567890",
            "type": "Jan Aushadhi Kendra",
            "lat": 17.4399,
            "lng": 78.4983,
            "rating": 4.8,
            "is_open": True,
            "available_medicines": [9, 10, 11, 12],
        },
        {
            "id": 31,
            "name": "Kukatpally Generics",
            "address": "KPHB Colony",
            "city": "Hyderabad",
            "distance_km": 12.0,
            "phone": "+91-7345678901",
            "type": "Generic Store",
            "lat": 17.4843,
            "lng": 78.3889,
            "rating": 4.6,
            "is_open": False,
            "available_medicines": [13, 14, 15, 16],
        },
        {
            "id": 32,
            "name": "Kothrud Jan Aushadhi",
            "address": "Karve Road",
            "city": "Pune",
            "distance_km": 4.5,
            "phone": "+91-6123456789",
            "type": "Jan Aushadhi Kendra",
            "lat": 18.5074,
            "lng": 73.8077,
            "rating": 4.9,
            "is_open": True,
            "available_medicines": [17, 18, 19, 20],
        },
        {
            "id": 33,
            "name": "Hinjewadi Medical Store",
            "address": "Phase 1",
            "city": "Pune",
            "distance_km": 15.0,
            "phone": "+91-6234567890",
            "type": "Medical Store",
            "lat": 18.5913,
            "lng": 73.7389,
            "rating": 4.3,
            "is_open": True,
            "available_medicines": [1, 3, 5, 7],
        },
        {
            "id": 34,
            "name": "Navrangpura Generics",
            "address": "CG Road",
            "city": "Ahmedabad",
            "distance_km": 3.0,
            "phone": "+91-5123456789",
            "type": "Generic Store",
            "lat": 23.0365,
            "lng": 72.5611,
            "rating": 4.5,
            "is_open": True,
            "available_medicines": [2, 4, 6, 8],
        },
        {
            "id": 35,
            "name": "SG Highway Jan Aushadhi",
            "address": "Near ISKCON Cross Road",
            "city": "Ahmedabad",
            "distance_km": 8.5,
            "phone": "+91-5234567890",
            "type": "Jan Aushadhi Kendra",
            "lat": 23.0258,
            "lng": 72.5074,
            "rating": 4.7,
            "is_open": True,
            "available_medicines": [9, 10, 11, 12],
        },
        {
            "id": 36,
            "name": "MI Road Pharmacy",
            "address": "Panch Batti",
            "city": "Jaipur",
            "distance_km": 2.0,
            "phone": "+91-4123456789",
            "type": "Medical Store",
            "lat": 26.9152,
            "lng": 75.8041,
            "rating": 4.4,
            "is_open": True,
            "available_medicines": [13, 14, 15, 16],
        },
        {
            "id": 37,
            "name": "Malviya Nagar Jan Aushadhi",
            "address": "Sector 3",
            "city": "Jaipur",
            "distance_km": 6.0,
            "phone": "+91-4234567890",
            "type": "Jan Aushadhi Kendra",
            "lat": 26.853,
            "lng": 75.8166,
            "rating": 4.8,
            "is_open": True,
            "available_medicines": [17, 18, 19, 20],
        },
        {
            "id": 38,
            "name": "Hazratganj Generics",
            "address": "MG Marg",
            "city": "Lucknow",
            "distance_km": 1.5,
            "phone": "+91-3123456789",
            "type": "Generic Store",
            "lat": 26.8496,
            "lng": 80.9392,
            "rating": 4.6,
            "is_open": True,
            "available_medicines": [1, 2, 3, 4],
        },
        {
            "id": 39,
            "name": "Gomti Nagar Jan Aushadhi",
            "address": "Vikas Khand",
            "city": "Lucknow",
            "distance_km": 8.0,
            "phone": "+91-3234567890",
            "type": "Jan Aushadhi Kendra",
            "lat": 26.8465,
            "lng": 81.0003,
            "rating": 4.7,
            "is_open": False,
            "available_medicines": [5, 6, 7, 8],
        },
    ]
    search_filter: str = ""
    type_filter: str = "All"
    sort_by: str = "distance"
    city_search: str = ""
    selected_city: str = ""
    show_city_suggestions: bool = False
    show_report_modal: bool = False
    report_pharmacy_id: int = 0
    report_medicine_name: str = ""
    report_status: str = "Available"
    reports: list[dict[str, str | int]] = []
    medicine_search: str = ""
    radius_filter: str = "All"
    matched_medicine_ids: list[int] = []

    @rx.event
    def set_radius_filter(self, val: str):
        self.radius_filter = val

    @rx.event
    async def update_medicine_search(self, val: str):
        self.medicine_search = val
        if not val or len(val) < 2:
            self.matched_medicine_ids = []
            return
        from app.states.medicine_state import MedicineState

        medicine_state = await self.get_state(MedicineState)
        q = val.lower()
        self.matched_medicine_ids = [
            m["id"]
            for m in medicine_state.medicines
            if q in m["brand_name"].lower()
            or q in m["generic_name"].lower()
            or q in m["salt_composition"].lower()
        ]

    @rx.var
    def filtered_city_suggestions(self) -> list[dict[str, str | float]]:
        if not self.city_search:
            return []
        search_lower = self.city_search.lower()
        return [c for c in self.INDIAN_CITIES if search_lower in c["name"].lower()]

    def _haversine(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        import math

        R = 6371
        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(math.radians(lat1))
            * math.cos(math.radians(lat2))
            * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * c, 1)

    @rx.event
    def receive_geolocation(self, coords: list):
        if len(coords) == 2:
            lat = float(coords[0])
            lng = float(coords[1])
            if lat == 0 and lng == 0:
                self.location_status = "denied"
                self.selected_city = "Delhi"
                self.city_search = "Delhi"
                import reflex_enterprise as rxe

                map_api = rxe.map.api("pharmacy-map")
                return map_api.fly_to(latlng(lat=28.6139, lng=77.209), 12.0)
            self.user_lat = lat
            self.user_lng = lng
            self.location_status = "allowed"
            self.selected_city = ""
            self.city_search = ""
            updated = []
            for p in self.pharmacies:
                new_p = dict(p)
                new_p["distance_km"] = self._haversine(
                    self.user_lat, self.user_lng, p["lat"], p["lng"]
                )
                updated.append(new_p)
            self.pharmacies = updated
            import reflex_enterprise as rxe

            map_api = rxe.map.api("pharmacy-map")
            return map_api.fly_to(latlng(lat=self.user_lat, lng=self.user_lng), 13.0)
        else:
            self.location_status = "error"

    @rx.event
    def geolocation_denied(self):
        self.location_status = "denied"

    @rx.event
    def geolocation_error(self, msg: str):
        self.location_status = "error"

    @rx.event
    def request_geolocation(self):
        self.location_status = "detecting"
        return rx.call_script(
            """
            new Promise((resolve, reject) => {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(
                        (pos) => {
                            console.log("Geolocation success:", pos.coords.latitude, pos.coords.longitude);
                            resolve([pos.coords.latitude, pos.coords.longitude]);
                        },
                        (err) => {
                            console.log("Geolocation error:", err.code, err.message);
                            resolve([0, 0]);
                        },
                        { enableHighAccuracy: true, timeout: 10000, maximumAge: 300000 }
                    );
                } else {
                    console.log("Geolocation not supported");
                    resolve([0, 0]);
                }
            })
            """,
            callback=PharmacyState.receive_geolocation,
        )

    @rx.var
    def map_center(self) -> LatLng:
        if self.location_status == "allowed" and self.user_lat != 0:
            return latlng(lat=self.user_lat, lng=self.user_lng)
        if self.selected_city:
            city = next(
                (c for c in self.INDIAN_CITIES if c["name"] == self.selected_city), None
            )
            if city:
                return latlng(lat=city["lat"], lng=city["lng"])
        return latlng(lat=20.5937, lng=78.9629)

    @rx.var
    def nearby_pharmacy_count(self) -> int:
        return len(self.filtered_pharmacies)

    @rx.event
    def fly_to_pharmacy(self, lat: float, lng: float):
        import reflex_enterprise as rxe

        map_api = rxe.map.api("pharmacy-map")
        return map_api.fly_to(latlng(lat=lat, lng=lng), 15.0)

    @rx.event
    def update_city_search(self, val: str):
        self.city_search = val
        self.show_city_suggestions = True

    @rx.event
    def hide_city_suggestions(self):
        self.show_city_suggestions = False

    @rx.event
    def select_city(self, city: dict):
        name = city["name"]
        lat_val = city["lat"]
        lng_val = city["lng"]
        self.selected_city = name.to(str) if hasattr(name, "to") else str(name)
        self.city_search = name.to(str) if hasattr(name, "to") else str(name)
        self.show_city_suggestions = False
        final_lat = lat_val.to(float) if hasattr(lat_val, "to") else float(lat_val)
        final_lng = lng_val.to(float) if hasattr(lng_val, "to") else float(lng_val)
        import reflex_enterprise as rxe

        map_api = rxe.map.api("pharmacy-map")
        return map_api.fly_to(latlng(lat=final_lat, lng=final_lng), 12.0)

    @rx.event
    def clear_city_search(self):
        self.selected_city = ""
        self.city_search = ""
        self.show_city_suggestions = False
        import reflex_enterprise as rxe

        map_api = rxe.map.api("pharmacy-map")
        return map_api.fly_to(latlng(lat=20.5937, lng=78.9629), 5.0)

    @rx.var
    def filtered_pharmacies(self) -> list[Pharmacy]:
        results = self.pharmacies
        if self.selected_city:
            results = [p for p in results if p["city"] == self.selected_city]
        if self.type_filter != "All":
            results = [p for p in results if p["type"] == self.type_filter]
        if self.search_filter:
            q = self.search_filter.lower()
            results = [
                p
                for p in results
                if q in p["name"].lower() or q in p["address"].lower()
            ]
        if self.medicine_search and len(self.medicine_search) >= 2:
            if not self.matched_medicine_ids:
                return []
            results = [
                p
                for p in results
                if any(
                    (
                        m_id in p["available_medicines"]
                        for m_id in self.matched_medicine_ids
                    )
                )
            ]
        if self.radius_filter != "All" and self.location_status == "allowed":
            try:
                radius = float(self.radius_filter)
                results = [p for p in results if p["distance_km"] <= radius]
            except ValueError:
                pass
        if self.sort_by == "rating":
            results.sort(key=lambda x: x["rating"], reverse=True)
        else:
            results.sort(key=lambda x: x["distance_km"])
        return results

    @rx.event
    def set_search_filter(self, val: str):
        self.search_filter = val

    @rx.event
    def set_type_filter(self, val: str):
        self.type_filter = val

    @rx.event
    def set_sort_by(self, val: str):
        self.sort_by = val

    @rx.event
    def toggle_report_modal(self):
        self.show_report_modal = not self.show_report_modal
        if not self.show_report_modal:
            self.report_medicine_name = ""
            self.report_status = "Available"

    @rx.event
    def open_report_modal(self, pharmacy_id: int):
        self.report_pharmacy_id = pharmacy_id
        self.show_report_modal = True

    @rx.event
    def set_report_medicine_name(self, val: str):
        self.report_medicine_name = val

    @rx.event
    def set_report_status(self, val: str):
        self.report_status = val

    @rx.event
    def submit_report(self):
        if not self.report_medicine_name.strip():
            return rx.toast("Please enter a medicine name")
        pharmacy = next(
            (p for p in self.pharmacies if p["id"] == self.report_pharmacy_id), None
        )
        pharmacy_name = pharmacy["name"] if pharmacy else "Unknown"
        self.reports.insert(
            0,
            {
                "pharmacy_id": self.report_pharmacy_id,
                "pharmacy_name": pharmacy_name,
                "medicine_name": self.report_medicine_name,
                "status": self.report_status,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            },
        )
        self.show_report_modal = False
        self.report_medicine_name = ""
        self.report_status = "Available"
        return rx.toast(
            "Report submitted successfully! Thank you for helping the community."
        )