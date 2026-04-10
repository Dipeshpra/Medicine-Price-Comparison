import reflex as rx


class AuthState(rx.State):
    is_logged_in: bool = False
    current_user: dict[str, str] = {}
    registered_users: list[dict[str, str]] = [
        {
            "name": "Demo User",
            "email": "demo@medsaver.com",
            "phone": "+91-9876543210",
            "password": "demo123",
            "address": "Sector 15, Delhi",
        }
    ]
    login_email: str = ""
    login_password: str = ""
    login_error: str = ""
    login_remember: bool = False
    signup_name: str = ""
    signup_email: str = ""
    signup_phone: str = ""
    signup_password: str = ""
    signup_confirm_password: str = ""
    signup_error: str = ""
    signup_success: bool = False
    show_login: bool = True
    show_password: bool = False

    @rx.event
    def toggle_password_visibility(self):
        self.show_password = not self.show_password

    @rx.event
    def toggle_auth_tab(self):
        self.show_login = not self.show_login
        self.login_error = ""
        self.signup_error = ""
        self.signup_success = False

    @rx.event
    def handle_login(self, form_data: dict[str, str]):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "").strip()
        if not email or not password:
            self.login_error = "Please fill in all fields"
            return
        user = next(
            (
                u
                for u in self.registered_users
                if u["email"] == email and u["password"] == password
            ),
            None,
        )
        if not user:
            self.login_error = "Invalid email or password"
            return
        self.is_logged_in = True
        self.current_user = {
            "name": user["name"],
            "email": user["email"],
            "phone": user["phone"],
            "address": user.get("address", ""),
        }
        self.login_error = ""
        self.login_email = ""
        self.login_password = ""
        return [
            rx.redirect("/"),
            rx.toast(f"Welcome back, {user['name']}!", duration=3000),
        ]

    @rx.event
    def handle_signup(self, form_data: dict[str, str]):
        name = form_data.get("name", "").strip()
        email = form_data.get("email", "").strip()
        phone = form_data.get("phone", "").strip()
        password = form_data.get("password", "").strip()
        confirm = form_data.get("confirm_password", "").strip()
        if not all([name, email, password, confirm]):
            self.signup_error = "Please fill in all required fields"
            return
        if len(password) < 6:
            self.signup_error = "Password must be at least 6 characters"
            return
        if password != confirm:
            self.signup_error = "Passwords do not match"
            return
        if any((u["email"] == email for u in self.registered_users)):
            self.signup_error = "An account with this email already exists"
            return
        self.registered_users.append(
            {
                "name": name,
                "email": email,
                "phone": phone,
                "password": password,
                "address": "",
            }
        )
        self.signup_error = ""
        self.signup_success = True
        self.show_login = True
        return rx.toast("Account created! Please log in.", duration=3000)

    @rx.event
    def logout(self):
        self.is_logged_in = False
        self.current_user = {}
        return [rx.redirect("/"), rx.toast("Logged out successfully", duration=3000)]

    @rx.event
    def require_auth(self):
        """Guard for protected routes — redirect to login if not logged in."""
        if not self.is_logged_in:
            return rx.redirect("/login")