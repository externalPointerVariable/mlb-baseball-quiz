from rest_framework import serializers
from .models import User, Quiz
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'email', 
            'password', 
            'user_performance', 
            'favourite_team', 
            'favourite_player'
        ]
        extra_kwargs = {'password': {'write_only': True}}

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quiz_id', 'username', 'topic_name', 'difficulty_level', 'correct_answer', 'total_questions']
        read_only_fields = ['quiz_id', 'username', 'total_questions']

    def validate_correct_answer(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("Correct answers must be between 0 and 10.")
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_performance', 'favourite_team', 'favourite_player']
        read_only_fields = ['id', 'email', 'user_performance']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'user_performance']