import os,my_module
from revChatGPT.V3 import Chatbot

chatbot = Chatbot(
    api_key = my_module.GPT_API_KEY,
    engine = "gpt-3.5-turbo",
    proxy = None,
    timeout = None,
    max_tokens = 3000,
    temperature = 0.5,
    top_p = 1.0,
    presence_penalty = 0.0,
    frequency_penalty = 0.0,
    reply_count = 1,
    truncate_limit = 2500,
    system_prompt = "You are ChatGPT, a large language model trained by OpenAI. Respond conversationally."
)

chatbot_file = 'chat/chatbot.json'
if os.path.isfile(chatbot_file):
    chatbot.load(file=chatbot_file)
