#!/usr/bin/env python

# Attempt at building a groupme bot

import requests
from bot_server import BotServer, BotServerRequestHandler

group  = 22000913
bot_id = 'c08d456b084bcd213f6052aeba'

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
