import discord
from discord.ext import commands
from discord import app_commands

class ErenCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="chat")
    async def chat(self, ctx, *, text: str):
        """與艾連對話"""
        async with ctx.typing():
            response = self.bot.llm.generate_response(text)
            await ctx.send(response)
            
    @commands.command(name="chat_with_image")
    async def chat_with_image(self, ctx, *, text: str):
        """與艾連對話（包含圖片）"""
        if not ctx.message.attachments:
            await ctx.send("Hmph, you didn't attach any image...")
            return
            
        image_url = ctx.message.attachments[0].url
        async with ctx.typing():
            response = self.bot.llm.generate_response(text, image_url)
            await ctx.send(response)
            
    @commands.command(name="chat_with_youtube")
    async def chat_with_youtube(self, ctx, youtube_url: str):
        """與艾連討論 YouTube 影片內容"""
        async with ctx.typing():
            await ctx.send("Hmph, let me watch this video and tell you what I think...")
            response = self.bot.llm.process_youtube_video(youtube_url)
            await ctx.send(response)
            
    @commands.command(name="chat_zh")
    async def chat_zh(self, ctx, *, text: str):
        """與中文版艾連對話"""
        async with ctx.typing():
            response = self.bot.llm_zh.generate_response(text)
            await ctx.send(response)
            
    @commands.command(name="chat_with_image_zh")
    async def chat_with_image_zh(self, ctx, *, text: str):
        """與中文版艾連對話（包含圖片）"""
        if not ctx.message.attachments:
            await ctx.send("哼，你沒有附上任何圖片...")
            return
            
        image_url = ctx.message.attachments[0].url
        async with ctx.typing():
            response = self.bot.llm_zh.generate_response(text, image_url)
            await ctx.send(response)
            
    @commands.command(name="chat_with_youtube_zh")
    async def chat_with_youtube_zh(self, ctx, youtube_url: str):
        """與中文版艾連討論 YouTube 影片內容"""
        async with ctx.typing():
            await ctx.send("哼，讓我看看這個影片，然後告訴你我的想法...")
            response = self.bot.llm_zh.process_youtube_video(youtube_url)
            await ctx.send(response)
            
    @commands.command(name="ping")
    async def ping(self, ctx):
        """測試機器人的延遲"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'延遲: {latency}ms')

async def setup(bot):
    await bot.add_cog(ErenCommands(bot)) 