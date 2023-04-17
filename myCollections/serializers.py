from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Collections
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ["title", "description", "movies"]