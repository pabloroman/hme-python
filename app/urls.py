from django.conf.urls import patterns, url

from app import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='home'),
	url(r'^bands/(?P<band_id>\d+)/$', views.band_show, name='bands_show'),
    url(r'^bands/$', views.band_index, name='bands_index'),
	url(r'^albums/(?P<album_id>\d+)/$', views.album_show, name='albums_show'),
    url(r'^albums/$', views.album_index, name='albums_index'),
	url(r'^genres/(?P<genre_id>\d+)/$', views.genre_show, name='genres_show'),
    url(r'^genres/$', views.genre_index, name='genres_index'),
    url(r'^search/$', views.band_search, name='search'),
)