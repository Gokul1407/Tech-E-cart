from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth,messages










def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username alreadyy taken.')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email already taken.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request,'Registration successful, You can now login.')
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')       
        else:
            message1='user not found'
            return render(request,'login.html',{'message1':message1}) 

    else:
        return render(request,'login.html')


 
def custom_logout(request):
    auth.logout(request)
    return redirect("/")                  


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the POST data
        if User.objects.filter(email=email).exists():
            messages.error(request, 'An email has been sent with instructions to reset your password.')   
            return redirect('login')  # Replace 'login' with the actual URL name for the login page
        else:
            messages.error(request, 'Account does not exist')   
            return redirect('login')  # Replace 'login' with the actual URL name for the login page

    return render(request, 'forgot_password.html')