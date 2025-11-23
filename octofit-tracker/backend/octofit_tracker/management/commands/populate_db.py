from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # コレクション名
        collections = ['users', 'teams', 'activities', 'leaderboard', 'workouts']
        for col in collections:
            db[col].delete_many({})

        # ユーザーサンプルデータ
        users = [
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
            {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "marvel"},
            {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
            {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
        ]
        db.users.insert_many(users)
        db.users.create_index([("email", 1)], unique=True)

        # チームサンプルデータ
        teams = [
            {"name": "marvel", "members": [u["email"] for u in users if u["team"] == "marvel"]},
            {"name": "dc", "members": [u["email"] for u in users if u["team"] == "dc"]},
        ]
        db.teams.insert_many(teams)

        # アクティビティサンプルデータ
        activities = [
            {"user_email": "ironman@marvel.com", "type": "run", "distance": 5},
            {"user_email": "batman@dc.com", "type": "cycle", "distance": 20},
            {"user_email": "superman@dc.com", "type": "swim", "distance": 2},
        ]
        db.activities.insert_many(activities)

        # リーダーボードサンプルデータ
        leaderboard = [
            {"team": "marvel", "score": 100},
            {"team": "dc", "score": 90},
        ]
        db.leaderboard.insert_many(leaderboard)

        # ワークアウトサンプルデータ
        workouts = [
            {"name": "Morning Cardio", "suggested_for": "marvel"},
            {"name": "Strength Training", "suggested_for": "dc"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
