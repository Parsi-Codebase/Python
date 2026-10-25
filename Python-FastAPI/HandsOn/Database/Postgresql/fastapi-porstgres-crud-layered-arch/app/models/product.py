from sqlalchemy import String,Integer,Float
from sqlalchemy.orm import Mapped,mapped_column
from ..database.database import Base
class Product(Base):
    __tablename__='products'
    id:Mapped[int]=mapped_column(
        Integer,
        primary_key=True,
        index=True
    )
    name:Mapped[str]=mapped_column(
        String(100),
        nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        String(500)
    )

    price: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )