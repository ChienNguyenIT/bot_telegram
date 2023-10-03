from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
from getnew_vxvault import getnewvxvault
from getnew_blocklist import getnewblocklist
from getnew_bazar import getnewbazaar


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    title = getnewvxvault()
    for i in title:
        await update.message.reply_text(f'Tin mới: \n {i}')

async def news1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    title = getnewblocklist()
    for i in title:
        await update.message.reply_text(f'Tin mới: \n {i}\n')

async def news2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    title = getnewbazaar()
    for i in title:
        await update.message.reply_text(f'Tin mới: \n {i}\n')

app = ApplicationBuilder().token("5803094348:AAFk0qFOh64_ScGL3Oy1crF5wl11UyRLgHk").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("news1", news1))
app.add_handler(CommandHandler("news2", news2))

app.run_polling()


