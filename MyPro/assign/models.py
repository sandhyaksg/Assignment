from django.db import models

# Create your models here.
class activityPeriods(models.Model):
    start_time = models.CharField(max_length=60)
    end_time = models.CharField(max_length=60)
    def __str__(self):
        return '%s: %s' % (self.start_time, self.end_time)

class User(models.Model):
    id = models.AutoField(primary_key=True)
    real_name = models.CharField(max_length=60)
    timezone = models.CharField(max_length=60)
    activity_periods = models.ManyToManyField(activityPeriods)
    
    def __str__(self):
        return self.real_name


