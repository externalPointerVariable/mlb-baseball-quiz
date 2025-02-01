from .models import User, Quiz

def calculate_user_performace(username):
    username = username

    quiz_data = Quiz.objects.values('corrext_answer', 'total_questions').filter(username = username)
    avearage_performace = 0
    total_correct_answers = 0
    total_questions = 0
    for quiz in quiz_data:
        total_correct_answers += quiz['correct_answer']
        total_questions += quiz['total_questions']
    
    if total_questions > 0:
        average_performance = (total_correct_answers / total_questions) * 100

    user = User.objects.get(username=username)
    user.user_performance = average_performance
    user.save()
