from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.core.config import db_settings

DB_URI = db_settings.PG_CONNECTION_STRING

# adding "+asyncpg", used when sqlalchemy parses URI and figures out database(pg), driver(asyncpg).. etc
new_URI = DB_URI.replace("postgresql://", "postgresql+asyncpg://")

engine = create_engine(
    new_URI, 
    echo=True,  # logs all SQL queries to console (useful for debugging)
    pool_pre_ping=True,  # checks if DB connection is alive before using it
    pool_size=5,  # number of persistent connections kept open in the pool
    max_overflow=5,  # extra temporary connections allowed beyond pool_size
    pool_timeout=30,  # seconds to wait for a free connection before erroring
    # closes/recreates connections older than 30 minutes to avoid stale connections
    pool_recycle=1800
)

session = async_sessionmaker(
    bind= engine,
    expire_on_commit= False, #reuse the same values and not pull from db evertime
)
