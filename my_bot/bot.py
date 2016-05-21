#!/usr/bin/env python

# Attempt at building a groupme bot

import requests
import os

def send_message(bot_id, message):
  try:
    bot_id = os.environ[bot_id]
  except:
    pass
  # Helper function to send a message
  payload = {'bot_id':bot_id, 'text':message}
  r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)
  # print r.status_code
  return r.text

def parrot():
  # Request last message sent in specific group
  # Parse message, send back same message
  pass
