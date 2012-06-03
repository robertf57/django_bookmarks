from django.db import models
from django.contrib.auth.models import User

# Link inherits from models.Model which is the base
# class for all models.
class Link(models.Model):
    url = models.URLField(unique=True)

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)

class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    bookmarks = models.ManyToManyField(Bookmark)
