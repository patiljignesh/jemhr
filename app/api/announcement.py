from typing import List
from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import Database
from app.crud import get_announcements, get_announcement, create_announcement
from app.models import Announcement
from app.schemas import AnnouncementCreate
from app.rabbitmq_producer import send_announcement


router = APIRouter()

@router.post("/announcements/", response_model=AnnouncementCreate)
async def create_announcement_endpoint(announcement: AnnouncementCreate):
    db_announcement = create_announcement(db, announcement)
    send_announcement(db_announcement)
    return db_announcement

@router.get("/announcements/{announcement_id}", response_model=AnnouncementCreate)
async def read_announcement(announcement_id: int):
    db = Database.get_db()
    announcement = get_announcement(db, announcement_id)
    if not announcement:
        raise HTTPException(status_code=404, detail="Announcement not found")
    return announcement

@router.get("/announcements/", response_model=list[AnnouncementCreate])
async def read_announcements():
    db = Database.get_db()
    announcements = get_announcements(db)
    return [AnnouncementCreate.from_orm(announcement) for announcement in announcements]
