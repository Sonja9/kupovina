from sqlalchemy import Column, Integer, Float, String
from database import Base


class Kupovina(Base):
    __tablename__ = 'kupovina'
    id = Column (Integer, primary_key=True, index=True)
    kupac = Column(String)
    grad = Column(String)
    datum_vrijeme = Column()
    proizvod = Column(String)
    cijena = Column(Float)