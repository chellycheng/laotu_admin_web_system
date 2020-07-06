from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm
# Create your views here.

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html')
    
def boards(request):
    boards = Board.objects.all()
    return render(request, 'boards.html', {'boards': boards})

def board_topics(request, bid):
    try:
        board = get_object_or_404(Board, pk=bid)
    except:
        raise Http404
    return render(request, 'topics.html', {'board': board, 'topics': board.topics.all() })

def new_post(request, pk):
    board = get_object_or_404(Board, pk=pk) # get the current boards
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'form': form})