from django.db import models

class Names(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)

	class Meta:
		unique_together = ('first_name', 'last_name')

	def __str__(self):
		return f'{self.first_name} {self.last_name}'


