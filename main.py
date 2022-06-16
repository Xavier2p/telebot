import key
from telegram.ext import *

TOKEN = key.TOKEN 


updater = Updater(TOKEN, use_context=True)

def start(update, context):
    update.message.reply_text("""
Telebot42: a bot of testing!
Commands:
-/start: to view this message.
-/echo: to display your message.
Enjoy!
    """)

def echo(update, context):
    update.message.reply_text(update.message.text)

def error(update, context):
    update.message.reply_text("Error! Unkown command '", update.message.text, "'")

def main():
    print("[OK] - updater created")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    print("[OK] - commands initialized")
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("echo", echo))

    print("[OK] - error mode enable")
    dp.add_handler(MessageHandler(Filters.text, error))

    print("[OK] - bot launched")
    updater.start_polling()

    print("[OK] - bot stopped")
    updater.idle()


if __name__ == '__main__':
    main()
