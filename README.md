# discord-bot
This repository contains information on how to quickly set up a functional bot in Discord using the python API. 

## Uses
Bots in Discord can track miscellaneous junk you don't want to, handle responses to events, and just generally automate out tedious tasks. I personally set my first bot up when I wanted to track information for a tabletop game I GM for. 

## This Guide
This guide will assume the user has a Discord, but not much experience outside of using it. By the end of this you should have a functional bot that can perform a few basic commands, respond to events, and save information received from users to a local drive or the cloud. Expanding from there is up to you.

### (1) The Developer Portal
First, head on over to the [Discord Developer Portal](https://discord.com/developers/applications) and create an account. Afterwards, you should see something like the below:

![Developer_Portal](https://github.com/Cromab/discord-bot/assets/145014565/2621daa5-c712-4f36-8137-bcb4abc6c59a)

Next, lets go ahead and click on New Application. We'll name our bot "my_bot" and accept the terms of service. You should see something like the below:

![image](https://github.com/Cromab/discord-bot/assets/145014565/e37f171f-cd2e-4447-b402-9a71c9e60881)

Feel free to add a description or change the name of your new bot. We still have a few steps to go before we can really use it, though. Click on over to OAuth2 and the URL Generator.

![image](https://github.com/Cromab/discord-bot/assets/145014565/f8769878-977f-405a-9650-17b12df44dc4)

We have to select some scopes for our bot, and the obvious choice is bot. Additionally, we'll need to set up the permissions for our bot. We're going to go ahead and give ours administrator privileges. Best practice is to only give your bot what it needs to operate, but this is good enough for this guide.

![OAuth2_Generator](https://github.com/Cromab/discord-bot/assets/145014565/ab62df21-dedb-4a0b-b613-dfe246859513)

Click "Copy" by the Generated URL and go ahead and paste it into your browser. You should be redirected to something like the below:

![Bot_URL](https://github.com/Cromab/discord-bot/assets/145014565/10441341-5810-4362-8d25-7532149df267)

Go ahead and select the server you want to add this bot to and continue. You'll be redirected to that server and you should see the bot in your server. Congratulations! You have added a bot to your Discord server.

Next we're going to talk about setting up our bot, making sure it's ready, and checking if it's online.

### (2) Build-a-Bot
The first step to building our bot is to install the discord.py using pip.
```shell
pip install -U discord.py 
```

This package allows us to interact with Discord API and has many applications beyond what we'll be outlining and can be found [here](https://discordpy.readthedocs.io/en/stable/). If you're interested in building out some awesome tools, please go ahead and read those docs.

For us, we're going to be focusing on just the basics. With that, let's start by creating our bot.py script. Here we'll start with the imports we need and the all important .env file.

```python
import os
import discord
from dotenv import load_dotenv
```
