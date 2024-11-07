   from telegram import Update
   from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

   # Function to format the reply based on user input
   def format_reply(user_message):
       lines = user_message.splitlines()
       if not lines or len(lines) < 1:
           return "Please send a valid message."

       episode_number = lines[0].strip()
       links = [line.strip() for line in lines[1:] if line.strip()]

       # Create HTML formatted reply
       reply = f'<h3 class="episode-title">Episode {episode_number} </h3>n'
       reply += '    </div>n'
       reply += '    <div class="download-box" id="download1" style="display: none;">n'
       reply += '        <p>WATCH/DOWNLOAD:</p>n'

       for index, link in enumerate(links):
           resolution = "480p" if index == 0 else "720p" if index == 1 else "1080p"
           reply += f'        <a class="resolution-button" href="{link}">{resolution}</a>n'

       reply += '    </div>'
       return reply

   # Function to handle incoming messages
   def handle_message(update: Update, context: CallbackContext):
       user_message = update.message.text
       reply_message = format_reply(user_message)
       update.message.reply_text(reply_message, parse_mode='HTML')

   def main():
       # Replace 'YOUR_TOKEN_HERE' with your bot's API token
       updater = Updater("YOUR_TOKEN_HERE")

       # Get the dispatcher to register handlers
       dp = updater.dispatcher

       # Handle text messages
       dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

       # Start the Bot
       updater.start_polling()

       # Run the bot until you press Ctrl-C
       updater.idle()

   if __name__ == '__main__':
       main()
   
