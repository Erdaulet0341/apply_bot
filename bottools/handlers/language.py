from telegram import ReplyKeyboardRemove
from telegram import Update
from telegram.ext import CallbackContext

from bottools.helpers.translations import translations
from bottools.helpers.states import PHONE_NUMBER, LANGUAGE
from bottools.helpers.utils import log


def language_handler(update: Update, context: CallbackContext) -> int:
    language = context.user_data.get('language', 'kaz')
    user_language = update.message.text
    log(f"language_handler, chat_id = {update.message.chat_id}, user_feedback = {user_language}")

    if user_language == '🇰🇿Қазақша':
        context.user_data['language'] = 'kaz'
        language = 'kaz'
        update.message.reply_text(translations['welcome'][language],
                                  reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(translations['enter_your_fullname'][language])

        return PHONE_NUMBER
    elif user_language == '🇷🇺Русский':
        context.user_data['language'] = 'rus'
        language = 'rus'
        update.message.reply_text(translations['welcome'][language],
                                  reply_markup=ReplyKeyboardRemove())
        update.message.reply_text(translations['enter_your_fullname'][language])
        return PHONE_NUMBER

    else:
        update.message.reply_text(translations['choose_valid_language'][language])
        return LANGUAGE
