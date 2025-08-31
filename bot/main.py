from logic import *
from dotenv import load_dotenv
load_dotenv(override=True)

import os

TOKEN = os.environ.get("DISCORD_TOKEN")

import discord 
from discord.ext import commands, tasks

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents = intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

class PersistentView(discord.ui.View):
    def __init__(self, owner):
        super().__init__(timeout=None)
        self.owner = owner

class PersistentView(discord.ui.View):
    def __init__(self, owner):
        super().__init__(timeout=None)
        self.owner = owner

    @discord.ui.button(label="Çeviri İngilizce", style=discord.ButtonStyle.primary)
    async def text_translate_en_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        obj = TextAnalysis.memory[self.owner][-1]
        await interaction.response.send_message(obj.translation_en, ephemeral=True)

    @discord.ui.button(label="Çeviri Arapça", style=discord.ButtonStyle.primary)
    async def text_translate_ar_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        obj = TextAnalysis.memory[self.owner][-1]
        await interaction.response.send_message(obj.translation_ar, ephemeral=True)

    @discord.ui.button(label="Cevap Al", style=discord.ButtonStyle.success)
    async def text_ans_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        obj = TextAnalysis.memory[self.owner][-1]
        await interaction.response.send_message(obj.response, ephemeral=True)

@bot.command("start")
async def start(ctx, *, text: str):
    TextAnalysis(text, ctx.author.name)
    view = PersistentView(ctx.author.name)
    await ctx.send("Mesajınızı aldım, ne yapalım?", view = view)

bot.run(TOKEN)