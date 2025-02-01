from rest_framework import response, status, request
from .models import User, Quiz
from rest_framework.decorators import api_view
from rest_framework import viewsets
from core.serializers import UserSerializer, QuizSerializer
from core.quizGen import generate_quiz
from core.scorecalc import calculate_user_performace

@api_view(['GET'])
def welcome(request):
    return response.Response({'message': 'Welcome to MLB API!'})

@api_view(['GET'])
def getLeaderboard(request):
    users = User.objects.values('username','user_performance').order_by('-user_performance')
    return response.Response(users, status=status.HTTP_200_OK)


@api_view(['POST'])
def generate_quiz_api(request):
    topic  = request.data.get('topic')
    difficulty = request.data.get('difficulty')
    result = generate_quiz(topic, difficulty)
    return response.Response(result, status=status.HTTP_200_OK)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return response.Response({'error': 'Username and password required!'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username=username)
        if password == user.password:
            return response.Response({'message': 'Login successful!', 
                                      'user_id': user.user_id}, status=status.HTTP_200_OK)
        else:
            return response.Response({'error': 'Invalid password!'}, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return response.Response({'error': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.data.get('username')
            calculate_user_performace(username)
        return super().create(request, *args, **kwargs)