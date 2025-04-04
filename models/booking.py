from datetime import date
from pydantic import BaseModel, Field

class Booking(BaseModel):
  id: str = Field(description='booking id, start with OTBH followed by integers, eg OTBH12345')
  hotel_id: int = Field(description='hotel id')
  hotel_name: str = Field(description='hotel name')
  arrival_date: date = Field(description='arrival date')