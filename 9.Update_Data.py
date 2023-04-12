Update Records
***********************************************************************************************************************************************
To update records that are already in the database, we first have to get the record we want to update:

>>> from members.models import Member
>>> x = Member.objects.all()[4]

***********************************************************************************************************************************************

x will now represent the member at index 4, which is "Stale Refsnes", but to make sure, let us see if that is correct:

>>> x.firstname

This should give you this result:

'Stale'


***********************************************************************************************************************************************

Now we can change the values of this record:

>>> x.firstname = "Stalikken"
>>> x.save()

***********************************************************************************************************************************************


Execute this command to see if the Member table got updated:

>>> Member.objects.all().values()


***********************************************************************************************************************************************


Hopefully, the result will look like this:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'},
{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>


















































































































..
