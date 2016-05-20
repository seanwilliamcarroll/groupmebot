from django.shortcuts import render
from django.http      import HttpResponse, HttpResponseNotFound
import bot
import datetime


def index(request):
  if request.method == 'POST':
    return HttpResponse(request.body)
  elif request.method == 'GET':
    return HttpResponse("Body: %d" % len(request.body))
    #return HttpResponse("Hello, world. You're at my_bot's index. Git update")
  else:
    return HttpResponseNotFound("Bad request")

def message(request):
  message = datetime.datetime.now()
  message = message.strftime("%A %B %d %Y %I:%M%p")
  bot.send_message(message)
  return HttpResponse("Message sent: %s" % message)
