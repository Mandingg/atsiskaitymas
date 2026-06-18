from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class BookModel(BaseModel):
    id: int
    user_id: int
    title: str
    author: str
    category: str
    rating: int
    description: str | None = None
    created_at: datetime


class BookCreateModel(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    author: str = Field(..., min_length=1, max_length=255)
    category: str = Field(..., min_length=1, max_length=55)
    rating: int = Field(..., ge=1, le=5)
    description: str | None = None


class BookUpdateModel(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=255)
    author: str | None = Field(None, min_length=1, max_length=255)
    category: str | None = Field(None, min_length=1, max_length=55)
    rating: int | None = Field(None, ge=1, le=5)
    description: str | None = None


class BookResponseModel(BaseModel):
    id: int
    title: str
    author: str
    category: str
    description: Optional[str] = None
    message: str