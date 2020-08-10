import factory
from factory.django import DjangoModelFactory
from datetime import datetime;
from datetime import timedelta
from .models import User
from .models import activityPeriods
from faker import Factory
# Defining a factory
faker = Factory.create()
import random

n=None;
class activityPeriodsFactory(factory.DjangoModelFactory):
    global n;
    n = random.randint(0,10)*60;
    class Meta:
        model = activityPeriods  
    start_time =(datetime.now()+timedelta(seconds=n)).strftime("%a %I:%M:%S %p")
    end_time =  (datetime.now()+timedelta(seconds=n+7200)).strftime("%a %I:%M:%S %p")
    
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    #id = factory.Sequence(lambda n: 'User%d' % n)
    real_name= faker.name();
    timezone = factory.Iterator(["America/Los_Angeles", "Asia/Kolkata", "Island/Kiribati"])
    
    @factory.post_generation
    def activity_periods(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.activity_periods.add(group)

    