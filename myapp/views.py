from django.shortcuts import render
from myapp.form import StuForm  
from myapp.form import StudentForm  
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
    student = StudentForm()  
    return render(request,'myapp/index.html',{'form':stu,'form2':student})  