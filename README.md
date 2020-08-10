# Assignment
Requirements: Virtual enverionment for Python,Installed with Django, djangorestframework

Project Dettails:
MyPro is a project file having assign app used to create API
This assign app include files like,
-------Model.py having 2 models with the name User and activityPeriods having many to many realtionship (Considering User has many multilple  activityPeriods)
-------Intail migration should be done to create respective DB
-------factories.py for populating the random data as per the model design
------serializers.py for seriallizing the data in the db with respect to the models
------views.py for displaying the serialized data in the form of jSON file
------urls.py for to get URL to link the views of the models

This assign app Included folders called management/commands
-----Used to created own commonds
-----Here it has two files
--------create_user.py, used to populate User objects
--------active.py, used to populate activityPeriods objects (file names will be used to populate the data as below)

How to populate the data: (we can repeat  multiple times)
Since the relation is many to many,  Many User has Many activityPeriods
fisrt populate the activityperiods data using cmd $python manage.py active 4
-----(here 4 indiates no of activityperiods objects need to create, here 4 activityperiods objects with ids 1, 2,3,4 respectively -this will create with same values,we can sperately create single objects with cmd $python manage.py active 1,executed 4 times)

Next populate indiviual user object with list of activityperiods objects, so cmd $python manage.py create_user 1 2 3 
-----( Here creating fisrt user object with list of activityperiods of id 1, 2, 3, We can create N number of users like this)
cmd $python manage.py create_user 1  3 
-----(Here creating fisrt user object with list of activityperiods of id 1,3) 

Run the Server $python manage.py runserver
go to the localhost http://127.0.0.1:8000 we get the rest API framework


