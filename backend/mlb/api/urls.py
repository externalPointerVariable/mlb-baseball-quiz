from django.urls import include, path
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'quiz', views.QuizViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('question/', views.generate_quiz_api),
    path('login/', views.user_login),
    path('leaderboard/', views.getLeaderboard),
    path('profile/', views.get_user_profile),
    path('leagues/', views.baseball_leagues),
    path('teams/', views.baseball_teams),
    path('players/', views.baseball_players),
    path('csrf/', views.get_csrf_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]