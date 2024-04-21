from django.db import models

# Create your models here.

class Match(models.Model):
    referee=models.CharField(max_length=50)
    stadium=models.CharField(max_length=50)


class Team(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Statistics(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    wins=models.IntegerField()
    draws=models.IntegerField()
    loses=models.IntegerField()
    goals=models.IntegerField()
    goals_lost=models.IntegerField()
    points = models.IntegerField()

    class Meta:
        ordering = ['-points']

    def calculate_points(self):
        return self.wins * 3 + self.draws  # Punkty za zwycięstwo: 3, za remis: 1, za porażkę: 0

    def save(self, *args, **kwargs):
        self.points = self.calculate_points()
        super(Statistics, self).save(*args, **kwargs)
class Season_Table(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    statistics= models.ForeignKey(Statistics, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-statistics__points']
    def __str__(self):
        return self.name
class Participation(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    match=models.ForeignKey(Match,on_delete=models.CASCADE)

class Player(models.Model):
    name = models.TextField(max_length=20)
    surname = models.TextField(max_length=20)
    age = models.IntegerField()
    nationality = models.TextField(max_length=20)
    number = models.IntegerField()
    position = models.TextField(max_length=20)

    def __str__(self):
        return str(self.name+" "+ self.surname)





class Contract(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "Piłkarz: "+str(self.player)+" "+"Drużyna: "+str(self.team)

class Squad(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
class Scorer_Table(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goal = models.IntegerField()

    def __str__(self):
        return str(self.player)+" "+"Goals: "+str(self.goal)