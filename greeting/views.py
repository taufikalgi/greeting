from django.shortcuts import render, redirect

import datetime, time

def index(request):

  now = datetime.datetime.now()
  morning_start = now.replace(hour = 0, minute=0, second=0)
  noon_start = now.replace(hour = 11, minute=0, second=0)
  afternoon_start = now.replace(hour = 16, minute=0, second=0)
  night_start = now.replace(hour = 19, minute=0, second=0)

  now_print = time.strftime('%H:%M:%S')

  if (now < noon_start):
    word = 'Good Morning, Monkey!'
  elif (now < afternoon_start):
    word = 'Good Afternoon, Monkey!'
  elif (now < night_start):
    word = 'Good Afternoon, Monkey!'
  else:
    word = 'Good Evening, Monkey!'

  context = {
    'greeting_word': word,
    'now': now.time(),
    'now_print': now_print
  }

  return render(request, 'greeting/index.html', context)
