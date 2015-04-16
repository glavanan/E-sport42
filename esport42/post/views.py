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
                else (permissions.IsAdminUser(), IsOwnerOrAdmin()))

    def perform_create(self, serializer):
        print self.request.data['image']
        path = FRONT_POST + str(self.request.data['image'])
        path = path.split('.')
        path[-1] = ".crop." + path[-1]
        dest = ""
        dest = dest.join(path)
        with Image.open(self.request.data['image']) as im:
            tmp2 = im.size[0] / 400
            tmp = im.size[1] / 300
            if (tmp2 < tmp):
                tmp = tmp2
            if (tmp == 0):
                tmp = 1
            size = (int(im.size[0] / tmp), int(im.size[1] / tmp))
            im.thumbnail(size)
            print size
            print size[0] / 2 - 150
            print size[1] / 2 - 100
            box = ((size[0] / 2) - 150, (size[1] / 2) - 100, size[0] / 2 + 150, size[1] / 2 + 100)
            im = im.crop(box)
            im.save(dest, im.format)
        instance = serializer.save(author=self.request.user, image_url=dest)
        return super(PostViewSet, self).perform_create(serializer)
        return Response({'status' : 'Bad request',
                         'message' : 'post could not be created with received data.'}, status=status.HTTP_400_BAD_REQUEST)


class AdminPostViewSet(viewsets.ViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        return ((permissions.AllowAny(),) if self.request.method == 'GET'
                else (permissions.IsAdminUser(), IsOwnerOrAdmin()))
