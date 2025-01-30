from django.urls import path
from core import views

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('login/', views.CustomObtainAuthToken.as_view(), name='login'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('quiz/submit/', views.QuizSubmissionView.as_view(), name='quiz-submit'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
]