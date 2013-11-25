from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    formed = models.CharField(max_length=200)
    yearsactive = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    themes = models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Album(models.Model):
    band = models.ForeignKey(Band)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Review(models.Model):
    band = models.ForeignKey (Band)
    album = models.ForeignKey (Album)
    pub_date = models.DateTimeField('Published on')
    score = models.IntegerField(default=0)