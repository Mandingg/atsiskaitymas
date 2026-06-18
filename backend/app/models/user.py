from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Literal
import re


class UserCreateModel(BaseModel):
    name: str = Field(min_length=1, max_length=55)
    surname: str = Field(min_length=1, max_length=55)
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=8, max_length=72)

    @field_validator("password")
    @classmethod
    def validate_password(cls, value: str) -> str:
        
        if not re.search(r"[A-Z]", value):
            raise ValueError(
                "Slaptažodyje turi būti bent viena didžioji raidė")
        if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", value):
            raise ValueError(
                "Slaptažodyje turi būti bent vienas specialus simbolis")
        return value


class UserLoginModel(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)


class UserResponseModel(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    role: Literal["ADMIN", "USER"]


class TokenResponseModel(BaseModel):
    access_token: str
    token_type: str
