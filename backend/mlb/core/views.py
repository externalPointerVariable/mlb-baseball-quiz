from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User, Quiz
from .serializers import UserSerializer, QuizSerializer, UserProfileSerializer, LeaderboardSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'user_id': serializer.data['user_id']}, status=status.HTTP_201_CREATED, headers=headers)

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.user_id,
                'email': user.email
            })
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class TeamListView(APIView):
    def get(self, request):
        teams = ["Team A", "Team B", "Team C"]  # Add actual team names
        return Response(teams)

class QuizSubmissionView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer

    def perform_create(self, serializer):
        quiz = serializer.save(user_id=self.request.user, total_questions=10)
        user = self.request.user
        user.user_performance += quiz.correct_answer
        user.save()

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

class LeaderboardView(generics.ListAPIView):
    serializer_class = LeaderboardSerializer
    queryset = User.objects.all().order_by('-user_performance')