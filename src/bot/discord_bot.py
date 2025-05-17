import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from ..llm.eren_llm import ErenLLM
from ..llm.eren_llm_zh import ErenLLMZh

load_dotenv()

class ErenBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
        self.llm = ErenLLM()
        self.llm_zh = ErenLLMZh()
        
    async def setup_hook(self):
        # 載入所有命令
        await self.load_extension('src.bot.commands')
        
    async def on_ready(self):
        print(f'{self.user} 已經成功登入！')
        
    def run_bot(self):
        self.run(os.getenv('DISCORD_TOKEN')) 