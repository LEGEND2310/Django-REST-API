from django.db.models import fields
from rest_framework import serializers
from .models import Creator


class CreatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Creator
        fields = ('name', 'bio', 'twitter', 'youtube',
                  'instagram', 'eth_address', 'charity')
