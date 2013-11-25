from django.shortcuts import render, get_object_or_404

from app.models import Band

# Create your views here.
def index(request):
    return render(request, 'home.html')
    
def band_index(request):
    band_list = Band.objects.order_by('name')[:5]
    context = { 'bands': band_list }
    return render(request, 'bands/index.html', context)
	
def band_show(request, band_id):
	band = get_object_or_404(Band, pk=band_id)
	return render(request, 'bands/show.html', { 'band': band })