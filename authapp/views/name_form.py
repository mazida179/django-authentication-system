from django.shortcuts import render
from django.http import HttpResponse
from ..forms import *

def postName(req):

    if req.method == 'POST':
        form = MyForm(req.POST)


        if form.is_valid():
            name = form.cleaned_data['name']

            return render(req, 'authapp/public/name_form.html', {'form':form})
    else:    
        form = MyForm(label_suffix='')

    return render(req, 'authapp/public/name_form.html', {'form':form})