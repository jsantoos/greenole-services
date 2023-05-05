from microservice.app.database import Base, engine, SessionLocal
from microservice.app import database


def test_database():
    try:
        conn = database.engine.connect()
        conn.close()
        database.Base.metadata.create_all(bind=database.engine)
        db = database.SessionLocal()
        assert db.execute("SELECT 1").fetchall() == [(1,)]
        db.close()
    except Exception as e:
        assert False, f"Database connection failed with error: {e}"
