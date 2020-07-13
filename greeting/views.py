from django.shortcuts import render, redirect

import datetime

def index(request):

  now = datetime.datetime.now()
  morning_start = now.replace(hour = 0, minute=0)
  noon_start = now.replace(hour = 11, minute=0)
  afternoon_start = now.replace(hour = 16, minute=0)
  night_start = now.replace(hour = 19, minute=0)

  if (now < noon_start):
    word = 'Selamat pagi'
  elif (now < afternoon_start):
    word = 'Selamat siang'
  elif (now < night_start):
    word = 'Selamat sore'
  else:
    word = 'Selamat malam'

  context = {
    'greeting_word': word
  }

  return render(request, 'greeting/index.html', context)
