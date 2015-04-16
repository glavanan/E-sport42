from django.db import models
from base.models import MyUser

class Post(models.Model):
    author = models.ForeignKey(MyUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/img/posts')

    # def __unicode__(self):
    #     return '{0}'.format(self.content)