from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler

import config
from tgbotBehavior import start, other_command, myid

 

if __name__ == '__main__':  

    application = ApplicationBuilder().token(config.bot_token).build()  


    application.add_handler(CommandHandler('start', start))

    application.add_handler(CommandHandler('myid', myid)) 

    application.add_handler(MessageHandler((~filters.COMMAND), other_command))


    application.run_polling(allowed_updates=Update.ALL_TYPES)