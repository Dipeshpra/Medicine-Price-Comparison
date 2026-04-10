import reflex as rx
import sqlmodel
from datetime import datetime
from typing import Optional
import uuid


class User(rx.Model, table=True):
    """User authentication and profile data."""
    __tablename__ = "users"

    id: str = sqlmodel.Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    name: str = sqlmodel.Field()
    email: str = sqlmodel.Field(unique=True, index=True)
    password: Optional[str] = sqlmodel.Field(default=None)
    provider: str = sqlmodel.Field(default="email")
    email_verified: bool = sqlmodel.Field(default=False)
    phone: Optional[str] = sqlmodel.Field(default=None)
    address: Optional[str] = sqlmodel.Field(default=None)
    session_token: Optional[str] = sqlmodel.Field(default=None, index=True)
    created_at: datetime = sqlmodel.Field(default_factory=datetime.now)


class UserMedicine(rx.Model, table=True):
    """Medicines added by users for expiry tracking."""
    __tablename__ = "user_medicines"

    id: str = sqlmodel.Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    user_id: str = sqlmodel.Field(index=True)
    medicine_name: str = sqlmodel.Field()
    expiry_date: str = sqlmodel.Field()
    dosage: Optional[str] = sqlmodel.Field(default=None)
    notes: Optional[str] = sqlmodel.Field(default=None)
    created_at: datetime = sqlmodel.Field(default_factory=datetime.now)


class MedicineReminder(rx.Model, table=True):
    """Track medicine reminders."""
    __tablename__ = "medicine_reminders"

    id: str = sqlmodel.Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    user_id: str = sqlmodel.Field(index=True)
    medicine_id: str = sqlmodel.Field(index=True)
    reminder_time: str = sqlmodel.Field(default="08:00")
    frequency: str = sqlmodel.Field(default="daily")
    active: bool = sqlmodel.Field(default=True)
    created_at: datetime = sqlmodel.Field(default_factory=datetime.now)
