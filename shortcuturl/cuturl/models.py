from django.db import models

# Create your models here.
class userurl(models.Model):
    url_text = models.URLField()