API_TOKEN: str = "Nzc3MDM3NzQ0NTA5NjgxNjY1.X69myg.rIJE625KrgjUxgfn7BuoezJsEuQ" # bot token
FILTER_TEXT: list = ["https", "is a level"] # a list of strings to match for message exclusion

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

outputFile: io.TextIOWrapper = open(outputDirPath + "/output.txt", "a")

@discordClient.event
async def on_message(message: discord.Message):
    if ("$historytest" in message.content):
        channel: discord.TextChannel = message.channel
        messageList: list = await channel.history(oldest_first=True).flatten()
        for currentMessage in messageList:
            messageText: str = currentMessage.content
            for keyword in FILTER_TEXT:
                if (keyword in messageText.lower()):
                    continue
            outputFile.write(messageText + "\n")
            print(messageText + "\n")
        outputFile.close()
        sys.exit()

discordClient.run(API_TOKEN)