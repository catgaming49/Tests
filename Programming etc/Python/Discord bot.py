import discord
import random
from discord import app_commands
client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

potmessages = ["ben", "yes", "no"]

amongusmessages = ["among", "sus", "amongus", "vent", "bedrager", "iblandt", "task", "tasks", "oppgave", "oppgaver", "imposter", "elektrisk", "electrical"]

@tree.command(name = "getroles", description = "Get your current roles", guild=discord.Object(1022549466655506532))
async def handleInput(interaction):
    roles_array = interaction.user.roles
    array52=[]
    for i in roles_array:
        if str(i) != "@everyone":
            array52.append(i.name)
    await interaction.response.send_message("Your roles are: "+', '.join(array52))

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1022549466655506532))
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    if str(message.author) != str(client.user):
        if any([x in str(message.content.lower()) for x in amongusmessages]):
            await message.channel.send("Amongus!!??!!")

    if message.content.startswith("!ben"):
        rand = random. randint(0, 3)
        times = 0
        for x in potmessages:
            if times == rand:
                await message.channel.send(x)
            times = times + 1

client.run("MTA1Mjg1MzQyMTIzNDk5NTIwMA.GeGcY5.VxQ5Ot-vmbK_iiutwgecz23ZHo2JblfcHfmwDk")