from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    workouts = models.ArrayField(model_container='Workout', blank=True, null=True)
    activities = models.ArrayField(model_container='Activity', blank=True, null=True)
    leaderboard_points = models.IntegerField(default=0)
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ArrayField(model_container='User', blank=True, null=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    calories = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    user = models.CharField(max_length=150)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    def __str__(self):
        return self.name
