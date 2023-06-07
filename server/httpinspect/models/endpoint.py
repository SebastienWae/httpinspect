from __future__ import annotations

from typing import TYPE_CHECKING
from uuid import UUID  # noqa: TCH003

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Uuid

from httpinspect.database import Base

if TYPE_CHECKING:
    from httpinspect.models.user import UserModel


class EndpointModel(Base):
    __tablename__ = "endpoints"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)  # noqa: A003
    name: Mapped[str] = mapped_column(String)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    owner: Mapped["UserModel"] = relationship(
        back_populates="endpoints",
        cascade="save-update, merge, expunge",
    )
