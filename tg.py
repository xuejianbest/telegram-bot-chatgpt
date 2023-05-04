from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import time,my_module
from key import chatbot



def chat(update: Update, context: CallbackContext) -> None:
    msg = update.message.text
    chat_id = update.message.chat_id
    from_user = update.message.from_user
    
    print(f'{from_user.first_name} ask {msg}')
    if msg is None:
        text = "只支持纯文本输入。"
        print(text)
        context.bot.send_message(chat_id=chat_id, text=text)
        return 

    message = context.bot.send_message(chat_id=chat_id, text='waiting...')
    msg_id = message.message_id

    response_generator = chatbot.ask_stream(prompt = msg, role = "user", convo_id = chat_id)

    text = ''
    for w in response_generator:
        print(w, end="", flush=True)
        text += w
        if w.strip() == '':
            continue
        timestamp = int(time.time())
        if timestamp % 4 != 0:
            continue
        escape_text = my_module.escape_string(text)
        try:
            context.bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text='md: ' + escape_text, parse_mode=ParseMode.MARKDOWN)
        except Exception as e:
            context.bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text='ex: ' + escape_text)
        time.sleep(0.8)
    escape_text = my_module.escape_string(text)
    try:
        context.bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text='doneM: ' + escape_text, parse_mode=ParseMode.MARKDOWN)
    except Exception as e:
        context.bot.edit_message_text(chat_id=chat_id, message_id=msg_id, text='doneE: ' + escape_text)

    print(f' to {update.message.from_user.first_name}')
    chatbot.save(file = 'chat/chatbot.json')

def main() -> None:
    MY_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    updater = Updater(MY_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(~Filters.command, chat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
