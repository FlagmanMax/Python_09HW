from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import command_hi, command_time, command_help, command_sum


app = ApplicationBuilder().token("ABC").build()

app.add_handler(CommandHandler("hi", command_hi))
app.add_handler(CommandHandler("time", command_time))
app.add_handler(CommandHandler("help", command_help))
app.add_handler(CommandHandler("sum", command_sum))

print("Server started!")
app.run_polling()