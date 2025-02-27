from django.shortcuts import render
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing

# Create your views here.
from django.http import HttpResponse

def index(request):
    # return HttpResponse('<h1>Testing BTRE Home Page</h1>')
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')