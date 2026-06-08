import app.models 
from sqlalchemy.ext.asyncio import AsyncConnection
from asyncio import run
from app.database.session import engine
from app.database.database import Base
from sqlalchemy import text

#borrow ONE connection
async def create_all_tables():
    async with engine.begin() as conn:
        # explicit type hint so my vs code can understand the type
        conn:AsyncConnection
        await conn.run_sync(Base.metadata.create_all)


async def verify_tables():
    async with engine.begin() as conn:
        result = await conn.execute(
            text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            """)
        )

        db_tables = {row[0] for row in result}
        model_tables = set(Base.metadata.tables.keys())

        missing = model_tables - db_tables
        extra = db_tables - model_tables

        print("Models:", model_tables)
        print("Database:", db_tables)
        print("Missing:", missing)
        print("Extra:", extra)

async def main():
    await create_all_tables()
    await verify_tables()

if __name__ == "__main__":
    #run is synchronous 
    run(main())

