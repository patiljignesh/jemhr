from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Announcement(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    created_at = Column(DateTime, nullable=False)