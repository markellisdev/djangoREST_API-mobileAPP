from .models import Fish
from rest_framework import serializers

class FishSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fish
		fields = ('name', 'active', 'created')