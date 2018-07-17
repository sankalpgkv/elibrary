from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author_name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0) 
    publisher = models.CharField(max_length=200, default='None')
    num_votes = models.IntegerField(default=0)
    book_image = models.CharField(max_length=250) 
    
    def __str__(self):
        return self.name       
 
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    review_text = models.CharField(max_length=300)

    def __str__(self):
        return self.review_text