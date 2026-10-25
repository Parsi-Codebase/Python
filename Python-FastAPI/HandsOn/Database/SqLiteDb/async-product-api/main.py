from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Integer, String, Float, select
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# --------------------------------------------------
# 1. FastAPI Application
# --------------------------------------------------

app = FastAPI()


# --------------------------------------------------
# 2. Database Configuration
# --------------------------------------------------

DATABASE_URL = "sqlite+aiosqlite:///./products.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


# --------------------------------------------------
# 3. SQLAlchemy Base
# --------------------------------------------------

class Base(DeclarativeBase):
    pass


# --------------------------------------------------
# 4. Product Model
# --------------------------------------------------

class Product(Base):

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    price: Mapped[float] = mapped_column(
        Float
    )

    quantity: Mapped[int] = mapped_column(
        Integer
    )


# --------------------------------------------------
# 5. Pydantic Models
# --------------------------------------------------

class ProductCreate(BaseModel):

    name: str
    price: float
    quantity: int


class ProductResponse(BaseModel):

    id: int
    name: str
    price: float
    quantity: int

    model_config = {
        "from_attributes": True
    }


# --------------------------------------------------
# 6. Create Database Tables
# --------------------------------------------------

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )


# --------------------------------------------------
# 7. CREATE Product
# --------------------------------------------------

@app.post(
    "/products",
    response_model=ProductResponse
)
async def create_product(product: ProductCreate):

    async with SessionLocal() as session:

        new_product = Product(
            name=product.name,
            price=product.price,
            quantity=product.quantity
        )

        session.add(new_product)

        await session.commit()

        await session.refresh(new_product)

        return new_product


# --------------------------------------------------
# 8. GET All Products
# --------------------------------------------------

@app.get(
    "/products",
    response_model=list[ProductResponse]
)
async def get_products():

    async with SessionLocal() as session:

        result = await session.execute(
            select(Product)
        )

        products = result.scalars().all()

        return products


# --------------------------------------------------
# 9. GET Product By ID
# --------------------------------------------------

@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
async def get_product(product_id: int):

    async with SessionLocal() as session:

        product = await session.get(
            Product,
            product_id
        )

        if product is None:

            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return product


# --------------------------------------------------
# 10. UPDATE Product
# --------------------------------------------------

@app.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
async def update_product(
    product_id: int,
    product_data: ProductCreate
):

    async with SessionLocal() as session:

        product = await session.get(
            Product,
            product_id
        )

        if product is None:

            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        product.name = product_data.name
        product.price = product_data.price
        product.quantity = product_data.quantity

        await session.commit()

        await session.refresh(product)

        return product


# --------------------------------------------------
# 11. DELETE Product
# --------------------------------------------------

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):

    async with SessionLocal() as session:

        product = await session.get(
            Product,
            product_id
        )

        if product is None:

            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        await session.delete(product)

        await session.commit()

        return {
            "message": "Product deleted successfully"
        }