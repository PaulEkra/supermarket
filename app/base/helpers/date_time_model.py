from datetime import datetime
from typing import Optional

from sqlalchemy import Column, DateTime, func
from sqlmodel import Field, SQLModel

from base.mixins.default_primary_key import DefaultPrimaryKeyMixin


class DateTimeModel(DefaultPrimaryKeyMixin,SQLModel):
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),         
            nullable=False,
        )
    )

    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True),
            server_default=func.now(),          
            onupdate=func.now(),                
            nullable=False,
        )
    )
    
    is_deleted: bool = False
