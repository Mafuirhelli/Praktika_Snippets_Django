from pygments import highlight
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner']

class UserSerializer(serializers.ModelSerializer):
   snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
   class Meta:
       model = User
       fields = ['url', 'id', 'username', 'snippets']