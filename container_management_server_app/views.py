# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from tasks import *
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

@api_view(['POST'])
def login_user(request):
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Logged In")
    else:
        return HttpResponse("No Logged")

@login_required
def logout_user(request):
    logout(request)
    return HttpResponse("Logout Ok")

@login_required
@api_view(['POST'])
def inicio_tarea(request):

    archivo = request.data['file']
    resultado = up_file_start_task(archivo)
    return HttpResponse("su ide de job es : "+resultado.id)
