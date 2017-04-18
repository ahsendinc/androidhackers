from django.contrib.auth.models import User,Group 
from .models import GenericData
from rest_framework import serializers

class GenericDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GenericData
		fields=('pubdate','jsondata')
		
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')