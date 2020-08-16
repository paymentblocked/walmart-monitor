import requests
import discord
TOKEN = ('Yourtokenhere')

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!start'):
        channel = message.channel
        await channel.send('Please send the Walmart link you would like to monitor.')

        def check(m):
            return m.author == message.author

        msg = await client.wait_for('message', check=check)
        await channel.send('Monitor starting.')

@client.event
async def on_message(message):
    if message.content.startswith('https://www.walmart.com'):
        channel = message.channel
        await channel.send('Checking for stock...')

        var = message.content

        stock = requests.get(var).text.count('Add to cart')
        if stock == 1:
            print("Restock detected, successfully sent to Discord.")

        if stock == 0:
            print("No stock detected. Monitoring for restock...")


client.run(TOKEN)
