from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.

def home(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def register(request):
    return render(request, 'register.html')

def register(request):
    return render(request, 'register.html')