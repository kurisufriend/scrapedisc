API_TOKEN: str = "" # bot token
FILTER_TEXT: list = ["https", "is a level", "historytest"] # a list of strings to match for message exclusion

import os
import discord
import io
import sys

discordClient: discord.Client = discord.Client()

currentPath: str = os.getcwd()
outputDirPath: str = currentPath + "/out"
print(currentPath)

if (not(os.path.isdir(outputDirPath))):
    print("output directory not found, creating it now")
    os.mkdir(outputDirPath)

outputFile: io.TextIOWrapper = io.open(outputDirPath + "/output.txt", "a", encoding="utf-8")

@discordClient.event
async def on_message(message: discord.Message):
    if ("$historytest" in message.content):
        channel: discord.TextChannel = message.channel; print("cp1")
        messageList: list = await channel.history(limit=100000, oldest_first=True).flatten(); print("cp2")
        for currentMessage in messageList:
            messageText: str = currentMessage.content
            shouldSkip: bool = False # doing like this hurts me but im too brainlet to reset two loops
            for keyword in FILTER_TEXT:
                if (keyword in messageText.lower()):
                    shouldSkip = True
                    break
            if (shouldSkip):
                continue
            outputFile.write(messageText + "\n")
            print(messageText + "\n")
        outputFile.close()
        sys.exit()

discordClient.run(API_TOKEN)
