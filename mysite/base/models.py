from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.







class League(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    league_logo = models.ImageField(null=True, blank=True, upload_to="images/")

    def save(self, *args, **kwargs):
        if not self.league_logo:  # Sprawdzenie, czy nie podano logo
            # Tutaj można ustawić ścieżkę do domyślnego logo
            default_logo_path = 'media/images/default_logo.png'
            self.league_logo = default_logo_path

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Team(models.Model):
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    team_logo = models.ImageField(null=True, blank=True, upload_to="images/")

    def save(self, *args, **kwargs):
        if not self.team_logo:  # Sprawdzenie, czy nie podano logo
            # Tutaj można ustawić ścieżkę do domyślnego logo
            default_logo_path = 'media/images/default_logo.png'
            self.team_logo = default_logo_path

        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Queue(models.Model):
    number = models.IntegerField()
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Kolejka {self.number}"


class Match(models.Model):
    team1 = models.ForeignKey('Team', related_name='team1_matches', on_delete=models.SET_NULL, null=True)
    team2 = models.ForeignKey('Team', related_name='team2_matches', on_delete=models.SET_NULL, null=True)
    referee = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)
    queue_number = models.IntegerField(default=1)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} - Kolejka {self.queue_number if self.queue_number else 'Brak kolejki'}"
    def clean(self):
        # Sprawdzamy, czy team1 i team2 są takie same
        if self.team1 == self.team2:
            raise ValidationError("Team1 and Team2 cannot be the same.")

    class Meta:
        # Dodajemy ograniczenie UniqueConstraint, aby para (team1, team2) była unikalna
        constraints = [
            models.UniqueConstraint(fields=['team1', 'team2'], name='unique_match')
        ]

'''
class Finished_Match(models.Model):
    team1 = models.ForeignKey(Team, related_name='finished_team1_matches', on_delete=models.SET_NULL, null=True)
    team2 = models.ForeignKey(Team, related_name='finished_team2_matches', on_delete=models.SET_NULL, null=True)
    referee = models.CharField(max_length=50)
    stadium = models.CharField(max_length=50)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)
'''




class Season_table(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.SET_NULL, null=True)

class Statistics(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)  # Typo corrected: 'loses' to 'losses'
    goals = models.IntegerField(default=0)
    goals_lost = models.IntegerField(default=0)
    matches_played=models.IntegerField(default=0)
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

class Position(models.Model):
    position=models.CharField(max_length=20)
    def __str__(self):
        return self.position
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.TextField(max_length=20)
    position=models.ForeignKey(Position, on_delete=models.CASCADE)
    surname = models.TextField(max_length=20)
    age = models.IntegerField()
    nationality = models.TextField(max_length=20)
    number = models.IntegerField()
    goals = models.IntegerField(default=0)
    image=models.ImageField(null=True, blank=True, upload_to="images/")

    def save(self, *args, **kwargs):
        if not self.image:  # Sprawdzenie, czy nie podano logo
            # Tutaj można ustawić ścieżkę do domyślnego logo
            default_logo_path = 'media/images/default_logo.png'
            self.image = default_logo_path

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name+" "+ self.surname)




'''
class Contract(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return "Piłkarz: "+str(self.player)+" "+"Drużyna: "+str(self.team)
        '''

class Squad(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match=models.ForeignKey(Match,on_delete=models.CASCADE,default=1)
class Scorer_Table(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    goal = models.IntegerField()

    def __str__(self):
        return str(self.player)+" "+"Goals: "+str(self.goal)

def validate_positive(value):
    if value < 0:
        raise ValidationError('Wartość musi być większa lub równa zero.')




class Type_of_Card(models.Model):
    type=models.CharField(max_length=20)
    def __str__(self):
        return self.type
class Match_Penalty(models.Model):
    card=models.ForeignKey(Type_of_Card,on_delete=models.CASCADE)
    player=models.ForeignKey(Player,on_delete=models.SET_NULL,null=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE,default=1)
    team=models.ForeignKey(Team,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return str(self.card.type+" CARD,   "+self.player.name+" "+self.player.surname+" ,  "+self.match.team1.name+" vs "+ self.match.team2.name)

'''
class Match_Penalty(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    penalty = models.ForeignKey(Penalty, on_delete=models.CASCADE)
    '''

'''
class Match_Events(models.Model):
    match=models.ForeignKey(Match,on_delete=models.CASCADE)
    #goal=models.IntegerField(validators=[validate_positive])
    goal = models.IntegerField()
    penalty=models.ManyToManyField(Penalty,through='MatchPenalty')
    
class MatchPenalty(models.Model):
    match_event = models.ForeignKey(Match_Event, on_delete=models.CASCADE)
    penalty = models.ForeignKey(Penalty, on_delete=models.CASCADE)
    '''


'''
class Goal(models.Model):
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    time=models.IntegerField()
    '''

class Match_Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE,default=1)
    player=models.ForeignKey(Player,on_delete=models.CASCADE)
    time=models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Goal by {self.player} at {self.time} minute(s)"


class Match_and_Score(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, default=1)
    team1_score=models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)

class Logo(models.Model):
    logo_image=models.ImageField(null=True, blank=True, upload_to="images/")



