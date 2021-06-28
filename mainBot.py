from telegram.ext import Updater
import logging
import helpers
from telegram.ext import MessageHandler, Filters
import environment

polling_handler = MessageHandler(Filters.text & (~Filters.command), helpers.polling_threading)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater = Updater(token=environment.bot_id, use_context=True)
updater.start_polling()
dispatcher = updater.dispatcher
dispatcher.add_handler(polling_handler)
