import discord
from functions import *
from _colors import Colors
from discord.ext import commands, tasks

class rainbowColor(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.change_color.start() 
        self.C = Colors()

    @tasks.loop(seconds=10)
    async def change_color(self):
        config = load_json()
        guild: discord.Guild = self.bot.get_guild(config['guildId'])
        if guild:
            role: discord.Role = guild.get_role(config['roleId'])
            if role:
                try:
                    await role.edit(color=discord.Color.random())
                    print(f"{self.C.CYAN}[CHANGING] {self.C.WHITE}La couleur du rôle à été modifié.")
                except Exception as e:
                    print(f"{self.C.RED}[ERROR] {self.C.WHITE}Une erreur est survenue lors de la modification du role.")

    @change_color.before_loop
    async def before_change_color(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(rainbowColor(bot))