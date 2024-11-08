import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import filters  # Correct import for filters

# Function to format the reply based on user input
def format_reply(user_message):
    lines = user_message.splitlines()
    if not lines or len(lines) < 1:
        return "Please send a valid message."

    episode_number = lines[0].strip()
    links = [line.strip() for line in lines[1:] if line.strip()]

    # Create HTML formatted reply
    reply = f'<h3 class="episode-title">Episode {episode_number}</h3>n'
    reply += '    <div class="download-box" id="download1" style="display: none;">n'
    reply += '        <p>WATCH/DOWNLOAD:</p>n'

    for index, link in enumerate(links):
        resolution = "480p" if index == 0 else "720p" if index == 1 else "1080p"
        reply += f'        <a class="resolution-button" href="{link}">{resolution}</a>n'

    reply += '    </div>'
    return reply

# Function to handle incoming messages
async def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    reply_message = format_reply(user_message)
    await update.message.reply_text(reply_message, parse_mode='HTML')

async def main():
    # Replace 'YOUR_TOKEN_HERE' with your bot's API token
    app = ApplicationBuilder().token("7204165447:AAGPA6vxvB8sDDZveuHWf53NGb378aepgN8").build()

    # Handle text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if str(e) == "This event loop is already running":
               # If the event loop is already running, we can directly await main()
            asyncio.get_event_loop().run_until_complete(main())
        else:
            raise
   
