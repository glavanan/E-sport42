from rest_framework import permissions, viewsets
from base.permissions import IsOwnerOrAdmin
from post.permissions import IsAdminOfSite
from post.models import Post
from post.serializers import PostSerializer
from PIL import Image
from esport42.settings import FRONT_POST, MEDIA_URL
import os

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        return ((permissions.AllowAny(),) if self.request.method == 'GET'
                else (IsOwnerOrAdmin(),))

    def perform_create(self, serializer):
        # Fais les choses proprement x_x"... https://docs.djangoproject.com/en/1.7/ref/models/fields/#django.db.models.FileField
        # os.path.join aussi :P.
        path = FRONT_POST + str(self.request.data['image'])
        path = path.split('.')
        path[-1] = ".crop." + path[-1]
        dest = ""
        dest = dest.join(path)
        # Care au join ("img.tarace.lol")
        with Image.open(self.request.data['image']) as im:
            tmp2 = float(im.size[0]) / 300
            tmp = float(im.size[1]) / 200
            if (tmp2 < tmp):
                tmp = tmp2
            if (tmp == 0):
                tmp = 1
            size = (int(im.size[0] / tmp), int(im.size[1] / tmp))
            im.thumbnail(size)
            box = ((size[0] / 2) - 150, (size[1] / 2) - 100, size[0] / 2 + 150, size[1] / 2 + 100)
            im = im.crop(box)
            try:
                im.save(dest, im.format)
            except IOError as e:
                print "I/O error({0}): {1}\nError: {2}".format(e.errno, e.strerror, e)
        instance = serializer.save(author=self.request.user, image_url=dest)
        return super(PostViewSet, self).perform_create(serializer)


class AdminPostViewSet(viewsets.ViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        return ((permissions.AllowAny(),) if self.request.method == 'GET'
                else (permissions.IsAdminUser(), IsOwnerOrAdmin()))
