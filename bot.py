#!/usr/bin/env python

# Attempt at building a groupme bot

import requests
from bot_server import BotServer, BotServerRequestHandler

try:
  import config
  group = config.group
  bot_id = config.bot_id
except:
  import gen_config
  group = gen_config.group
  bot_id = gen_config.bot_id

def send_message(message, bot):
  # Helper function to send a message
  payload = {'bot_id':bot, 'text':message}
  print payload
  r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)
  print r.status_code

def parrot():
  # Request last message sent in specific group
  # Parse message, send back same message
  
  pass

def main():
  send_message('System test', bot_id)
  parrot()

main()
