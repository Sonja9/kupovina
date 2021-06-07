from datetime import datetime
from pydantic import BaseModel


class Kupovina(BaseModel):
    kupac: str
    grad: str
    datum_vrijeme: datetime
    proizvod: str
    cijena: float