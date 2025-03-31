from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from bottools.helpers.translations import translations
from bottools.integrations.gpt_connector import GPTConnector
from bottools.helpers.utils import get_env, log
from bottools.helpers.states import AI_ASSISTANT



def ai_assistant_handler(update: Update, context: CallbackContext):
    """
    AI assistant handler.
    Method for processing messages from the user and sending them to the OpenAI API.
    """
    language = context.user_data.get('language', 'kaz')
    text = update.message.text

    if text == translations['understand'][language]:
        update.message.reply_text(translations['thanks_please_wait_answer'][language],
                                  reply_markup=ReplyKeyboardRemove())
        return  # If the user does not want to ask a question, the conversation ends

    connector = GPTConnector()
    assistant_id = get_env('ASSISTANT_ID')
    openai_thread = context.user_data.get('openai_thread')
    if not openai_thread:
        openai_thread = connector.create_thread()  # Create a new thread for the user
        context.user_data['openai_thread'] = openai_thread

    is_connected = context.user_data.get('is_connected', False)  # Check if the user is connected to the assistant
    if not is_connected:
        update.message.reply_text(translations['ready_ask_any_questions'][language],
                                  reply_markup=ReplyKeyboardRemove())
        context.user_data['is_connected'] = True
        return AI_ASSISTANT

    update.message.reply_chat_action(action="typing")  # Show typing status to the user

    answer = connector.process_message(
        thread_id=openai_thread,
        assistant_id=assistant_id,
        content=text
    )

    if not answer:
        update.message.reply_text(translations['error_occurred'][language])
        log(f"Error occurred while processing the message, thread_id = {openai_thread}")
        return AI_ASSISTANT  # If the answer is empty, the conversation continues

    update.message.reply_text(answer, reply_markup=ReplyKeyboardRemove())
    log(f"Message processed successfully, thread_id = {openai_thread}, answer = {answer}")
    return AI_ASSISTANT
