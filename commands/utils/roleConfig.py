import discord
from functions import *
from discord import app_commands
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="config-role", description="Configurer le role qui changera de couleur.")
    async def roleConfig(self, interaction: discord.Interaction, role: discord.Role):
        config = load_json()
        if interaction.user.id not in config['owners']:
            return await interaction.response.send_message("Tu n'es pas autorisé à utiliser cette commande.", ephemeral=True)
        
        config['roleId'] = role.id
        json.dump(config, open("./config.json", 'w', encoding='utf-8'), indent=4)

        embed = discord.Embed(
            title="`🟢`・Rôle Modifié",
            description=f"*Le rôle {role.mention} sera maintenant un rôle arc-en-ciel*",
            color=embed_color()
        )

        return await interaction.response.send_message(embed=embed)

    
async def setup(bot) -> None:
    await bot.add_cog(PingCommand(bot))