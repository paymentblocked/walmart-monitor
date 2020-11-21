import requests
import asyncio
import discord

TOKEN = ('YourTokenHere')

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!monitor'):
        embed = discord.Embed(title="Please send the Walmart link you would like to monitor.", color=0x0071ce, description="**Example**: https://www.walmart.com/ip/Nintendo-Switch-Console-with-Neon-Blue-Red-Joy-Con/709776123.")
        embed.set_thumbnail(url="https://cdn.corporate.walmart.com/dims4/WMT/c2bbbe9/2147483647/strip/true/crop/2389x930+0+0/resize/1446x563!/quality/90/?url=https%3A%2F%2Fcdn.corporate.walmart.com%2Fd6%2Fe7%2F48e91bac4a8ca8f22985b3682370%2Fwalmart-logos-lockupwtag-horiz-blu-rgb.png")
        await message.channel.send(embed=embed)
        
        # Get link from user

    if message.content.startswith('https://www.walmart.com'):
        embed = discord.Embed(title="**Monitor starting.**", color=0x0071ce, description="Checking for stock...")
        embed.set_author(name="Walmart Monitor", url="https://www.walmart.com", icon_url="https://www.bocaratontribune.com/wp-content/uploads/2020/06/walmart-logo-300x300.jpg")
        embed.set_thumbnail(url="https://cdn.corporate.walmart.com/dims4/WMT/c2bbbe9/2147483647/strip/true/crop/2389x930+0+0/resize/1446x563!/quality/90/?url=https%3A%2F%2Fcdn.corporate.walmart.com%2Fd6%2Fe7%2F48e91bac4a8ca8f22985b3682370%2Fwalmart-logos-lockupwtag-horiz-blu-rgb.png")
        await message.channel.send(embed=embed)
        print("Monitoring started, checking for stock.")

        link = message.content
        
        # Check for stock

        def checkStock():
        stock = requests.get(link).text.count('Add to cart')
        
        # If stock detected, send message to discord.

        if stock == 1:
            embed = discord.Embed(title="**Restock Detected!**", color=0x0071ce, description="Link: " + link)
            embed.set_author(name="Walmart Monitor", url="https://www.walmart.com", icon_url="https://www.bocaratontribune.com/wp-content/uploads/2020/06/walmart-logo-300x300.jpg")
            embed.set_thumbnail(url="https://cdn.corporate.walmart.com/dims4/WMT/c2bbbe9/2147483647/strip/true/crop/2389x930+0+0/resize/1446x563!/quality/90/?url=https%3A%2F%2Fcdn.corporate.walmart.com%2Fd6%2Fe7%2F48e91bac4a8ca8f22985b3682370%2Fwalmart-logos-lockupwtag-horiz-blu-rgb.png")
            await message.channel.send(embed=embed)
            print("Restock detected, successfully sent to Discord.")
            
         # If no stock is detected, do not send message to discord. Continue to monitor for stock using asyncio.sleep

        while stock == 0:
            print("No stock detected. Monitoring for restock...")
            checkStock()
            await asyncio.sleep(30)

client.run(TOKEN)
