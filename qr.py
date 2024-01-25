import discord
from discord.ext import commands
import qrcode

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(help="Generate a QR code for the provided URL.")
async def qr(ctx, url):
    """
    Generate a QR code for the provided URL.
    !qr <URL>
    Parameters:
    !qr <url>: The URL for which the QR code will be generated.
    """
    # Delete the user's command message
    await ctx.message.delete()

    # Generate QR code
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=25,
        border=0,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img_path = f'qr_code_{ctx.message.id}.png'
    img.save(img_path)

    # Send the QR code image to the Discord channel
    await ctx.send(file=discord.File(img_path))

    # Remove the saved image file
    import os
    os.remove(img_path)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')

# Close the bot properly when exiting the script
async def close_bot():
    await bot.close()

# You can call the close_bot() function whenever you want to close the bot, for example, at the end of your script.
