from sqlmodel import Field


class DefaultPrimaryKeyMixin:
    id : int = Field(default=None, primary_key=True)