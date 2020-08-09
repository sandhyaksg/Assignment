from rest_framework import serializers
from .models import User
from .models import activityPeriods
class activityPeriodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = activityPeriods
        fields = ('start_time', 'end_time')

class UserSerializer(serializers.ModelSerializer):
    activity_periods = activityPeriodsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'real_name','timezone','activity_periods')
