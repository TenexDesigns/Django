^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ MANAGERS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In Django ORM, a manager is a Python class that provides methods for querying the database. 
A manager is associated with a model class, and is responsible for performing queries on that model's database table.

When you define a model in Django, a default manager is created for you automatically.
This manager provides basic query methods like all(), filter(), and get().
However, you can also define your own custom managers that provide additional query methods or modify the behavior of the default manager.

Heres an example of a custom manager that returns only active records:
  
  
  class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

      
      
      
 To use this custom manager, you would add it to your model like this:
  
  
  class MyModel(models.Model):
    # Fields go here...

    objects = ActiveManager()




In this example, the ActiveManager class defines a get_queryset() method that filters the results to only include records where the active field is True.
Then, the objects attribute of the MyModel class is set to an instance of the ActiveManager class, which means that queries
on MyModel will use the ActiveManager instead of the default manager.


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ QUERY SETS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^READ MORE ABOUT QUERY SETS IN THIS DJANGO TUTORIAL.

A QuerySet is a collection of data from a database.

A QuerySet is built up as a list of objects.

QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.


QuerySets are objects that represent a collection of records from a database table.
QuerySets are returned by the managers query methods. QuerySets provide a way to chain multiple queries together,
allowing you to filter, exclude, and order records as needed.




Heres an example of how you might use a QuerySet to filter records:
  
  # Get all records where the name starts with 'J'
j_records = MyModel.objects.filter(name__startswith='J')

# Get all active records where the name starts with 'J'
j_active_records = MyModel.objects.filter(name__startswith='J', active=True)




In this example, we first retrieve all records from the MyModel table where the name starts with 'J',
using the filter() method. Then, we further filter those results to only include active records.

QuerySets are lazy, which means that they dont actually execute the query until you try to access the data.
This allows you to chain multiple queries together and optimize your database access by only retrieving the data you need.



QUERY METHODS
*******************************************************************************************************************************************


In Django, a manager is a class that encapsulates the database access logic for a particular model.
It provides methods for querying the database to retrieve, create, update, and delete records.

Some of the commonly used query methods in the manager in Django are:



all() - Returns all the records for the model.
filter() - Returns a QuerySet containing the records that match the specified criteria.
exclude() - Returns a QuerySet containing the records that do not match the specified criteria.
get() - Returns a single record that matches the specified criteria. Raises an exception if multiple records are found.
create() - Creates a new record with the specified data.
update() - Updates one or more records that match the specified criteria.
delete() - Deletes one or more records that match the specified criteria.
values() - Returns a QuerySet containing a subset of fields for each record.
order_by() - Returns a QuerySet containing the records sorted by one or more fields.


























































































































...
