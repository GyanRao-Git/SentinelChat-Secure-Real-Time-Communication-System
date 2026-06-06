import asyncpg
import asyncio
from app.core.config import db_settings

async def main():
    conn = await asyncpg.connect(db_settings.PG_CONNECTION_STRING)
    rows= await conn.fetch ("SELECT NOW()")
    print(rows)
    await conn.close()

asyncio.run(main())
