from django.db import models
from base.models import MyUser
from esport42.settings import STATIC_URL, MEDIA_URL, FRONT_POST

class Post(models.Model):
    author = models.ForeignKey(MyUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    resume = models.TextField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=FRONT_POST)
    image_url = models.CharField(max_length=1024)

    def __unicode__(self):
        return '{0}'.format(self.title)
