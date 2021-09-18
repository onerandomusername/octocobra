#!/usr/bin/env python3

from disnake.ext import commands, tasks
import disnake

import config
from cogs.utils import db

initial_extensions = (
    'cogs.tags',
)
SLASH_COMMAND_GUILDS = (
    859290967475879966, # m1raynee's test
    808030843078836254  # disnake
)

class DisnakeHelper(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=disnake.Intents.all(),
            test_guilds=SLASH_COMMAND_GUILDS,
            **kwargs
        )

        for ext in initial_extensions:
            try:
                self.load_extension(ext)
            except Exception as e:
                print(f'Could not load extension {ext} due to {e.__class__.__name__}: {e}')
        
        self.loop.run_until_complete(db.init())

    async def on_ready(self):
        print(f'Logged on as {self.user} (ID: {self.user.id})')