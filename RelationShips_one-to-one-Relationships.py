
DEFINING ONE TO ONE FIELD RELATIONSHIP
******************************************************************************************************************************


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






Here is some more explanation
_________________________________________________

A one-to-many relationship is defined using a ForeignKey field. For example, if you have a Book model and a Author model, 
and each book can have only one author but each author can have multiple books, you can define a one-to-many relationship between the models like this:



class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)












































































































....
