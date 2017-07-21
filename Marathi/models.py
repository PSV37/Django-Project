from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Movie(models.Model):
	  movie_name = models.CharField(max_length=20)
	  movie_catagory=models.CharField(max_length=30)
	  movie_director=models.CharField(max_length=20)
	  movie_producer=models.CharField(max_length=20)
	  movie_image=models.FileField()

	  def get_absolute_url(self):
            return reverse('detail', kwargs={'pk':self.pk})	

          