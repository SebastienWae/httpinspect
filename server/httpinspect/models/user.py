from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from httpinspect.database import Base

if TYPE_CHECKING:
    from httpinspect.models.endpoint import EndpointModel


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003
    email: Mapped[str] = mapped_column(String, unique=True)

    endpoints: Mapped[list["EndpointModel"]] = relationship(
        back_populates="owner",
        cascade="save-update, merge, expunge, delete, delete-orphan",
    )
