from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    user_performance  = models.IntegerField(default=0)
    favourite_team = models.CharField(max_length=50, default='Null')
    favourite_player = models.CharField(max_length=50, default='Null')

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id')
    topic_name = models.CharField(max_length=50)
    difficulty_level = models.CharField(max_length=25)
    correct_answer = models.IntegerField()
    total_questions = models.IntegerField()

