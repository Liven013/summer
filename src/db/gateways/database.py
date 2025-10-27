from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.settings import DBSettings

class AsyncDatabase:
    def __init__(self, config: DBSettings=None):
        
        if not config:
            config = DBSettings()
        self.config = config

        url=f"postgresql+asyncpg://{config.user}:{config.password}@{config.host}:{config.port}/{config.db_name}"
        self.engine = create_async_engine(
            url
        )
        self.async_sessionmaker = async_sessionmaker(
            self.engine, expire_on_commit=False
        )

    @asynccontextmanager
    async def db(self):
        async with self.async_sessionmaker() as session:
            yield session

session = AsyncDatabase()

async def get_db_connection():
    async with session.db() as db:
        yield db