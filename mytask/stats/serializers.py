from rest_framework import serializers
from .models import Stats


class StatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stats
        fields = ('id', 'date', 'views', 'clicks', 'cost', 'cpc', 'cpm')
