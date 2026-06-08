from uuid import UUID, uuid4
from datetime import datetime, UTC

from sqlalchemy import String, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from app.database.database import Base


class Message(Base):
    __tablename__ = "messages"

    message_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    conversation_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("conversations.conversation_id"),
        nullable=False,
        index=True
    )

    sender_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.user_id"),
        nullable=False,
        index=True
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    message_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="text"
    )

    sent_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: func.now(),
        nullable=False
    )
