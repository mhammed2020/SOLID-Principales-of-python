from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse  
  
def hello(request):  

    return render(request,'myapp/hello.html',{})  

def index(request):  

    return render(request,'myapp/index.html',{})  