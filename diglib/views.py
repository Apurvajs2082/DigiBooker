from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from django.contrib import messages

def home(request):
    if request.method == "POST":
        emailid = request.POST['email']
        password = request.POST['password']
        print(User.objects.filter(email=emailid).exists())
        if User.objects.filter(email=emailid).exists():
            username = User.objects.get(email=emailid)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            else:
                messages.error(request, "Invalid Credentials")
                return render(request, 'home.html', {'title': 'Login'})
        else:
            messages.error(request, "User does not exist")
            return render(request, 'home.html', {'title': 'Login'})
    return render(request,"home.html")

def file(request):
    if request.user.is_authenticated:
        return render(request,"file.html")
    else:
        messages.error(request,"Please login first. ")
        return redirect(home)

def logout(request):
    auth.logout(request)
    messages.success(request,"Logged Out Successfully ")
    return redirect('/')