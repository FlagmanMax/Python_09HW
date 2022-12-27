from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime 
from spy import *

async def command_hi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Good day {update.effective_user.first_name}!')
    
async def command_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')
    
async def command_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
    
async def command_sum(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    lst = msg.split() #/sum a b
    a = int(lst[1])
    b = int(lst[2])
    print(msg)
    await update.message.reply_text(f'{a} + {b} = {a+b}')