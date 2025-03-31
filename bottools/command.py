from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler

from bottools.helpers.states import LANGUAGE, HOME
from bottools.menu import language_menu
from bottools.helpers.translations import translations, help_text_rus, help_text_kaz
from bottools.helpers.utils import log


def start(update: Update, context: CallbackContext) -> int:  # Handler for the /start command
    context.user_data['current_question'] = 0
    language = context.user_data.get('language', 'kaz')
    update.message.reply_text(translations['start_prompt'][language])

    if context.user_data.get('started', False):
        update.message.reply_text(translations['already_started'][language])
        return

    language_menu(update)
    context.user_data['started'] = True
    return LANGUAGE


def help_bot(update: Update, context: CallbackContext):  # Handler for the /help command`
    language = context.user_data.get('language', 'kaz')

    if language == 'rus':
        update.message.reply_text(help_text_rus)
    else:
        update.message.reply_text(help_text_kaz)


def cancel(update: Update, context: CallbackContext) -> int:  # Handler for the /cancel command
    log(f"Session ended, chat_id = {update.message.chat_id}")
    context.user_data['timer_stop'] = True
    language = context.user_data.get('language', 'kaz')

    update.message.reply_text(translations['cancel_message'][language], reply_markup=ReplyKeyboardRemove())
    context.user_data['started'] = False

    return ConversationHandler.END
