from django.shortcuts import render
from django.http      import HttpResponse
import bot
import datetime


def index(request):
  return HttpResponse("Hello, world. You're at my_bot's index. Git update")

def message(request):
  message = datetime.datetime.now()
  message = message.strftime("%A %B %d %Y %I:%M%p")
  bot.send_message(message)
  return HttpResponse("Message sent: %s" % message)
