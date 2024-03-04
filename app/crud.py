from typing import List
from sqlalchemy.orm import Session
from app.models import Announcement
from app.schemas import AnnouncementCreate

def get_announcements(db: Session) -> List[Announcement]:
    return db.query(Announcement).all()

def get_announcement(db: Session, announcement_id: int) -> Announcement:
    return db.query(Announcement).filter(Announcement.id == announcement_id).first()

def create_announcement(db: Session, announcement: AnnouncementCreate) -> Announcement:
    db_announcement = Announcement(title=announcement.title, content=announcement.content)
    db.add(db_announcement)
    db.commit()
    db.refresh(db_announcement)
    return db_announcement