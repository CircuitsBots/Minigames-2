import typing

import discord
from discord.ext import commands

if typing.TYPE_CHECKING:
    from .database import Database


EXTENSIONS = []


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        self.db: Database = kwargs.pop("database")
        super().__init__(*args, **kwargs)

        for ext in EXTENSIONS:
            self.load_extension(ext)

    async def before_invoke(self, ctx: commands.Context) -> None:
        await self.create_data(ctx.message)

    async def create_data(self, message: discord.Message) -> None:
        pass

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user} in {len(self.guilds)} guilds!")
