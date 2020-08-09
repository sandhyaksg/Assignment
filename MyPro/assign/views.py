from django.shortcuts import render

from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import activityPeriodsSerializer
from .models import User
from .models import activityPeriods

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    
class activityPeriodsViewSet(viewsets.ModelViewSet):
    queryset = activityPeriods.objects.all()
    serializer_class = activityPeriodsSerializer
    