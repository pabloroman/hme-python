from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^bands/(?P<band_id>\d+)/$', views.band_show, name='bands_show'),
    url(r'^bands/$', views.band_index, name='bands_index'),
)