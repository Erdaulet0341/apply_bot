from telegram import Update
from telegram.ext import CallbackContext

from bottools.helpers.translations import translations
from bottools.helpers.states import COUNTRY, PHONE_NUMBER
from bottools.helpers.utils import log, is_valid_fullname


def phone_number_handler(update: Update, context: CallbackContext) -> int:
    language = context.user_data.get('language', 'kaz')
    text = update.message.text
    if not is_valid_fullname(text):
        update.message.reply_text(translations['enter_valid_fullname'][language])
        return PHONE_NUMBER
    context.user_data['fullname'] = text

    log(f"phone_number_handler: chat_id = {update.message.chat_id}, fullname = {text}")

    update.message.reply_text(translations['enter_phone_number'][language])
    return COUNTRY
