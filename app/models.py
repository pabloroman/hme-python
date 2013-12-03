from django.db import models
from django.db.models.fields import PositiveIntegerField
from django.utils.http import urlquote_plus
from django.utils.encoding import iri_to_uri
import hashlib, urllib

class PositiveBigIntegerField(PositiveIntegerField):
    """Represents MySQL's unsigned BIGINT data type (works with MySQL only!)"""
    empty_strings_allowed = False

    def get_internal_type(self):
        return "PositiveBigIntegerField"

    def db_type(self, connection):
        # This is how MySQL defines 64 bit unsigned integer data types
        return "bigint UNSIGNED"


# Create your models here.
class Band(models.Model):
    id = PositiveBigIntegerField(primary_key=True)
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
    id = PositiveBigIntegerField(primary_key=True)
    band = models.ForeignKey(Band)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    score = models.DecimalField(max_digits=10, decimal_places=3)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
        
    def cached_cover(self):
        hash = hashlib.sha1(str(self.id)).hexdigest()
        return '/static/images/'+hash[0]+'/'+hash[1]+'/'+hash+'.jpg'
        
    def encoded_query(self):
        return self.band.name+' '+self.name
    

class Review(models.Model):
    id = PositiveBigIntegerField(primary_key=True)
    band = models.ForeignKey (Band)
    album = models.ForeignKey (Album)
    date = models.DateTimeField('Published on')
    score = models.IntegerField(default=0)