from django.shortcuts import render

# Create your views here.
  
def hello(request):  
    context = {'title' : 'Python basics',
    
    'body' : 'the first tuto'}
   
    return render(request,'myapp/hello.html',context)  
   

def index(request):  
    context = {'title' : 'java basics',
    
    'body' : 'the second tuto'}

    return render(request,'myapp/index.html',context)  