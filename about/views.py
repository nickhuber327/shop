from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'about/index.html')

def contact(request):
    return render(request, 'about/basic.html',{'content':['If you would like to contact me, please email me.','nickhuber327@gmail.com']})
