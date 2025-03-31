from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from bottools.helpers.states import HOME, AI_ASSISTANT
from bottools.helpers.temp_database import add_client, is_client_exists, send_channel
from bottools.helpers.translations import translations
from bottools.menu import ai_assistant_menu
from bottools.helpers.utils import log


def home_handler(update: Update, context: CallbackContext):
    """
    Home handler.
    Method for processing messages from the user and adding a new client to the database.
    """

    language = context.user_data.get('language', 'kaz')
    country = update.message.text

    if country == translations['other_country'][language]:
        update.message.reply_text(translations['enter_your_country'][language], reply_markup=ReplyKeyboardRemove())
        return HOME  # If the user selects "Other country", the conversation continues

    fullname = context.user_data.get('fullname')
    phone_number = context.user_data.get('phone_number')
    username = context.user_data.get('username')
    telegram_id = update.message.chat_id

    if is_client_exists(phone_number):
        update.message.reply_text(translations['client_exists'][language], reply_markup=ReplyKeyboardRemove())
        return HOME  # If the client already exists, no need to add it to the database

    add_client(fullname, phone_number, country, username, telegram_id)  # Add a new client to the database
    send_channel(context, fullname, phone_number, country, username)  # Send a message to the channel
    log(f"Client added to the database, chat_id = {telegram_id}, phone_number = {phone_number}")

    ai_assistant_menu(update, context)  # Show the AI assistant menu
    return AI_ASSISTANT
