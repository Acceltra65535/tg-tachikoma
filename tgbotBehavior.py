from telegram import Update  
from telegram.ext import ContextTypes  
import config  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):  

    pass

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"这是一个转存机器人")  


async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):  

    your_chat_id = update.effective_chat.id  

    await context.bot.send_message(chat_id=your_chat_id, text=f'你的 chat id 是 {your_chat_id}')  

 

async def other_command(update: Update, context: ContextTypes.DEFAULT_TYPE):  

    pass