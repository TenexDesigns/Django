Delete Records
**********************************************************************************************************************************************************
To delete a record in a table, start by getting the record you want to delete:

>>> from members.models import Member
>>> x = Member.objects.all()[5]

**********************************************************************************************************************************************************

x will now represent the member at index 5, which is "Jane Doe", but to make sure, let us see if that is correct:

>>> x.firstname
This should give you this result:

'Jane'

**********************************************************************************************************************************************************

Now we can delete the record:

>>> x.delete()


The result will be:

(1, {'members.Member': 1})


Which tells us how many items were deleted, and from which Model.

**********************************************************************************************************************************************************


If we look at the Member Model, we can see that 'Jane Doe' is removed from the Model:



>>> Member.objects.all().values()
<QuerySet [{'id': 1, 'firstname': 'Emil', 'lastname': 'Refsnes'},
{'id': 2, 'firstname': 'Tobias', 'lastname': 'Refsnes'},
{'id': 3, 'firstname': 'Linus', 'lastname': 'Refsnes'},
{'id': 4, 'firstname': 'Lene', 'lastname': 'Refsnes'},
{'id': 5, 'firstname': 'Stalikken', 'lastname': 'Refsnes'}]>































































































































....
