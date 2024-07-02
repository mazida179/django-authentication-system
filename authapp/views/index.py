from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import views as v
from datetime import datetime


def index(req):
    # now = datetime.time(datetime.now())
    now = datetime.now()
    print(now.strftime('%X'))
    print(req.user)
    return render(req, 'authapp/public/index.html')

