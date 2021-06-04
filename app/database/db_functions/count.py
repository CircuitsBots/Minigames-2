from app.constants import MISSING
from typing import Any, Dict, List, Optional, TYPE_CHECKING


if TYPE_CHECKING:
    from app.database import Database


class CountingChannels:
    def __init__(self, db: "Database"):
        self.db = db

    async def get(self, channel_id: int) -> Optional[Dict[str, Any]]:
        return await self.db.fetchrow(
            """SELECT * FROM counting_channels
            WHERE id=$1""",
            channel_id,
        )

    async def get_many(self, guild_id: int) -> List[Dict[str, Any]]:
        return await self.db.fetch(
            """SELECT * FROM counting_channels
            WHERE guild_id=$1""",
            guild_id,
        )

    async def create(self, channel_id: int):
        await self.db.execute(
            """INSERT INTO counting_channels (id)
            VALUES ($1)""",
            channel_id,
        )

    async def edit(
        self,
        channel_id: int,
        last: int = MISSING,
        current: int = MISSING,
    ):
        channel = await self.get(channel_id)

        result = {
            "last": channel["last"] if last is MISSING else last,
            "current": channel["current"] if current is MISSING else current,
        }
