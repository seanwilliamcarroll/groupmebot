from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseNotFound
from types import *
import datetime

import bot

def index(request):
  if request.method == 'POST':
    # Find most recent message and send it back
    data = request.body
    print data
    print type(data)
    try:
      data = eval(data)
    except:
      print "Eval failed"
      return HttpResponseNotFound("Bad")
    if 1==1:#is_valid_v3_message(data):
      if data['sender_type'] == 'user':
        bot.send_message("User {} sent: {}".format(data['name'],data['text']))
        return HttpResponse("OK")
      else:
        return HttpResponse("OK")
    return HttpResponseNotFound(str(data))
  elif request.method == 'GET':
    return HttpResponse("Hello, world. You're at my_bot's index. Git update")
  else:
    return HttpResponseNotFound("Bad request")

def message(request):
  message = datetime.datetime.now()
  message = message.strftime("%A %B %d %Y %I:%M%p")
  bot.send_message(message)
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


