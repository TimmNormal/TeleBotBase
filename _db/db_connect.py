
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from _db.conf import DB_NAME, HOST, PASSWORD, USER

def create_connection():
    engine = create_engine(f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
    engine.connect()
    session = Session(bind=engine)
    return session