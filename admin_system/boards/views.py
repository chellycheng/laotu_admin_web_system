from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Board, Topic
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, bid):
    try:
        board = get_object_or_404(Board, pk=bid)
    except:
        raise Http404
    return render(request, 'topics.html', {'board': board})