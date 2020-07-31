import json
from urllib.parse import parse_qs
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages, auth
from django.conf import settings
import requests
from users.forms import RegistrationForm


def index(request):
    return HttpResponse("<h1>welcome</h1>")


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are successfully registered')
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {
        'form': form,
        'client_id': settings.CLIENT_ID
    })


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user:
            auth.login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')
        messages.error(request, 'Invalid Credentials')
        return redirect('login')
    return render(request, 'users/login.html')


def github_login(request):
    # Get temporary GitHub code
    session_code = request.GET['code']
    r = requests.post('https://github.com/login/oauth/access_token', data={
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'code': session_code
    })
    result = parse_qs(r.content)
    # Note: there's no error handling here
    r = requests.get('https://api.github.com/user', headers={
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token ' + result[b"access_token"][0].decode('utf-8')
    })
    user = {
        "username": r.json()["login"],
        "email": r.json()["email"],
    }
    with open("user.json", "w") as f:
        json.dump(user, f)
    return HttpResponseRedirect('/users/dashboard')


def dashboard(request):
    return render(request, 'users/dashboard.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return render(request, 'users/logout.html')
