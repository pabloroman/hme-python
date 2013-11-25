from django.contrib import admin

# Register your models here.
from app.models import Band, Album, Review

admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Review)
