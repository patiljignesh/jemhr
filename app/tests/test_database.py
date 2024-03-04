import pytest
from app.database import Base, engine

@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    yield SessionLocal()
    Base.metadata.drop_all(bind=engine)

def test_create_announcement(db_session):
    announcement_data = {
        "title": "Test Announcement",
        "content": "This is a test announcement.",
        "send_at": (datetime.now() + timedelta(minutes=1)).isoformat()
    }
    announcement = crud.create_announcement(db_session, AnnouncementCreate(**announcement_data))
    assert announcement.title == announcement_data["title"]
    assert announcement.content == announcement_data["content"]
    assert announcement.send_at == announcement_data["send_at"]
    assert announcement.status == "pending"

# ...