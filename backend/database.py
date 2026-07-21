import os

from pathlib import Path
from dotenv import load_dotenv

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Index
from sqlalchemy.orm import declarative_base, sessionmaker

# Force load .env from the exact same directory as database.py
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Note: index speeds up searches on columns, but slows down inserts and updates.

# Song table
class Song(Base):
    __tablename__ = "songs"

    song_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, default="Unknown")

# Fingerprint table
class Fingerprint(Base):
    __tablename__ = "fingerprints"

    fingerprint_id = Column(Integer, primary_key=True, index=True)
    hash = Column(String(40), index=True, nullable=False)
    song_id = Column(Integer, ForeignKey("songs.song_id", ondelete="CASCADE"))
    offset_ms = Column(Integer, nullable=False) # Offset in ms from the start of the song

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created successfully.")

