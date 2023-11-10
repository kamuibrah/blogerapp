from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=45, verbose_name="Author Name")
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    birth_date = models.DateField(auto_now=False,auto_now_add=False)
    no_of_articles = models.IntegerField() 

class Article(models.Model):
    title = models.CharField(max_length=50)
    summer = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateField(auto_now=False)
    is_published = models.BooleanField(default=False)