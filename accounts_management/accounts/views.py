from django.shortcuts import render, HttpResponseRedirect,redirect
from django.views import View
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




class Profile(View):
    template = 'accounts/profile.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            # Пользователь аутентифицирован, отображаем профиль
            return render(request, self.template)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))


class Login(View):
    template = 'accounts/login.html'

    def get(self, request):
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print('FORM IS VALIIIIIID')
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                print('FORM IS VALIIIIIID')
                login(request, user)
                return HttpResponseRedirect(reverse('accounts:index'))


class Registration(View):
    template = 'accounts/registration.html'

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form,
        }
        return render(request, self.template, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounts:login')
