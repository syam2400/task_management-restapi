from django.db import models

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateField()
    completed = models.BooleanField()
    image = models.ImageField(upload_to='image/',null=True,blank=True)

    def __str__(self):
        return self.title
