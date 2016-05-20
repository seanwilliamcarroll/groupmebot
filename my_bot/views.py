from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseNotFound
from types import *
import datetime

import bot

def index(request):
  if request.method == 'POST':
    # Find most recent message and send it back
    #if is_valid_v3_message(request) and request.POST["sender_type"] is "user":
    data = request.body
    data = eval(data)
    data = type(data)
    if 0 == 1:
      bot.send_message("User {} sent: {}".format(request.POST["name"],request.POST["text"]))
      return HttpResponse("OK")
    #bot.send_message("Error: %s" % request.body)
    return HttpResponseNotFound(data)
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
def is_valid_v3_message(request):
  return \
     "attachments" in request.POST and \
     "avatar_url"  in request.POST and \
     "created_at"  in request.POST and \
     "group_id"    in request.POST and \
     "id"          in request.POST and \
     "name"        in request.POST and \
     "sender_id"   in request.POST and \
     "sender_type" in request.POST and \
     "source_guid" in request.POST and \
     "system"      in request.POST and \
     "text"        in request.POST and \
     "user_id"     in request.POST


