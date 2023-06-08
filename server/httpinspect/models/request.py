from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from httpinspect.database import Base

if TYPE_CHECKING:
    from httpinspect.models.endpoint import EndpointModel


class RequestModel(Base):
    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(primary_key=True)  # noqa: A003

    endpoint_id: Mapped[int] = mapped_column(ForeignKey("endpoints.id"))
    endpoint: Mapped["EndpointModel"] = relationship(
        back_populates="requests",
        cascade="save-update, merge, expunge",
    )
