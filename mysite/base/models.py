from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.




class Team(models.Model):
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class League(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1_matches', on_delete=models.SET_NULL, null=True)
    team2 = models.ForeignKey(Team, related_name='team2_matches', on_delete=models.SET_NULL, null=True)
    referee = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

    # Dodajemy ograniczenie UniqueConstraint, aby para (team1, team2) była unikalna
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['team1', 'team2'], name='unique_match')
        ]

    def clean(self):
        # Sprawdzamy, czy team1 i team2 są takie same
        if self.team1 == self.team2:
            raise ValidationError("Team1 and Team2 cannot be the same.")

class season_table(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

class Statistics(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    wins = models.IntegerField()
    draws = models.IntegerField()
    loses = models.IntegerField()  # Typo corrected: 'loses' to 'losses'
    goals = models.IntegerField()
    goals_lost = models.IntegerField()
    def __str__(self):
        return f"{self.team.name} Statistics"  # Provides a human-readable string representation
    @property
    def points(self):
        """Calculates the points based on wins and draws."""
        return self.wins * 3 + self.draws


'''
class Season_Table(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    statistics= models.ForeignKey(Statistics, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-statistics__points']
    def __str__(self):
        return self.name
        '''
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