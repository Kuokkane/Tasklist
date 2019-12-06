from django.db import models

#Tietokantataulukko joka sisältää tehtävän ja tehtävän tilan
class List(models.Model):
	task = models.CharField(max_length = 200)
	completed = models.BooleanField(default=False)

#Tallentaa tietokantaan tehtävän nimellä
def __str__(self):
		return self.task + ' | ' + str(self.completed)