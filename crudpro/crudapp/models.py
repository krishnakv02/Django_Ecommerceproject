from django.db import models

# Create your models here.

class Task(models.Model):
    task=models.CharField(max_length=250)
    complete=models.BooleanField(default=False)
    create_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task
    class Meta:
        ordering = ['-create_at']
    