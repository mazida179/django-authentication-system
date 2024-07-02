from django.shortcuts import redirect, render
from django.http import request
from django.contrib.auth.models import User
from ..forms import *

def resigterUser(req):
    context = {}

    if req.method == 'POST':
        form = RegisterUser(req.POST)
        print('error =>',form['username'].errors)

        
        if form.is_valid():
            pass
            # form.save()
        else:
            context['errors'] = 'Some input data is invalid'
    
    form = RegisterUser(auto_id=False)
    context['form'] = form
    
    return render(req, 'authapp/auth/register-user.html', context)