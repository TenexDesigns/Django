
DEFINING ONE TO ONE FIELD RELATIONSHIP
******************************************************************************************************************************
Note -> Django always creates the reverse relationship from one table to another, so there is no need for us, to do it.

my_tennis_club
    manage.py
    my_tennis_club/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
              models.py



from django.db import models



class Customer (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique= True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null =True)
    
    




    # Here we assume each and every custome has only one address
 # And each addrress should belong only to one customer.
 # So here we have a one to one relationship between customers and addreses.
class Address (models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #Here we create a one to one relationship between the customer modal class and the addddress modal class
    # Here we also define what should be done in the address class incase a customer is deleted. Here we have defined cascade, Meaning that i a customer is deleyed , then the coresponding address should be deleted
    # Here wehave also set the imported customer id as a foreign key, and we used it as primary key in the address modal class. This is beacuse each address is unique to one customer, so if we use the customer id as a foreighn key to be this modal classes primary key, therr is no problem as all customers have a unique id.
    Customer = models.OneToOneField(Customer,on_delete=models.CASCADE, primary_key= True)
    
    
    
  1.  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    
    
    One-to-one relationship:
        
A one-to-one relationship is defined when each instance of one model is related to exactly one instance of another model.
For example, consider a model for a Person and a model for a Passport. Each person has exactly one passport, 
and each passport belongs to exactly one person. We can define this relationship in Django using a OneToOneField:
    
    from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

class Passport(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20)
    # Other fields...
  
2.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55

    
    
    A one-to-one relationship in Django links two models, where each row in one table appears once in another table. To create a one-to-one relationship, use the OneToOneField class.
    Heres an example of a one-to-one relationship between Contact and Employee models:
        
        from django.db import models

class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    The Employee class has the contact attribute that references an instance of the OneToOneField class with the Contact model specified and the on_delete option set to models.CASCADE (pythontutorial.net).
    
    
  3.  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    
    
    Here is some more Explanation
    ________________________________________________________________

    You can also define a OneToOneField relationship to indicate that each instance of one model corresponds to exactly 
    one instance of another model. For example, if you have a Profile model that stores additional information about each user in your Django app,
    you might define a OneToOneField relationship between the Profile model and the built-in User model:

      
 from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=200)

In this example, each Profile instance is associated with exactly one User instance.

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55






DEFINING ONE TO MANY FIELD RELATIONSHIP
******************************************************************************************************************************
Here we assume a customer can have may addresses
So here we change the field relationship to one to many
Where  the custome is one and  the many ,is the multiple addresses.




my_tennis_club
    manage.py
    my_tennis_club/
    members/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
              models.py



from django.db import models



class Customer (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique= True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null =True)






class Address (models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # Here we are tellling Django that customer is a foreign key in thhis table
    # We do not put the primay key option, because , we want to have multiple addresses for the same customer.
    customer = models.ForeignKey(
      Customer,on_delete=models.PROTECT, # o here if we accedentaly delete a customer, we dont end up deleting all the addreses in that customer.
    
    )
    
   1. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
One-to-many relationship:

A one-to-many relationship is defined when each instance of one model is related to multiple instances of another model.
For example, consider a model for a BlogPost and a model for a Comment. Each blog post can have multiple comments, 
but each comment belongs to only one blog post. We can define this relationship in Django using a ForeignKey:
    from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    # Other fields...

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    # Other fields...




  2.  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    A one-to-many relationship (also known as a many-to-one relationship) in Django is defined using the ForeignKey class.
    Heres an example of a one-to-many relationship between Restaurant and Waiter models:
        
        from django.db import models

class Restaurant(models.Model):
    # ... other fields ...

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
    
    In this example, a Waiter is associated with a Restaurant using the restaurant attribute, which is an instance of the ForeignKey class (docs.djangoproject.com).
        
        

   3. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55


Here is some more explanation
_________________________________________________

A one-to-many relationship is defined using a ForeignKey field. For example, if you have a Book model and a Author model, 
and each book can have only one author but each author can have multiple books, you can define a one-to-many relationship between the models like this:



class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55







MANY TO MANY RELATIONSHIPS.
******************************************************************************************************************************




Here we are going to create a  Promotion  model class a products model class.
Here the product can have difffreent promaotions and a a promation can be on different products




class Promotion (models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    
    

class Products (models.Model):
    title= models.CharField(max_length=255)
    description = models.CharField(max_length=255)    
    promotions = models.ManyToManyField()
    
   1. %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    Many-to-many relationship:
A many-to-many relationship is defined when each instance of one model can be related to multiple instances of another model, and vice versa.
For example, consider a model for a Book and a model for an Author. Each book can have multiple authors, and each author can have written multiple books.
We can define this relationship in Django using a ManyToManyField:
    
    from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    # Other fields...

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    # Other fields...

    2.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    
    
    Many-to-many relationship
A many-to-many relationship in Django is defined using the ManyToManyField class.
Heres an example of a many-to-many relationship between Student and Course models:
    
    from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    In this example, a Student can be enrolled in multiple Course instances, and a Course can have multiple Student instances enrolled (betterprogramming.pub).
    
    3.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    
    



______________________________________________________Here is some more explanation

Many-to-Many Relationship:
A many-to-many relationship is defined using a ManyToManyField field. For example, if you have a Book model and a Tag model, and each book can have multiple tags and each tag can be associated with multiple books, you can define a many-to-many relationship between the models like this:

python
Copy code
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55










CIRCULAR RELATIONSHIP

******************************************************************************************************************************


A circular relationship is a type of relationship where two models have a many-to-many relationship with each other.
To define a circular relationship in Django, you can use the ManyToManyField field and specify the "self" option as the target model. For example,
if you have a Person model and each person can have multiple friends, and each friend is also a Person, you can define a circular relationship like this:





class Person(models.Model):
    name = models.CharField(max_length=100)
    friends = models.ManyToManyField('self')

    1.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    Circular relationship:
A circular relationship is defined when two models have a many-to-many relationship with each other.
For example, consider a model for a User and a model for a Group. Each user can be a member of multiple groups, and each group can have multiple members.
We can define this relationship in Django using a ManyToManyField with the "symmetrical=False" option:
    
    from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField('Group', symmetrical=False)
    # Other fields...

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, symmetrical=False)
    # Other fields...

    
    

    2.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    . Circular relationship
A circular relationship in Django is a relationship where two models have a ForeignKey field pointing to each other. Here's an example of a circular relationship between ModelA and ModelB:



from django.db import models

class ModelA(models.Model):
    model_b = models.ForeignKey('ModelB', on_delete=models.CASCADE, null=True)

class ModelB(models.Model):
    model_a = models.ForeignKey(ModelA, on_delete=models.CASCADE, null=True)
    
    
    
    In this example, ModelA has a ForeignKey to ModelB, and ModelB has a ForeignKey to ModelA. It's important to handle circular relationships carefully, as they can lead to issues in your application logic and performance.

    .%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55
    
    



GENERIC RELATIONSHIP
******************************************************************************************************************************
  A generic relationship is a type of relationship where a model can be related to any other model.
    Its defined using the GenericForeignKey field. For example, if you have a Comment model that 
    can be associated with any other model in your app (e.g., a BlogPost model, a Photo model, etc.), you can define a generic relationship like this:



from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()





In this example, the content_type field is a foreign key to the ContentType model, 
which is a built-in Django model that represents the type of a content object (e.g., a BlogPost object, a Photo object, etc.).
The object_id field is an integer field that stores the ID of the related object. 
The content_object field is a GenericForeignKey field that allows you to retrieve the related object using



    1.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55


A generic relationship is defined when a model can be related to multiple other models, but the related model is not known at the time of writing the model.
For example, consider a model for a Comment, where each comment can be related to either a BlogPost or a NewsArticle. We can define this relationship in Django using a GenericForeignKey:

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


In this example, "content_type" is a foreign key to Django's ContentType model, which is used to store the type of the related object



    2.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55

A generic relationship in Django allows a model to have a foreign key to any other model in your application. To create a generic relationship, 
use the GenericForeignKey class along with ContentType and PositiveIntegerField fields. Here's an example of a generic relationship in a Comment model:


from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    text = models.TextField()

    In this example, the Comment model has a generic foreign key content_object that can be associated with any model in your application (betterprogramming.pub).





    2.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55






























....
