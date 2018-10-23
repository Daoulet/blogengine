from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 120)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to="static/media/", blank=True)

    def __str__(self):
    	return "Заголовок %s %s" % (self.date, self.title,)
 #  or just
 #  def __str__(self):
 #   	return self.title




 		
