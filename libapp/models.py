from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0) 
    publisher = models.CharField(max_length=200, default='None')
    
    def __str__(self):
        return self.name       