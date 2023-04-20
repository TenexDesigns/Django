In Django, Q objects can be used to create complex queries with logical operators.
Here are some examples of complex lookups using Q objects in Django:



OR queries: 
  To perform OR queries, you can use the Q object with the | operator. For example, to find objects where the name is either "John" or "Jane",
  you can use the following code: MyModel.objects.filter(Q(name='John') | Q(name='Jane'))

AND queries:
  To perform AND queries, you can use the Q object with the & operator.
  For example, to find objects where the name is "John" and the age is 25, you can use the following code: MyModel.objects.filter(Q(name='John') & Q(age=25))


Nested queries:
  You can also nest Q objects to create more complex queries. For example, to find objects where the name is "John" and the age is either 25 or 30, 
  you can use the following code: MyModel.objects.filter(Q(name='John') & (Q(age=25) | Q(age=30)))



Negating queries:
  You can use the ~ operator with Q objects to negate a query. 
  For example, to find objects where the name is not "John", you can use the following code: MyModel.objects.filter(~Q(name='John'))


Case-insensitive queries:
  To perform case-insensitive queries, you can use the Q object with the i prefix. 
  For example, to find objects where the name contains "john" (case-insensitive),
  you can use the following code: MyModel.objects.filter(Q(name__icontains='john'))



Subqueries:
  You can also use subqueries with Q objects. For example, to find objects where the age is greater than the average age of all objects,
  you can use the following code: MyModel.objects.filter(age__gt=MyModel.objects.aggregate(avg_age=Avg('age'))['avg_age'])




Combining AND and OR queries:
  You can combine AND and OR queries using parentheses and | and & operators with Q objects.
  For example, to find objects where the name is "John" and the age is either 25 or 30, or the name is "Jane" and the age is 35,
  you can use the following code: MyModel.objects.filter(Q(name='John') & (Q(age=25) | Q(age=30)) | Q(name='Jane', age=35))



Searching for values in a list:
  You can use the in operator and Q objects to find objects where a fields value is in a list of values. 
  For example, to find objects where the age is 25, 30, or 35, you can use the following code: MyModel.objects.filter(Q(age__in=[25, 30, 35]))    



Querying related models: 
  You can use Q objects to query related models using the double underscore notation.
  For example, to find objects where the related ForeignKeyModel has a name of "Example",
  you can use the following code: MyModel.objects.filter(foreign_key_field__name='Example')



Chaining multiple queries:
  You can chain multiple queries together using the Q objects and | and & operators. For example, to find objects where the name
  is "John" and the age is either 25 or 30, or the name is "Jane" and the age is 35, and the city is "New York", 
  you can use the following code: MyModel.objects.filter((Q(name='John') & (Q(age=25) | Q(age=30)) | Q(name='Jane', age=35)) & Q(city='New York'))




Combining multiple Q objects: 
  You can combine multiple Q objects using & and | operators 
  to create more complex queries. For example, to find objects where the name is either "John" or "Jane" and the age is greater than 25,
  you can use the following code: MyModel.objects.filter(Q(name='John') | Q(name='Jane'), Q(age__gt=25))






These are just a few more examples of the many complex lookups you can perform using Q objects in Django.
Remember to refer to the Django documentation for more information and examples.





















































































....
