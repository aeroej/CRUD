from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    body = models.TextField()
    pub_date = models.DateTimeField('date published') # date published : 발행일

    def __str__(self):
        return self.title