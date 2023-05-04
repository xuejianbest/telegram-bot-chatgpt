import os,my_module
from revChatGPT.V1 import Chatbot

config = {
  "access_token": my_module.GPT_ACCESS_TOKEN
}

chatbot = Chatbot(config=config)