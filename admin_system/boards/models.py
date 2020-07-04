from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, models.PROTECT,related_name='topics',)
    starter = models.ForeignKey(User, models.PROTECT,related_name='topics') 
    def __str__(self):
        return self.subject
    
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, models.PROTECT, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,models.PROTECT, related_name='posts')
    solved = models.BooleanField(default=False)
    def __str__(self):
        return self.message[0:min(len(message),10)]