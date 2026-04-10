import reflex as rx
import bcrypt
import secrets
import uuid
from datetime import datetime
from app.models import User


class AuthState(rx.State):
    is_logged_in: bool = False
    current_user: dict[str, str] = {}
    session_token: str = ""
    login_error: str = ""
    signup_error: str = ""
    show_login: bool = True
    show_password: bool = False
    show_logout_modal: bool = False

    @rx.event
    def toggle_password_visibility(self):
        self.show_password = not self.show_password

    @rx.event
    def toggle_auth_tab(self):
        self.show_login = not self.show_login
        self.login_error = ""
        self.signup_error = ""

    @rx.event
    def handle_login(self, form_data: dict):
        email = form_data.get("email", "").strip().lower()
        password = form_data.get("password", "").strip()
        if not email or not password:
            self.login_error = "Please fill in all fields"
            return
        with rx.session() as session:
            user = session.exec(User.select().where(User.email == email)).first()
            if not user:
                self.login_error = "No account found with this email"
                return
            if user.provider == "google":
                self.login_error = "This account uses Google Sign-In"
                return
            if not user.password or not bcrypt.checkpw(
                password.encode(), user.password.encode()
            ):
                self.login_error = "Invalid email or password"
                return
            token = secrets.token_urlsafe(32)
            user.session_token = token
            session.add(user)
            session.commit()
            session.refresh(user)
            self.is_logged_in = True
            self.session_token = token
            self.current_user = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone or "",
                "address": user.address or "",
                "provider": user.provider,
                "email_verified": str(user.email_verified),
            }
            self.login_error = ""
        return [
            rx.redirect("/"),
            rx.toast(
                f"Welcome back, {self.current_user.get('name', '')}!", duration=3000
            ),
            rx.call_script(f'localStorage.setItem("medsaver_session", "{token}")'),
        ]

    @rx.event
    def handle_signup(self, form_data: dict):
        name = form_data.get("name", "").strip()
        email = form_data.get("email", "").strip().lower()
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
        with rx.session() as session:
            existing = session.exec(
                User.select().where(User.email == email)
            ).first()
            if existing:
                self.signup_error = "An account with this email already exists"
                return
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User(
                name=name,
                email=email,
                password=hashed,
                phone=phone or None,
                provider="email",
                email_verified=False,
            )
            session.add(new_user)
            session.commit()
        self.signup_error = ""
        self.show_login = True
        return rx.toast("Account created successfully! Please log in.", duration=3000)

    @rx.event
    def show_logout_confirm(self):
        self.show_logout_modal = True

    @rx.event
    def cancel_logout(self):
        self.show_logout_modal = False

    @rx.event
    def confirm_logout(self):
        if self.current_user.get("id"):
            with rx.session() as session:
                user = session.exec(
                    User.select().where(User.id == self.current_user["id"])
                ).first()
                if user:
                    user.session_token = None
                    session.add(user)
                    session.commit()
        self.is_logged_in = False
        self.current_user = {}
        self.session_token = ""
        self.show_logout_modal = False
        return [
            rx.redirect("/"),
            rx.toast("Logged out successfully", duration=3000),
            rx.call_script('localStorage.removeItem("medsaver_session")'),
        ]

    @rx.event
    def logout(self):
        self.show_logout_modal = True

    @rx.event
    def check_session(self):
        return rx.call_script(
            'localStorage.getItem("medsaver_session") || ""',
            callback=AuthState.restore_session,
        )

    @rx.event
    def restore_session(self, token: str):
        if not token:
            return
        with rx.session() as session:
            user = session.exec(
                User.select().where(User.session_token == token)
            ).first()
            if not user:
                return rx.call_script('localStorage.removeItem("medsaver_session")')
            self.is_logged_in = True
            self.session_token = token
            self.current_user = {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "phone": user.phone or "",
                "address": user.address or "",
                "provider": user.provider,
                "email_verified": str(user.email_verified),
            }

    @rx.event
    def require_auth(self):
        if not self.is_logged_in:
            return rx.redirect("/login")

    @rx.event
    def seed_demo_user(self):
        with rx.session() as session:
            existing = session.exec(
                User.select().where(User.email == "demo@medsaver.com")
            ).first()
            if not existing:
                hashed = bcrypt.hashpw("demo123".encode(), bcrypt.gensalt()).decode()
                demo = User(
                    name="Demo User",
                    email="demo@medsaver.com",
                    password=hashed,
                    phone="+91-9876543210",
                    address="Sector 15, Delhi",
                    provider="email",
                    email_verified=True,
                )
                session.add(demo)
                session.commit()
