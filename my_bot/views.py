from django.shortcuts import render
from django.http      import HttpResponse
import bot


def index(request):
  return HttpResponse("Hello, world. You're at my_bot's index. Git update")

def message(request):
  return HttpResponse(bot.send_message())
