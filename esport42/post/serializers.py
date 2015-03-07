from rest_framework import serializers
from base.serializers import MyUserSerializer
from post.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = MyUserSerializer(read_only=True, required=False)
    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created_at', 'updated_at', 'title', 'image')
        read_only_fields = ('id', 'created_at', 'updated_at')

        def get_validation_exclusion(self):
            exclusions = super(PostSerializer, self).get_validation_exclusions()
            return exclusions + ['author']