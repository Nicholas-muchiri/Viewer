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


# def past_days_news(request,past_date):
    
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(news_today)
    
#     news = Article.days_news(date)
#     return render(request, 'all-news/past-news.html', {"date":date,"news":news})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Picture.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"pictures": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})