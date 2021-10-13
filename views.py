from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from .models import registration,Exam
from .forms import registrationForm
from django.db.models import Q
# Create your views here.


def reg(request):
    return render(request,'index.html')
def register(request):
    form=registrationForm()
    if request.method=='POST':
        form=registrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect('/')
    else:
        
        form=registrationForm()
        
    return render(request,'login.html',{"form":form})
def log(request):
    login_status=''

    if request.method=='POST':
        
       
        username=request.POST['username']
        password=request.POST['password']

        if username is not None and password is not None:
            login=registration.objects.filter(Q(email=username)& Q(password=password))
            if login:
                exam=Exam.objects.all()
                return  render(request,'home.html',{"exam":exam})
            else:
                login_status='Invalid username or password '
    return render(request,'login.html',{"login_status":login_status})

