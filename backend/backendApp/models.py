from django.db import models

class Name(models.Model):
    nadimak = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Score(models.Model):
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    score_value = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.score_value}"

class ScoreID(models.Model):
    score = models.ForeignKey(Score, on_delete=models.CASCADE)
    score_id_value = models.IntegerField()

    def __str__(self):
        return f"{self.score.name} - {self.category} - {self.score_id_value}"