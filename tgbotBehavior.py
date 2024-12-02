import logging
from html import escape
from uuid import uuid4
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, InlineQueryHandler
import config
import ipinfo
import ipsearch

# Enable logging

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

# set higher logging level for httpx to avoid all GET and POST requests being logged

logging.getLogger("httpx").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)



# Define a few command handlers. These usually take the two arguments update and

# context.

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /start is issued."""

    await update.message.reply_text("Hi!")



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Send a message when the command /help is issued."""

    await update.message.reply_text("Help!")



async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Handle the inline query. This is run when you type: @botusername <query>"""

    query = update.inline_query.query


    if not query:  # empty query should not be handled

        return

    revc=ipsearch.do_req(query),
    results = [

        InlineQueryResultArticle(

            id=str(uuid4()),

            title="IPSearch",
            
            input_message_content=InputTextMessageContent(str(revc)),

        ),

    ]


    await update.inline_query.answer(results)



def main() -> None:

    """Run the bot."""

    # Create the Application and pass it your bot's token.

    application = Application.builder().token(config.bot_token).build()


    # on different commands - answer in Telegram

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CommandHandler("help", help_command))


    # on inline queries - show corresponding inline results

    application.add_handler(InlineQueryHandler(inline_query))


    # Run the bot until the user presses Ctrl-C

    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":

    main()