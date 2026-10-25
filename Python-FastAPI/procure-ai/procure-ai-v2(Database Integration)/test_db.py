import asyncio

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from app.core.config import settings


async def test():

    print("URL:", settings.database_url)

    engine = create_async_engine(
        settings.database_url
    )

    async with engine.connect() as connection:

        result = await connection.execute(
            text("SELECT current_user, current_database()")
        )

        print(result.fetchone())

    await engine.dispose()


asyncio.run(test())