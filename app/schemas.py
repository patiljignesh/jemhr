from datetime import datetime
from pydantic import BaseModel
from app.models import Announcement

class AnnouncementCreate(BaseModel):
    title: str
    content: str
    send_at: datetime

    @classmethod
    def from_orm(cls, announcement: Announcement):
        return cls(title=announcement.title, content=announcement.content, send_at=announcement.send_at)