from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tracking, Poi

class UserSerializer(serializers.ModelSerializer):
    trackings = serializers.PrimaryKeyRelatedField(many=True, queryset=Tracking.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups', 'trackings']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TrackingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Tracking
        fields = ['id', 'owner', 'date', 'latitude', 'longitude']      

class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = ['name', 'latitude', 'longitude', 'rank']  