In Django, a field represents a column in the database table. The type of field determines the type of data that can be stored in that column.
Django comes with several built-in field types, which are described below along with code samples:



1.CharField: This field is used for storing a string of characters, such as a name or description.
  Example:
    
  
  from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    
2. TextField: This field is used for storing larger amounts of text, such as a books content or a blog post.
  Example:
    
  
  from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)




3.IntegerField: This field is used for storing integer values, such as a user's age or a product's price.
  Example:
    
  
  from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()




4.FloatField: This field is used for storing decimal values, such as a product's weight or a user's salary.
  Example:
    
  
  from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    salary = models.FloatField()

    
    
5.BooleanField: This field is used for storing boolean values, such as whether a user has agreed to terms and conditions or not.
  Example:
    
  
  from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    agreed_to_tos = models.BooleanField(default=False)

    
    
    
6.DateField: This field is used for storing dates, such as a users birthday or the date a product was added to the database. 
  Example:
    
  
  
  from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    
    
7.DateTimeField: This field is used for storing both date and time information, such as the date and time a blog post was published.
  Example:
    
  
  from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    
    
8.EmailField: This is used to store email addresses.
  
Example:
    
    from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    
9.URLField: This is used to store URLs.
  
Example:
    
    from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    
    
10.FileField: This is used to upload and store files.
  
Example:
  
  from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')

    
    
11.ImageField: This is used to upload and store image files.
Example:
  
  from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')

    
    
12.ForeignKey: This is used to create a many-to-one relationship between two models.
  
  
  Example:
    
  
  from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

  
  
  
13.ManyToManyField: This is used to create a many-to-many relationship between two models.
    
Example:
  
  
  
  from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

    
    
    
14.DecimalField: This is used to store decimal numbers with a specified precision.
  
Example:
  
  
  from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

  
  
  
15.PositiveIntegerField: This is used to store positive integers.
  
Example:
  
  from django.db import models

class Order(models.Model):
    order_number = models.PositiveIntegerField()
    # ...

    
    
 16.DurationField: This is used to store a duration of time.
  
Example:
  
  from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()

  
  
  
 17.BinaryField: This is used to store binary data, such as images or files.
  
Example:
  
  
  from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    data = models.BinaryField()

    
18.IPAddressField: This is used to store IP addresses.
  
Example:
  
  from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.IPAddressField()

    
    
 19.SlugField: This is used to store a short label or identifier, typically used in URLs.
  
Example


from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    
    
20.TimeField: This is used to store a time of day.
  
Example:
  
  from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()

    
    
21.AutoField: This is used to automatically generate a unique ID for each record in the database.
  
Example:
  
  from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    
    
22.BigIntegerField: This is used to store large integers.
  
Example:
  
  from django.db import models

class Order(models.Model):
    order_number = models.BigIntegerField()
    # ...

    
 23.PositiveSmallIntegerField: This is used to store positive small integers.
  
Example:
  
  from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
  
  
  
24. FileField: A field for storing uploaded files.
    It requires the upload_to attribute, which specifies the subdirectory within the MEDIA_ROOT where the files will be stored
    
    document = models.FileField(upload_to='documents/')

  
  
  
 25.SmallIntegerField: This is used to store small integers.
  
Example:
  
  from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    num_pages = models.SmallIntegerField()

    
    
26.UUIDField: This is used to store universally unique identifiers.
  
Example:
  
  import uuid
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
    
    
    
    
These are just a few of the many field types available in Django. 
By using these fields, you can ensure that your data is stored in a consistent and structured way.    




































































































































...