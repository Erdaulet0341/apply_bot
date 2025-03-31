from telegram import Update
from telegram.ext import CallbackContext

from bottools.helpers.states import HOME, COUNTRY
from bottools.helpers.utils import log, is_valid_phone
from bottools.menu import country_menu
from bottools.helpers.translations import translations


def country_handler(update: Update, context: CallbackContext) -> int:
    language = context.user_data.get('language', 'kaz')
    phone_number = update.message.text
    if not is_valid_phone(phone_number):
        update.message.reply_text(translations['enter_valid_phone_number'][language])
        return COUNTRY

    context.user_data['phone_number'] = phone_number
    chat_id = update.message.chat_id

    log(f"country_handler: chat_id = {chat_id}, phone_number = {phone_number}")

    country_menu(update, context)
    return HOME

