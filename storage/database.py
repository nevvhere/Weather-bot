from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class UserPlace(Base):
    __tablename__ = "user_places"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    place_name = Column(String)

class BannedUser(Base):
    __tablename__ = "banned_users"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=True)

# База данных
engine = create_engine("sqlite:///storage/bot_db.sqlite3")
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
