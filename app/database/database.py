from typing import List, Any

import asyncpg

from .tables import ALL_TABLES
from .db_functions import Guilds


class Database:
    def __init__(
        self,
        database: str,
        user: str,
        password: str
    ) -> None:
        self._db_name = database
        self._user = user
        self._password = password

        self.pool: asyncpg.pool.Pool = None

        self.guilds = Guilds(self)

    async def open(self) -> None:
        self.pool = await asyncpg.create_pool(
            database=self._db_name, user=self._user, password=self._password
        )
        await self._create_tables()

    async def execute(self, *args, **kwargs) -> None:
        return await self.pool.execute(*args, **kwargs)

    async def executemany(self, *args, **kwargs) -> None:
        return await self.pool.executemany(*args, **kwargs)

    async def fetch(self, *args, **kwargs) -> List[asyncpg.Record]:
        return await self.pool.fetch(*args, **kwargs)

    async def fetchrow(self, *args, **kwargs) -> asyncpg.Record:
        return await self.pool.fetchrow(*args, **kwargs)

    async def fetchval(self, *args, **kwargs) -> Any:
        return await self.pool.fetchval(*args, **kwargs)

    async def _create_tables(self) -> None:
        for table in ALL_TABLES:
            await self.execute(table)
