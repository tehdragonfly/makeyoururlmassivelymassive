from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import String, UnicodeText

engine = create_engine("sqlite:///makeyoururlmassivelymassive.db")
session = scoped_session(sessionmaker(bind=engine, autoflush=False))

Base = declarative_base(bind=engine)

class MassiveURL(Base):
    __tablename__ = "massive_urls"
    id = Column(String(40), primary_key=True, nullable=False)
    url = Column(UnicodeText, nullable=False)
