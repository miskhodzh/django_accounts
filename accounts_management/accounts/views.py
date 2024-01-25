from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = 'accounts/index.html'
    return render(request, template)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:index'))
    else:
        form = AuthenticationForm()

    context = {'form': form}
    template = 'accounts/login.html'
    return render(request, template, context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
