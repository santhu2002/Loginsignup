from django.shortcuts import render,redirect
from django.contrib.auth.models import User ,auth
from django.contrib import messages
# Create your views here.
def nav(request):
    return render(request,'Nav.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/login')
    return render(request,'Login.html')

def signup(request):
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if(User.objects.filter(username=name).exists() or User.objects.filter(email=email).exists() ):
            print("user already exist")
            messages.info(request,"User Already Exist")
            return redirect('/signup')
        else:
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
            print('user created')
            return redirect('/login')
            # messages.info(request,"User Created")
        return redirect('/')
    else:
        return render(request,'Signup.html')