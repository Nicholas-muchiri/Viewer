from django.db import models

# Create your models here.
class Image(models.Model):
	picture = models.ImageField(upload_to='picture/')
    name = models.CharField(max_length =60)
    details = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news
    
    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news