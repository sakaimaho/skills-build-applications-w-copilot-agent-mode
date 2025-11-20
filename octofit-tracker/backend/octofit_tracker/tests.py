from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name='Marvel')
        User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(user='Iron Man', activity='Running', duration=30)
        Leaderboard.objects.create(team='Marvel', points=100)
        Workout.objects.create(user='Iron Man', workout='Pushups', reps=50)

    def test_user(self):
        user = User.objects.get(name='Iron Man')
        self.assertEqual(user.email, 'ironman@marvel.com')

    def test_team(self):
        team = Team.objects.get(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

    def test_activity(self):
        activity = Activity.objects.get(user='Iron Man')
        self.assertEqual(activity.activity, 'Running')

    def test_leaderboard(self):
        lb = Leaderboard.objects.get(team='Marvel')
        self.assertEqual(lb.points, 100)

    def test_workout(self):
        workout = Workout.objects.get(user='Iron Man')
        self.assertEqual(workout.reps, 50)
