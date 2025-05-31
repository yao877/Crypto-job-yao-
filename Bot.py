
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Récupération du token depuis les variables d'environnement
TOKEN = os.getenv("7478572277:AAG-V01yeqfkwgcy85oCcUfga8f2op_pMsE")

# Fonction qui gère la commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur le Bot Crypto Vote !")

# Création du bot
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Lancement du bot
app.run_polling()
