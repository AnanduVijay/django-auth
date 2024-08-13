from django.shortcuts import render, redirect
from django.contrib.auth import (
    get_user_model, authenticate, login, logout
    )
from users.forms import UserCreationForm, LoginForm

User = get_user_model()

def home(request):
    return render(request, "home.html")

def signupView(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            print(user)
            login(request, user)
            return redirect("home")
        else:
            return render(request, "signup.html", {'form': form})       

def loginView(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            print("grgrrhgrhrhtrhtjhtjtjtjtjt")
            print(user)
        if user is not None:
            print("grgrrhgrhrhtrhtjhtjtjtjtjt")
            print(user)
            login(request, user)
            return redirect("home")
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form, "message": "Invalid username or password"})

def logoutView(request):
    logout(request)
    return redirect("login")