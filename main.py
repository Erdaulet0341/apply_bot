from telegram import BotCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

from bottools.handlers.country import country_handler
from bottools.handlers.home import home_handler
from bottools.handlers.phone_number import phone_number_handler
from bottools.handlers.language import language_handler
from bottools.handlers.ai_assistant import ai_assistant_handler
from bottools.helpers.states import LANGUAGE, PHONE_NUMBER, HOME, COUNTRY, AI_ASSISTANT
from bottools.command import start, help_bot, cancel
from bottools.helpers.utils import get_env

updater = Updater(get_env('TG_BOT_TOKEN'), use_context=True)


def main() -> None:
    """
    Start the bot.
    Method to start the bot and add handlers to the dispatcher.
    """

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PHONE_NUMBER: [MessageHandler(Filters.all & ~Filters.command, phone_number_handler)],
            COUNTRY: [MessageHandler(Filters.all & ~Filters.command, country_handler)],
            HOME: [MessageHandler(Filters.all & ~Filters.command, home_handler)],
            LANGUAGE: [MessageHandler(Filters.text & ~Filters.command, language_handler)],
            AI_ASSISTANT: [MessageHandler(Filters.all & ~Filters.command, ai_assistant_handler)]
        },
        fallbacks=[CommandHandler('start', start)]

    )
    dispatcher.add_handler(CommandHandler("help", help_bot))
    dispatcher.add_handler(CommandHandler("cancel", cancel))

    commands = [
        BotCommand("start", "/start"),
        BotCommand("help", "/help"),
        BotCommand("cancel", "/cancel")
    ]
    updater.bot.set_my_commands(commands)

    dispatcher.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
    print('Bot is running')
