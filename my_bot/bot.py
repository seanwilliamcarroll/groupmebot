#!/usr/bin/env python

# Attempt at building a groupme bot

import requests


def send_message(message, bot):
  try:
    import config
    group = config.group
    bot_id = config.bot_id
  except:
    import gen_config
    group = gen_config.group
    bot_id = gen_config.bot_id
  # Helper function to send a message
  payload = {'bot_id':bot, 'text':message}
  r = requests.post("https://api.groupme.com/v3/bots/post", data=payload)
  # print r.status_code
  return r.text

def parrot():
  # Request last message sent in specific group
  # Parse message, send back same message
  pass
