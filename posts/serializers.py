from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    profile_id = serializers.ReadOnlyField(source='user.userprofile.id')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user

    class Meta:
        model = Post
        fields = [
            'id', 'user', 'name', 'title', 'content', 'created_at',
            'profile_id', 'is_owner'
        ]
