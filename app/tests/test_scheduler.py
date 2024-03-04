import pytest
from app.scheduler import on_job_run
from app.database import SessionLocal
from app.models import Announcement
from app.database import Base
from app.schemas import AnnouncementCreate

@pytest.fixture(scope="module")
def db_session():
    db = SessionLocal()
    yield db
    db.rollback()

def test_on_job_run(db_session):
    announcement_data = {
        "title": "Test Announcement",
        "content": "This is a test announcement.",
        "send_at": (datetime.now() + timedelta(minutes=1)).isoformat()
    }
    announcement = crud.create_announcement(db_session, AnnouncementCreate(**announcement_data))
    on_job_run()
    announcement.refresh(db_session)
    assert announcement.status == "sent"

# ...