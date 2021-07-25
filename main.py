import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print('Bot is ready')

@bot.event
async def on_message(message):
    if message.author == bot.user():
        return
    else:
        if str(message.channel.type) == 'private':
            guild = bot.get_guild(YOUR GUILD ID)
            channels = await guild.fetch_channels()
            channel = discord.utils.get(channels, name = str(message.author.id))
            if channel is None:
                catagory = discord.utils.get(guild.catagories, name = 'Tickets')
                channel = await guild.create_text_channel(message.author.id, catagory = catagory)

            embedVar = discord.Embed(title = f'{message.author} Has sent a new message', discription = message.content, color = 0x00ff00)
            await channel.send(embed = embedVar)

@bot.command(discription = 'Send a private message through modmail, only mods can use this command.')
@commands.has_permissions(manage_messages = True)
async def send(ctx, user: discord.User, *, message):
    embedVar = discord.Embed(title = 'The moderators have sent you a new message.', discription = message, color = 0x00ff00)
    await user.send(embed = embedVar)

@bot.command(discription = 'Close a ticket using this command, only mods can use this.')
@commands.has_permissions(manage_messages = True)
async def close(ctx):
    await ctx.message.channel.delete()


bot.run('YOUR BOT TOKEN')