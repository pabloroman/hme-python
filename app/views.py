from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Min, Sum, Avg
from app.models import Album, Band, Review

# Create your views here.
def index(request):

# SELECT `app_album`.*, AVG(`score`) as `avg` FROM `app_album` INNER JOIN `app_review` ON `app_album`.`id` = `app_review`.`album_id` WHERE `app_review`.`date` > "2013-10-01" AND `app_album`.`year` = "2013" GROUP BY `album_id` ORDER BY `avg`
    
    #     album_list = Album.objects.filter(review__date__gte='2013-10-01').filter(year__gte='2013').annotate(average_score=Avg('review__score')).order_by
    
    album_list = Album.objects.filter(year__gte='2013').order_by('-score')[:24]
    return render(request, 'home.html', { 'albums': album_list })

def band_search(request):
    return render(request, 'bands/search.html')

def band_index(request):
    band_list = Band.objects.order_by('name')
    paginator = Paginator(band_list, 20)
    page = request.GET.get('page')
    try:
    	band_list = paginator.page(page)
    except PageNotAnInteger:
    	band_list = paginator.page(1)
    except EmptyPage:
    	band_list = paginator.page(paginator.num_pages)
    	
    return render(request, 'bands/index.html', { 'bands': band_list })

def band_show(request, band_id):
	band = get_object_or_404(Band, pk=band_id)
	return render(request, 'bands/show.html', { 'band': band })
	
def album_index(request):
    return render(request, 'albums/index.html')

def album_show(request, album_id):
    return render(request, 'albums/show.html')

def genre_index(request):
    return render(request, 'genres/index.html')

def genre_show(request, genre_id):
    return render(request, 'genres/show.html')

def years_show(request, year_start, year_end):
    album_list = Album.objects.filter(year__gte=year_start).filter(year__lt=year_end).order_by('-score')[:60]
    return render(request,  'home.html', {'albums': album_list })
