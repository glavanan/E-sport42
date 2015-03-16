from rest_framework import permissions, viewsets
from base.permissions import IsOwnerOrAdmin
from post.models import Post
from post.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        instance = serializer.save(author=self.request.user)
        return super(PostViewSet, self).perform_create(serializer)

    def get_permissions(self):
        return ((permissions.AllowAny(),) if self.request.method == 'POST'
                else (permissions.IsAdminUser(), IsOwnerOrAdmin()))