from base.helpers.date_time_model import DateTimeModel
from sqlmodel import Field

class NamedDateTimeModel(DateTimeModel):
    name:str = Field(max_length=100, nullable=False)