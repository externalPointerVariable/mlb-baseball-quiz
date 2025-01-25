from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Achievement, UserAchievement

ACHIEVEMENT_CACHE = {}

async def load_achievements(db: AsyncSession):
    """Cache achievements using async query"""
    global ACHIEVEMENT_CACHE
    result = await db.execute(select(Achievement))
    ACHIEVEMENT_CACHE = {a.id: a for a in result.scalars().all()}

async def check_achievements(db: AsyncSession, user: User):
    new_achievements = []
    
    for achievement in ACHIEVEMENT_CACHE.values():
        if not await has_achievement(db, user, achievement.id):
            if meets_criteria(user, achievement):
                await grant_achievement(db, user, achievement)
                new_achievements.append(achievement)
    
    return new_achievements

async def has_achievement(db: AsyncSession, user: User, achievement_id: int):
    result = await db.execute(
        select(UserAchievement)
        .filter_by(user_id=user.id, achievement_id=achievement_id)
    )
    return result.scalar_one_or_none() is not None

def meets_criteria(user: User, achievement: Achievement):
    # This can stay synchronous as it doesn't touch the database
    if achievement.criteria_type == "quiz_count":
        return user.total_quizzes >= achievement.threshold
    elif achievement.criteria_type == "xp":
        return user.xp >= achievement.threshold
    elif achievement.criteria_type == "perfect_score":
        return user.perfect_scores >= achievement.threshold
    return False

async def grant_achievement(db: AsyncSession, user: User, achievement: Achievement):
    user_achievement = UserAchievement(
        user_id=user.id,
        achievement_id=achievement.id
    )
    db.add(user_achievement)
    await db.commit()
    await db.refresh(user_achievement)