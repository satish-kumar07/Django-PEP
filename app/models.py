from django.db import models

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    created_AT=models.DateField(auto_now=True)
    isPublish=models.BooleanField(default=True)

    def str(self):
        return self.title