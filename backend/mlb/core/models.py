from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    user_performance = models.IntegerField(default=0)
    favourite_team = models.CharField(max_length=50)
    favourite_player = models.CharField(max_length=50)

    # Remove these redundant fields (already in AbstractUser)
    # username, email, and password are inherited

    # Add unique email constraint
    email = models.EmailField(unique=True)

    # Explicitly specify USERNAME_FIELD and REQUIRED_FIELDS
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, to_field='username')
    topic_name = models.CharField(max_length=50)
    difficulty_level = models.IntegerField()
    correct_answer = models.IntegerField()
    total_questions = models.IntegerField()

