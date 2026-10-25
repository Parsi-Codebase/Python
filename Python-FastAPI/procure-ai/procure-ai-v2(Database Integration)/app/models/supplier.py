from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from app.models.base import Base
class Supplier(Base):
    __tablename__='suppliers'
    id:Mapped[int]=mapped_column(
        primary_key=True
    )
    name:Mapped[str]=mapped_column(
        String(100),
        nullable=False
    )
    email:Mapped[str]=mapped_column(
        String(150),
        unique=True,
        nullable=False
    )
    phone:Mapped[str]=mapped_column(
        String(15),
        nullable=False
    )
    city:Mapped[str]=mapped_column(
        String(50),
        nullable=False
    )
    
    