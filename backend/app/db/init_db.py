import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.models.user import User
from app.models.quiz import Quiz, Question, UserScore
from app.models.achievement import Achievement, UserAchievement

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

def init_db():
    # Create tables
    from app.core.database import Base
    engine = create_engine(settings.DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    
    # Create session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        # Create initial achievements
        achievements = [
            {
                "name": "Rookie",
                "description": "Complete your first quiz",
                "icon": "/icons/rookie.png",
                "criteria_type": "quiz_count",
                "threshold": 1
            },
            {
                "name": "Perfect Streak",
                "description": "Get 3 perfect scores in a row",
                "icon": "/icons/streak.png",
                "criteria_type": "perfect_streak", 
                "threshold": 3
            }
        ]

        for achievement in achievements:
            if not db.query(Achievement).filter_by(name=achievement["name"]).first():
                db.add(Achievement(**achievement))
        
        db.commit()
        print("✅ Database initialized successfully")

    except Exception as e:
        db.rollback()
        print(f"❌ Error initializing database: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()