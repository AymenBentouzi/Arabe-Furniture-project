from django.shortcuts import render, redirect
from users.forms import UserRegisterForm
from django.contrib.auth import login, logout,  authenticate
from django.contrib import messages
from django.conf import settings 
from users.models import User


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('core:index')
    else:
        form = UserRegisterForm()
    return render(request, 'users/sign-up.html', {'form': form})
   
def login_view(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.warning(request, f"User with email {email} does not exist.") 
            return render(request, "users/sign-in.html")

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in.")
            return redirect("core:index")
        else:
            messages.warning(request, "Invalid email or password, please try again.")
            
    return render(request, "users/sign-in.html")



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("users:sign-out")
