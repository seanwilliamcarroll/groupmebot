from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseNotFound
import datetime
import json
import os

import bot

def index(request):
  return HttpResponse("Pay no attention to the man behind the curtain2")

def parrot(request):
  if request.method == 'POST':
    # Find most recent message and send it back
    data = request.body
    try:
      data = json.loads(data)
    except:
      return HttpResponseNotFound("Bad message")
    if is_valid_v3_message(data):
      if data['sender_type'] == 'user':
        # Only want to parrot user's messages, else infinite loop
        if data['text'] == '!ParrotBot':
          os.environ['PARROT_BOT_ON'] = not os.environ['PARROT_BOT_ON']
        if os.environ['PARROT_BOT_ON']:
          bot.send_message('PARROT_BOT', "{}".format(data['text']))
        return HttpResponse("OK")
      else:
        return HttpResponse("OK")
    return HttpResponseNotFound("Invalid Groupme Message")
  elif request.method == 'GET':
    return HttpResponse("Hello, world. You're at parrot_bot's index.")
  else:
    return HttpResponseNotFound("Bad request")

def hello(request):
  if request.method == 'POST':
    # Make sure it is a valid message
    data = request.body
    try:
      data = json.loads(data)
    except:
      return HttpResponseNotFound("Bad message")
    if is_valid_v3_message(data):
      if data['sender_type'] == 'user':
        # Check if message contains 'hello' anywhere
        if data['text'].lower().find("hello") >= 0:
          bot.send_message('HELLO_BOT' , "Hello {}!".format(data['name']))
      return HttpResponse("OK")
  elif request.method == 'GET':
    return HttpResponse("Hello there!")
  return HttpResponseNotFound("Bad request")

def message(request):
  message = datetime.datetime.now()
  message = message.strftime("%A %B %d %Y %I:%M%p")
  bot.send_message('HELLO_BOT',message)
  return HttpResponse("Message sent: %s" % message)

# Helper to determine is a message is a valid v3 message
def is_valid_v3_message(data):
  return \
     "attachments" in data and \
     "avatar_url"  in data and \
     "created_at"  in data and \
     "group_id"    in data and \
     "id"          in data and \
     "name"        in data and \
     "sender_id"   in data and \
     "sender_type" in data and \
     "source_guid" in data and \
     "system"      in data and \
     "text"        in data and \
     "user_id"     in data


