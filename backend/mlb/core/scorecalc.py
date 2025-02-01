from .models import User, Quiz

def calculate_user_performace(user_id):
    user_id = user_id

    quiz_data = Quiz.objects.values('correct_answer', 'total_questions').filter(user_id = user_id)
    average_performance = 0
    total_correct_answers = 0
    total_questions = 0
    for quiz in quiz_data:
        total_correct_answers += quiz['correct_answer']
        total_questions += quiz['total_questions']

    if total_questions > 0:
        average_performance = (total_correct_answers / total_questions) * 100

    user = User.objects.get(user_id=user_id)
    user.user_performance = average_performance
    user.save()
