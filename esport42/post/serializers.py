from rest_framework import serializers
from base.serializers import MyUserSerializer
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = MyUserSerializer(read_only=True, required=False)
    image_url = serializers.CharField(read_only=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'resume', 'created_at', 'updated_at', 'title', 'image', 'image_url', 'is_landing')
        read_only_fields = ('id', 'created_at', 'updated_at', 'image_url')

        def get_validation_exclusion(self):
            exclusions = super(PostSerializer, self).get_validation_exclusions()
            return exclusions + ['author', 'image_url']