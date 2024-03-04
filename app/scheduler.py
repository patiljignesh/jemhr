import time
import pika
from app.database import SessionLocal
from app.crud import get_announcements
from app.models import Announcement

def on_job_run():
    db = SessionLocal()
    announcements = get_announcements(db)
    db.close()

    for announcement in announcements:
        if announcement.send_at < datetime.now():
            # Update the announcement status
            announcement.status = "sent"
            db = SessionLocal()
            db.add(announcement)
            db.commit()
            db.close()

            # Simulate sending the announcement (e.g., print a confirmation)
            print(f"Announcement {announcement.id} would be sent")