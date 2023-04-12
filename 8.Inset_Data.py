Django Insert Data


Add Records
*****************************************************************************************************************************************
The Members table created in the previous chapter is empty.

We will use the Python interpreter (Python shell) to add some members to it.


*****************************************************************************************************************************************

To open a Python shell, type this command:

py manage.py shell

At the bottom, after the three >>> write the following:

>>> from members.models import Member
Hit [enter] and write this to look at the empty Member table:

>>> Member.objects.all()

*****************************************************************************************************************************************


This should give you an empty QuerySet object, like this:

<QuerySet []>
A QuerySet is a collection of data from a database.

Read more about QuerySets in the Django QuerySet chapter.
*****************************************************************************************************************************************


Add a record to the table, by executing these two lines:

>>> member = Member(firstname='Emil', lastname='Refsnes')
>>> member.save()

*****************************************************************************************************************************************

Execute this command to see if the Member table got a member:

>>> Member.objects.all().values()

Hopefully, the result will look like this:

<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'}]>




Add Multiple Records
*****************************************************************************************************************************************

You can add multiple records by making a list of Member objects, and execute .save() on each entry:

>>> member1 = Member(firstname='Tobias', lastname='Refsnes')
>>> member2 = Member(firstname='Linus', lastname='Refsnes')
>>> member3 = Member(firstname='Lene', lastname='Refsnes')
>>> member4 = Member(firstname='Stale', lastname='Refsnes')
>>> member5 = Member(firstname='Jane', lastname='Doe')
>>> members_list = [member1, member2, member3, member4, member5]
>>> for x in members_list:
>>>   x.save()






Now there are 6 members in the Member table:
*****************************************************************************************************************************************
  

>>> Member.objects.all().values()
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stale', 'lastname': 'Refsnes'},
{'id': 6, 'firstname': 'Jane', 'lastname': 'Doe'}]>























































































































...
