from uuid import UUID, uuid4
from datetime import datetime

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from app.database.database import Base



class Conversation(Base):
    __tablename__ = "conversations"

    conversation_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    conversation_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )  # "dm" or "group"

    name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    created_by: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.user_id"),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
