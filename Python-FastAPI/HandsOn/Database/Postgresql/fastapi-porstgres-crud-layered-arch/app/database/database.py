from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
DATABASE_URL = "postgresql+psycopg://procureuser:procurepassword@localhost:5433/procuredb"
engine=create_engine(
    DATABASE_URL,
    echo=True
)
sessionLocal=sessionmaker(
    bind=engine,
    autoflush=False
)
class Base(DeclarativeBase):
    pass
def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()