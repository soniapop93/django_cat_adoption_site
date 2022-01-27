from distutils.command.upload import upload
from email.policy import default
from django.db import models
import datetime
from django.utils import timezone

class Cat(models.Model):
    cat_name_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.cat_name_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

class Cat_Details(models.Model):
    details = models.ForeignKey(Cat, on_delete=models.CASCADE)
    description_text = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=200)
    cat_photo = models.ImageField(upload_to='adoptions/', default='static/adoptions/cat_static.jpg')

    def __str__(self):
        return self.description_text


