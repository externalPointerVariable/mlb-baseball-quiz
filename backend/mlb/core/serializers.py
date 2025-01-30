from rest_framework import serializers
from .models import User, Quiz
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'password', 'user_performance', 'favourite_team', 'favourite_player']
        read_only_fields = ['user_id', 'user_performance']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            favourite_team=validated_data.get('favourite_team', ''),
            favourite_player=validated_data.get('favourite_player', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['quiz_id', 'user_id', 'topic_name', 'difficulty_level', 'correct_answer', 'total_questions']
        read_only_fields = ['quiz_id', 'user_id', 'total_questions']

    def validate_correct_answer(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("Correct answers must be between 0 and 10.")
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'user_performance', 'favourite_team', 'favourite_player']
        read_only_fields = ['user_id', 'email', 'user_performance']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'user_performance']