Add Fields in the Model
************************************************************************************************************************************
To add a field to a table after it is created, open the models.py file, and make your changes:
  
  
my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField()
  joined_date = models.DateField()
  
  

************************************************************************************************************************************


As you can see, we want to add phone and joined_date to our Member Model.

This is a change in the Models structure, and therefor we have to make a migration to tell Django that it has to update the database:


py manage.py makemigrations members


************************************************************************************************************************************


Which, in my case, will result in a prompt, because I try to add fields that are not allowed to be null, to a table that already contains records.

As you can see, Django asks if I want to provide the fields with a specific value, or if I want to stop the migration and fix it in the model:


  
  py manage.py makemigrations members
You are trying to add a non-nullable field 'joined_date' to members without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
  
************************************************************************************************************************************
  

I will select option 2, and open the models.py file again and allow NULL values for the two new fields:

my_tennis_club/members/models.py:

from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)             // We make the fields have null values
  joined_date = models.DateField(null=True)            // We make the fields have null values



************************************************************************************************************************************
  
  And make the migration once again:

py manage.py makemigrations members



************************************************************************************************************************************
Run the migrate command:

py manage.py migrate




INSERT DATA
************************************************************************************************************************************


We can insert data to the two new fields with the same approach as we did in the Update Data chapter:

First we enter the Python Shell:


py manage.py shell



************************************************************************************************************************************

Now we are in the shell

At the bottom, after the three >>> write the following (and hit [enter] for each line):


>>> from members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()


************************************************************************************************************************************


This will insert a phone number and a date in the Member Model, at least for the first record,
the four remaining records will for now be left empty. We will deal with them later in the tutorial.

Execute this command to see if the Member table got updated:

>>> Member.objects.all().values()


************************************************************************************************************************************




The result should look like this:

<QuerySet [
{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}]>



















































































...
