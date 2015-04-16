from rest_framework import permissions, viewsets
from base.permissions import IsOwnerOrAdmin
from post.permissions import IsAdminOfSite
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        return ((permissions.AllowAny(),) if self.request.method == 'GET'
                else (permissions.IsAdminUser(), IsOwnerOrAdmin()))

    def perform_create(self, serializer):
        print self.request.user
        if self.request.user.is_staff:
            instance = serializer.save(author=self.request.user)
            return super(PostViewSet, self).perform_create(serializer)
        return Response({'status' : 'Bad request',
                         'message' : 'post could not be created with received data.'}, status=status.HTTP_400_BAD_REQUEST)


class AdminPostViewSet(viewsets.ViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def get_permissions(self):
        return ((permissions.AllowAny(),) if self.request.method == 'GET'
                else (permissions.IsAdminUser(), IsOwnerOrAdmin()))
