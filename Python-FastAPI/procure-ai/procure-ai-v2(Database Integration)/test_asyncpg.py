import asyncio
import asyncpg


async def test():

    connection = await asyncpg.connect(
        user="procureuser",
        password="procurepassword",
        database="procureai",
        host="127.0.0.1",
        port=5433
    )

    print("ASYNCpg CONNECTION SUCCESS")

    result = await connection.fetchrow(
        "SELECT current_user, current_database()"
    )

    print(result)

    await connection.close()


asyncio.run(test())