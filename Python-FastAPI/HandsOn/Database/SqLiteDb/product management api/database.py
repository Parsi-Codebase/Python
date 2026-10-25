from sqlalchemy import create_engine #create engine for database connection
from sqlalchemy.orm import DeclarativeBase # create base class for models
from sqlalchemy.orm import sessionmaker # create session for database operations
# database connection string
DATABASE_URL='sqlite:///./products.db'
# create engine and session for database operations
engine=create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread':False} # for SQLite
)
# create session for database operations
SessionLocal=sessionmaker(
    bind=engine, # bind session to engine
    autoflush=False # disable autoflush to avoid automatic commit
)
# create base class for models
class Base(DeclarativeBase):
    pass # base class for all models
# create a function to get database session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close() # close the database session after use
