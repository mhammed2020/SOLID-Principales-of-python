from django.shortcuts import render
from myapp.form import StuForm  
# Create your views here.
  
def hello(request):  
    context = {'title' : 'Python basics',
    
    'body' : 'the first tuto'}
   
    return render(request,'myapp/hello.html',context)  
   

def index(request):  
    context = {'title' : 'java basics',
    
    'body' : 'the second tuto'}

    ##forms.py

    stu = StuForm()  

    return render(request,'myapp/index.html',{'form':stu})  