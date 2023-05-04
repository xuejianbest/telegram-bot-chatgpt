from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import time,my_module
from my_module import tg_bot_whitelist
from key3 import chatbot

def chat(update: Update, context: CallbackContext) -> None:
    msg = update.message.text
    chat_id = update.message.chat_id
    from_user = update.message.from_user
    print(f'{from_user.first_name} ask {msg}')
    
    if from_user.id not in tg_bot_whitelist:
        return
    
    if msg is None:
        text = "只支持纯文本输入。"
        print(text)
        context.bot.send_message(chat_id=chat_id, text=text)
        return

    message = context.bot.send_message(chat_id=chat_id, text='waiting...')
    msg_id = message.message_id

    response_generator = chatbot.ask(prompt = msg)
    
    prev_text = ""
    for w in response_generator:
        text = w["message"]
        new_text = text[len(prev_text) :]
        print(new_text, end="", flush=True)
        prev_text = text
        
        if text.strip() == '':
            continue
        timestamp = int(time.time())
        if timestamp % 3 != 0:
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
    #chatbot.save(file = 'chat/chatbot3.json')

def main() -> None:
    MY_TOKEN = my_module.TG_BOT_TOKEN_1
    updater = Updater(MY_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(~Filters.command, chat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()