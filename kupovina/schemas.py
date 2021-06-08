from pydantic import BaseModel
from datetime import datetime


class Kupovina(BaseModel):
    kupac: str
    grad: str
    datum_vrijeme: datetime
    proizvod: str
    cijena: float