from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from bottools.helpers.translations import translations


def language_menu(update: Update):
    keyboard = [
        ["🇰🇿Қазақша", "🇷🇺Русский"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        translations['choose_language']['kaz'],
        reply_markup=reply_markup
    )


def country_menu(update: Update, context: CallbackContext):
    language = context.user_data.get('language', 'kaz')
    context.user_data['update'] = update
    context.user_data['context'] = context

    keyboard = [
        [translations['usa'][language], translations['england'][language]],
        [translations['other_country'][language]],
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        translations['select_country'][language],
        reply_markup=reply_markup
    )


def ai_assistant_menu(update: Update, context: CallbackContext):
    language = context.user_data.get('language', 'kaz')
    context.user_data['update'] = update
    context.user_data['context'] = context

    keyboard = [
        [translations['understand'][language], translations['ask_from_assistant'][language]]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(
        translations['your_apply_complicated'][language],
        reply_markup=reply_markup
    )
