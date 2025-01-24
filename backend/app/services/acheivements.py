from sqlalchemy.orm import Session
from app.models import User, Achievement, UserAchievement

ACHIEVEMENT_CACHE = {}

def load_achievements(db: Session):
    """Cache achievements for faster processing"""
    global ACHIEVEMENT_CACHE
    ACHIEVEMENT_CACHE = {a.id: a for a in db.query(Achievement).all()}

def check_achievements(db: Session, user: User):
    new_achievements = []
    
    # Get all possible achievements
    for achievement in ACHIEVEMENT_CACHE.values():
        if not has_achievement(db, user, achievement.id):
            if meets_criteria(user, achievement):
                grant_achievement(db, user, achievement)
                new_achievements.append(achievement)
    
    return new_achievements

def has_achievement(db: Session, user: User, achievement_id: int):
    return db.query(UserAchievement).filter_by(
        user_id=user.id,
        achievement_id=achievement_id
    ).first() is not None

def meets_criteria(user: User, achievement: Achievement):
    if achievement.criteria_type == "quiz_count":
        return user.total_quizzes >= achievement.threshold
    elif achievement.criteria_type == "xp":
        return user.xp >= achievement.threshold
    elif achievement.criteria_type == "perfect_score":
        return user.perfect_scores >= achievement.threshold
    return False

def grant_achievement(db: Session, user: User, achievement: Achievement):
    user_achievement = UserAchievement(
        user_id=user.id,
        achievement_id=achievement.id
    )
    db.add(user_achievement)
    db.commit()