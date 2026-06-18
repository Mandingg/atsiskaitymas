from pydantic import BaseModel, Field
from datetime import datetime


class CategoryModel(BaseModel):
    id: int
    name: str
    created_at: datetime


class CategoryCreateModel(BaseModel):
    name: str = Field(..., min_length=1, max_length=55)


class CategoryUpdateModel(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=55)