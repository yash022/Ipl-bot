import discord
from IPL import *

client = discord.Client()

@client.event
async def on_message(message):
    
    if message.content == "!scoreboard":
        general_channel = client.get_channel(#your channel ID)
        await general_channel.send(teams_data(),tts=True)

    if message.content == "!open ipl website":
        general_channel = client.get_channel(#your channel ID)
        await general_channel.send(open_IPL_website(),tts=True)

    if message.content == "!latest score":
        general_channel = client.get_channel(#your channel ID)
        await general_channel.send(latest_match_score(),tts=True)

    if message.content == "!msd":
        general_channel = client.get_channel(#your channel ID)
        await general_channel.send(play_ipl_msd_song(),tts=True)

    if message.content == "!match schedule":
        general_channel = client.get_channel(#your channel ID)
        await general_channel.send(match_schedule(),tts=True)

    if message.content == "!next match":
            general_channel = client.get_channel(#your channel ID)
            await general_channel.send(next_match(),tts=True)

    if message.content == "!ipl news":
            general_channel = client.get_channel(#your channel ID)
            await general_channel.send(ipl_news(),tts=True)

    if "team members of" in message.content:
        general_channel = client.get_channel(#your channel ID)
        team=str(message.content).replace("team members of"," ")
        members=team_members(team)
        await general_channel.send(members,tts=True)

    if message.content == "!help":
        general_channel = client.get_channel(#your channel ID)
        help_data =help()
        await general_channel.send(help_data,tts=True)


client.run("#your bots token")
