from pydantic import BaseModel, Field


class StudentV1(BaseModel):

    name: str = Field(
        examples=["John"]
    )

    age: int = Field(
        examples=[25]
    )


class StudentV2(BaseModel):

    full_name: str = Field(
        examples=["John Smith"]
    )

    age: int = Field(
        examples=[25]
    )

    email: str = Field(
        examples=["john@example.com"]
    )