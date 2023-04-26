^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ MANAGERS ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


In Django ORM, a manager is a Python class that provides methods for querying the database. 
A manager is associated with a model class, and is responsible for performing queries on that models database table.

When you define a model in Django, a default manager is created for you automatically.
This manager provides basic query methods like all(), filter(), and get().

In this example the manager comes after the ProductModel.objects  . This gives us many methods to access the data from the database seuc as
ProductModel.objects.all()   -- To Get alll the dtaa from the database
ProductModel.object.get(pk=1) - Returns a single record that matches the specified criteria.
and many more discussed here below.
This manage acts as an interface between our django app and our database.

Note -> That when we run most of this methods , we dont get the actual data , insted we get a guery set
i.e dataFormDatabase = ProductModel.objects.all() --> Here the dataFromDataBase is a quey set insted of the actual data.
This means that the return query set is lazy, i.e has not been implemented, We can thus even implement adtional fileters on the retyurnd query e.g 
 dataFormDatabase = ProductModel.objects.all() 
  datafromDatabase.filter(age>5).filter(gender=male)  
The only time a qeyset is implamented is fit
1.It is converted
   dataFormDatabase = ProductModel.objects.all() 
    list(datafromdatabase)
 2.When sliced or you access an individual element
    dataFormDatabase = ProductModel.objects.all() 
    datafromDatabase[0:6]---------------------------Sliced
    datafromDatabase[0:6]---------------------------Access single item
3. When the queryset is terated over or looped
 dataFormDatabase = ProductModel.objects.all() 
    for product in datafromdatabase:
        print(product)

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
from StoreApp import ProductModel


def GetDataFromDataBase:
    dataFormDatabase = ProductModel.objects.all()
    
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    


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

In this example the manager comes after the ProductModel.objects  . This gives us many methods to access the data from the database seuc as
ProductModel.objects.all()   -- To Get alll the dtaa from the database
ProductModel.object.get(pk=1) - Returns a single record that matches the specified criteria.
and many more discussed here below.
This manage acts as an interface between our django app and our database.

Note -> That when we run most of this methods , we dont get the actual data , insted we get a guery set
i.e dataFormDatabase = ProductModel.objects.all() --> Here the dataFromDataBase is a quey set insted of the actual data.
This means that the return query set is lazy, i.e has not been implemented, We can thus even implement adtional fileters on the retyurnd query e.g 
 dataFormDatabase = ProductModel.objects.all() 
  datafromDatabase.filter(age>5).filter(gender=male)  
The only time a qeyset is implamented is fit
1.It is converted
   dataFormDatabase = ProductModel.objects.all() 
    list(datafromdatabase)
 2.When sliced or you access an individual element
    dataFormDatabase = ProductModel.objects.all() 
    datafromDatabase[0:6]---------------------------Sliced
    datafromDatabase[0:6]---------------------------Access single item
3. When the queryset is terated over or looped
 dataFormDatabase = ProductModel.objects.all() 
    for product in datafromdatabase:
        print(product)


        
        Some methods do not retun query sets such as count(). Since the result is small and not much operations can be done on it.
        
        explain query set in django with code samples and them being lazy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     
In Django, a query set is a collection of database objects or rows that have been retrieved from the database based on a certain set of conditions or filters. 
A query set is essentially a lazy representation of the database objects, which means that the actual database query is not executed until the query set is evaluated.
This approach provides several benefits such as reduced memory usage, improved performance, and better optimization.

Here is an example code that demonstrates the use of a query set in Django:
 
 
 # Import the necessary modules
from django.db import models

# Define a model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title

# Create a query set
book_queryset = Book.objects.filter(published_date__year=2022)

# Iterate over the query set
for book in book_queryset:
    print(book)


  In this example, we define a model named Book with three fields: title, author, and published_date. We then create a query set by filtering all 
   the books whose published_date is in the year 2022. 
   This query set is lazy, meaning that the database query is not executed at this point.
   
   
   Next, we iterate over the query set to retrieve each book object that meets our filter condition. 
   The actual database query is executed during the iteration process. The __str__() method of the Book model is used to print the book's title.
   
   
   One of the benefits of using a lazy query set is that we can chain multiple filters together to further narrow down our results without actually executing the query until we evaluate the query set.
   For example:

    book_queryset = Book.objects.filter(published_date__year=2022).filter(author="J.K. Rowling")

    This query set will only retrieve books published in 2022 and written by J.K. Rowling, but the database query will not be executed until we evaluate the query set.
    
    In summary, a query set in Django is a lazy collection of database objects that can be filtered, sliced, and ordered without actually executing the query until the query set is evaluated.
    This approach provides several benefits, including improved performance and reduced memory usage.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^     
        
        
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
annotate() - Returns a QuerySet containing calculated fields for each record.
select_related() - Returns a QuerySet with related objects preloaded.
values_list() - Returns a QuerySet containing a tuple of values for each record.
distinct() - Returns a QuerySet containing unique records.
values_queryset() - Returns a QuerySet containing related objects.
raw() - Returns a QuerySet containing raw SQL queries.


******************************************************************************************************************************************

For example, if you have a model called "Book" with attributes like "title", "author", "published_date", "price",
etc., you can use the manager to query the database to find all the books by a particular author 
or find all the books published after a specific date. Here's an example:


from django.db import models

class BookManager(models.Manager):
    def published_after(self, date):
        return self.filter(published_date__gte=date)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    objects = BookManager()

    
    
In the example above, weve defined a custom manager called BookManager with a method called published_after that takes a
date as an argument and returns all the books published after that date. 
Weve also specified that the Book model should use this manager by setting objects = BookManager().
With this manager in place, we can easily retrieve books published after a specific date like this:    



books = Book.objects.published_after(date(2022, 1, 1))


This will return a QuerySet containing all the books published after January 1, 2022.
******************************************************************************************************************************************











order_by() - Returns a QuerySet containing the records sorted by one or more fields.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method
called get_queryset that returns all the books sorted by title in ascending order and published date in descending order.

class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('title', '-published_date')

   



values() - Returns a QuerySet containing a subset of fields for each record.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method
called published_after that returns only the title and author fields of the books published after a specific date.
This can be useful when you only need a subset of fields for a large number of records.

class BookManager(models.Manager):
    def published_after(self, date):
        return self.filter(published_date__gte=date).values('title', 'author')

books = Book.objects.published_after(date(2022, 1, 1))




annotate() - Returns a QuerySet containing calculated fields for each record.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called authors_with_books that returns a count of books for each author. 
This is achieved by using the annotate() method with the Count() function.
The resulting QuerySet will have a num_books field for each author.


from django.db.models import Count

class BookManager(models.Manager):
    def authors_with_books(self):
        return self.values('author').annotate(num_books=Count('id'))

authors = Book.objects.authors_with_books()





select_related() - Returns a QuerySet with related objects preloaded.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called get_queryset that preloads the author object for each book. 
This can be useful when you know youll be accessing related objects and want to avoid additional database queries.


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('author')

books = Book.objects.all()




values_list() - Returns a QuerySet containing a tuple of values for each record.
******************************************************************************************************************************************
In the example above, weve defined a custom manager called BookManager with a method called published_after that returns 
a tuple of the title, author, and price fields for the books published after a specific date.
This can be useful when you only need a subset of fields and want to avoid the overhead of creating model instances.



class BookManager(models.Manager):
    def published_after(self, date):
        return self.filter(published_date__gte=date).values_list('title', 'author', 'price')

books = Book.objects.published_after(date(2022, 1, 1))






distinct() - Returns a QuerySet containing unique records.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method 
called distinct_authors that returns a list of unique authors sorted by name. 
This is achieved by using the distinct() method with the author field as the argument.


class BookManager(models.Manager):
    def distinct_authors(self):
        return self.order_by('author').distinct('author')

authors = Book.objects.distinct_authors()








values_queryset() - Returns a QuerySet containing related objects.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called get_queryset that returns a QuerySet containing the related
author objects for each book. This can be useful when you want to prefetch related objects for multiple records.


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().values_queryset('author')

books = Book.objects.all()







raw() - Returns a QuerySet containing raw SQL queries.
******************************************************************************************************************************************

In the example above, we've defined a custom manager called BookManager with a method called raw_query that allows you to execute raw SQL queries. 
This can be useful when you need to perform complex queries that can't be expressed using the Django ORM.


class BookManager(models.Manager):
    def raw_query(self, query):
        return super().get_queryset().raw(query)

books = Book.objects.raw_query('SELECT * FROM books WHERE published_date >= "2022-01-01"')






filter() - Returns a QuerySet containing records that match specified criteria.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called available_books that returns a
QuerySet containing books with a status of 'available'. This can be useful when you want to filter records based on specific criteria.

class BookManager(models.Manager):
    def available_books(self):
        return self.filter(status='available')

books = Book.objects.available_books()




exclude() - Returns a QuerySet containing records that do not match specified criteria.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called unavailable_books 
that returns a QuerySet containing books that do not have 
a status of 'available'. This can be useful when you want to exclude records based on specific criteria

class BookManager(models.Manager):
    def unavailable_books(self):
        return self.exclude(status='available')

books = Book.objects.unavailable_books()




first() - Returns the first record in a QuerySet.
******************************************************************************************************************************************
In the example above, we've defined a custom manager called BookManager 
with a method called get_first_book that returns the first book in the QuerySet. This can be useful when you want to retrieve a single record.


class BookManager(models.Manager):
    def get_first_book(self):
        return self.first()

book = Book.objects.get_first_book()







last() - Returns the last record in a QuerySet.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called get_last_book 
that returns the last book in the QuerySet. This can be useful when you want to retrieve the most recent record.


class BookManager(models.Manager):
    def get_last_book(self):
        return self.last()

book = Book.objects.get_last_book()








annotate() - Adds aggregate fields to a QuerySet.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called AuthorManager with a method called annotate_num_books that 
adds a num_books field to each author in the QuerySet,
representing the total number of books they have written. This can be useful when you want to perform calculations on related objects


from django.db.models import Count

class AuthorManager(models.Manager):
    def annotate_num_books(self):
        return self.annotate(num_books=Count('books'))

authors = Author.objects.annotate_num_books()







prefetch_related() - Retrieves related objects in a separate query to avoid performance issues.
******************************************************************************************************************************************

In the example above, weve defined a custom manager called BookManager with a method called get_queryset that
retrieves all books with their related authors objects pre-fetched in a separate query. 
This can be useful when you want to avoid performance issues caused by querying related objects for each record individually.


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related('authors')

books = Book.objects.all()






values() - Returns a QuerySet containing only specified fields.
******************************************************************************************************************************************


In the example above, weve defined a custom manager called BookManager with a method called get_titles that returns a QuerySet containing only the title field for each book. 
This can be useful when you want to retrieve a subset of fields and avoid unnecessary overhead.

class BookManager(models.Manager):
    def get_titles(self):
        return self.values('title')

titles = Book.objects.get_titles()






exists() - Returns a boolean indicating whether a record exists.
******************************************************************************************************************************************

In the example above, we've defined a custom manager called BookManager with a method called has_published_books that returns
a boolean indicating whether any books with a
status of 'published' exist in the QuerySet. This can be useful when you want to perform a simple existence check.


class BookManager(models.Manager):
    def has_published_books(self):
        return self.filter(status='published').exists()

has_published = Book.objects.has_published_books()







count() - Returns the number of objects in a QuerySet.
******************************************************************************************************************************************

In the example above, we've defined a custom manager called BookManager with a method called get_num_books that returns
the total number of books in the QuerySet. This can be useful when you want to perform a simple count of the number of records in a QuerySet.



class BookManager(models.Manager):
    def get_num_books(self):
        return self.count()

num_books = Book.objects.get_num_books()







select_related() - Retrieves related objects in a single query to reduce database hits.
******************************************************************************************************************************************

In the example above, we've defined a custom manager called BookManager with a method called 
get_queryset that retrieves all books with their related publisher objects in a single query.
This can be useful when you want to reduce the number of database hits and improve performance.


class BookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('publisher')

books = Book.objects.all()










































































...
