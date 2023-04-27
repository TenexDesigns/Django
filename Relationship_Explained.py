In Django, relationships are used to represent the connections between different models(tables) in a database.
These relationships are defined using fields in the model classes.

There are three types of relationships in Django:
  
  
  
  
  One-to-one (OneToOneField):
    This relationship is used when each record in one table is related to exactly one record in another table. 
    For example, if you have a model for a person and a model for an address
    you might use a one-to-one relationship to connect each person to their corresponding address.
    This means that for each and every person  in the person table, there is one  coresponding addres in the address table.
    For example here George Can only have one addres o, In which this case he has been assigned an address of groccery
  
  
   id |   Person   | 
----+------------
  1 | George     |->-----------------------------------------
  2 | Ben        |                                           |
  3 | Chris      |                                           |
  4 | Stanly     |                                           |
  5 | Peter      |                                           |
  6 | Betric     |                                           |
  7 | Spencer    |                                           |
  8 | Trump      |                                           |
 9 | Mary        |                                           |
                                                             |
                                                             |
                                                             |
   id |  Address   |                                         |
----+------------+                                           |
                                                             |
  2 | Grocery    | <-----------------------------------------|
  3 | Beauty     |
  4 | Cleaning   |
  5 | Stationary |
  6 | Pets       |
  7 | Baking     |
  8 | Spices     |
  9 | Toys       |
 10 | Magazines  |




code

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)

class Address(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    
  In this example, we have two models: Person and Address. Each Person has exactly one Address, and each Address belongs to exactly one Person.
    We define this relationship using a OneToOneField on the Address model, which references the Person model.  




One-to-many (ForeignKey): 
  This relationship is used when each record in one table is related to many records in another table. For example, 
  if you have a model for a person and a model for addres, you might use a one-to-many relationship to connect each 
  person to its corresponding addreses. If that person has more than one addres.
  This can even be used for a video and comment example, where a video can have multiple commentts
  In this example below the person George Has mutiple addresses and we use a one to many fild relationship.





   id |   Person   | 
----+------------
  1 | George     |->-----------------------------------------
  2 | Ben        |                                           |
  3 | Chris      |                                           |
  4 | Stanly     |                                           |
  5 | Peter      |                                           |
  6 | Betric     |                                           |
  7 | Spencer    |                                           |
  8 | Trump      |                                           |
 9 | Mary        |                                           |
                                                             |
                                                             |
                                                             |
   id |  Address   |                                         |
----+------------+                                           |
                                                             |
  2 | Grocery    | <-----------------------------------------|
  3 | Beauty     |                                           |
  4 | Cleaning   |                                           |
  5 | Stationary |                                           |
  6 | Pets       |                                           |
  7 | Baking     |<------------------------------------------|
  8 | Spices     |                                           |
  9 | Toys       |                                           |
 10 | Magazines  |<------------------------------------------|
 12 | Racing     |                                           |
 13 | Baking     |                                           |                                         


code

from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    In this example, we have two models: BlogPost and Comment. Each BlogPost can have many Comments, but each Comment belongs to exactly one BlogPost.
    We define this relationship using a ForeignKey on the Comment model, which references the BlogPost model.


    
    
    
    
    
    
Many-to-many (ManyToManyField):
  This relationship is used when each record in one table is related to many records in another table,
  and each record in the other table is also related to many records in the first table.
  For example, if you have a model for a book and a model for authors,
  you might use a many-to-many relationship to connect each book to its corresponding authors.
  
  
  
  from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    published_date = models.DateField()



In this example, we have two models: Author and Book. Each Author can have many Books, and each Book can have many Authors.
  We define this relationship using a ManyToManyField on the Book model, which references the Author model.





























In SQL, a record is a row of data in a table. A table is a collection of records, and each record represents a single 
instance of the data that is being stored in the table. Each record is composed of one or more fields, which correspond to columns in the table.
For example, if you have a table that stores information about customers, each record in the table might represent a single customer,
and each field in the record might correspond to a specific attribute of the customer, such as their name, address, or phone number.

In SQL, you can use various commands and statements to insert, update, retrieve, and delete records in a table.
These operations allow you to manipulate the data stored in the table and perform various tasks, such as adding new records,
updating existing records, or querying the data to retrieve specific records based on certain criteria. 
Overall, records are an essential concept in SQL and relational databases, and they are used to represent the data that is being stored, manipulated, 
and retrieved in a structured and organized manner.

































































































....
