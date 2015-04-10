from rest_framework import serializers
from base.serializers import MyUserSerializer
from post.models import Post
from esport42 import settings

class PostSerializer(serializers.ModelSerializer):
    author = MyUserSerializer(read_only=True, required=False)
    image_url = serializers.SerializerMethodField(read_only=True, required=False)

    def get_image_url(self, obj):
        return "%s" % (obj.image)
    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'created_at', 'updated_at', 'title', 'image', 'image_url')
        read_only_fields = ('id', 'created_at', 'updated_at', 'image_url')



        def get_validation_exclusion(self):
            exclusions = super(PostSerializer, self).get_validation_exclusions()
            return exclusions + ['author']