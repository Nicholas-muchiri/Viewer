from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Picture

# # Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def picture_of_day(request):
    date = dt.date.today()
    pictures = Picture.todays_picture()
    return render(request, 'welcome.html', {"date": date, "pictures": pictures})


def filtered(request,past_date):
    picture = Picture.objects.get(id = past_date)
    return render(request, 'all-pictures/picture.html', {"picture":picture})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})

def pics(request):
   
    pictures = Picture.objects.all()

    return render(request,"welcome.html", {"pictures":pictures})