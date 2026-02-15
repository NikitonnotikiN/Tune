#python 3.7.1

from telegram import Update, constants
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

WEB_APP_URL = '<https://nikitonnotikin.github.io/Tune/>'  # замените на фактический URL вашей залитой страницы

async def open_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
        f'<a href="{WEB_APP_URL}" data-webviewheight="full">Открыть мини-приложение</a>',
        parse_mode=constants.ParseMode.HTML,
        disable_web_page_preview=True
    )

def main():
    bot_token = '<8312314104:AAFGn3BU49S0sivS-QAwq84JOc-uvBgq59Y>'
    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("open", open_app))  # команда "/open" открывает приложение
    app.run_polling()

if __name__ == "__main__":
    main()
    