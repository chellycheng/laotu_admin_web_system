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

class Project(models.Model):
    name = models.TextField(max_length=400)
    description = models.TextField(max_length=4000)
    start_date =  models.DateTimeField(auto_now_add=True)
    end_date =  models.DateTimeField(auto_now_add=True)
    localtion = models.TextField(max_length=1000)
    price = models.IntegerField()
    discount_policy = models.TextField(max_length=4000)

class Event(models.Model):
    Project = models.ForeignKey(Project,models.PROTECT, related_name='events')
    name = models.TextField(max_length=400)
    notes = models.TextField(max_length=2000)
    start_date =  models.DateTimeField(auto_now_add=True)
    end_date =  models.DateTimeField(auto_now_add=True)
    localtion = models.TextField(max_length=1000)
    speaker = models.TextField(max_length=2000)

class Role(User):
    # Stuff
    SeniourStaff = "SS"
    JuniorStaff = "JS"
    # Spearker
    Speaker = "SK"

    LIST_OF_ROLES = (
        (SeniourStaff, 'SeniourStaff'),
        (JuniorStaff, 'JuniorStaff'),
        (Speaker , 'Speaker')
    )

    role = models.CharField(
        max_length=2,
        choices=LIST_OF_ROLES,
        default=JuniorStaff,
    )

    # person =  models.ForeignKey(User,models.PROTECT, related_name='roles')

class Info(models.Model):
    subject = models.TextField(max_length=400)
    descriptions = models.TextField(max_length=4000)
    