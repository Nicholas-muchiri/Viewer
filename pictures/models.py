from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Picture(models.Model):
	picture = models.ImageField(upload_to='picture/',null=True)
	name = models.CharField(max_length=60)
	details = models.TextField()
	category = models.ForeignKey(Category)
	location = models.ForeignKey(Location)
	pub_date = models.DateTimeField(auto_now_add=True)



	def save_picture(self):
		self.save()

	@classmethod
	def todays_picture(cls):
		today = dt.date.today()
		picture = cls.objects.filter(pub_date__date = today)
		return picture
    
    
    # @classmethod
    # def search_by_title(cls,search_term):
    #     news = cls.objects.filter(title__icontains=search_term)
    #     return news