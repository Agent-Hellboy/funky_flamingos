from urllib.parse import parse_qs
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from users.forms import RegistrationForm
from django.contrib import messages, auth
from django.conf import settings
import requests


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

    return render(request, 'users/register.html', {'form': form, 'client_id': settings.CLIENT_ID })


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
    # result now has the access token
    return HttpResponse(str(result))


def dashboard(request):
    return render(request, 'users/dashboard.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been logged out')
    return render(request, 'users/logout.html')
