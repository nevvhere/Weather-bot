from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class UserPlace(Base):
    __tablename__ = "user_places"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    place_name = Column(String)

engine = create_engine("sqlite:///storage/user_places.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
