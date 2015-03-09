from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from post.models import Post
from post.permissions import IsAdminOfSite
from post.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = (IsAdminOfSite,)


    def perform_create(self, serializer):
        print self.request.user
        if self.request.user.get('is_admin', None):
            instance = serializer.save(author=self.request.user)
            return super(PostViewSet, self).perform_create(serializer)
        return Response({'status' : 'Bad request',
                         'message' : 'post could not be created with received data.'}, status=status.HTTP_400_BAD_REQUEST)


class AdminPostViewSet(viewsets.ViewSet):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer

# Create your views here.
