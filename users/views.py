# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

# Create your views here.
from users.forms import LoginForm
from django.views.generic import View

class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            # no usarlo pq petaria si no existe -- username = request.POST['usr']
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'photos_home'))
                else:
                    error_messages.append('El usuario no está activo')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('photos_home')
