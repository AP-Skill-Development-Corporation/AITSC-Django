from django.db import models

# Create your models here.

class Work(models.Model):
	t = [
		('De',"None"),
		('Py','Python'),
		('Jv','Java'),
		]
	sb = models.CharField(choices=t,default='De',max_length=10)
	title = models.CharField(max_length=100)
	des = models.CharField(max_length=150)
