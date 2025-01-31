from rest_framework import response, request
from .models import User, Quiz
from rest_framework.decorators import api_view
from rest_framework import viewsets
from core.serializers import UserSerializer, QuizSerializer

@api_view(['GET'])
def welcome(request):
    return response.Response({'message': 'Welcome to MLB API!'})

@api_view(['GET'])
def generate_quiz(request):
    return response.Response({'message': 'Quiz generated!'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer