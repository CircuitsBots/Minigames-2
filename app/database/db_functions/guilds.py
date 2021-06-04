from typing import Any, Dict, Optional, TYPE_CHECKING

import asyncpg

if TYPE_CHECKING:
    from app.database import Database


class Guilds:
    def __init__(self, db: "Database"):
        self.db = db

    async def get(self, guild_id: int) -> Optional[Dict[str, Any]]:
        return await self.db.fetchrow(
            """SELECT * FROM guilds
            WHERE id=$1""",
            guild_id,
        )

    async def create(self, guild_id: int):
        try:
            await self.db.execute(
                """INSERT INTO guilds (id) VALUES ($1)""",
                guild_id,
            )
        except asyncpg.exceptions.UniqueViolationError:
            pass
