from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StatsSerializer
from stats.models import Stats


class StatsViewSet(viewsets.ModelViewSet):

    queryset = Stats.objects.all().order_by('date')
    serializer_class = StatsSerializer

