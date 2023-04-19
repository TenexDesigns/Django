customizing database schema in django




In Django, you can customize your database schema by defining your own database models. A model is a Python class that represents a table in the database.

Here are the steps to customize your database schema in Django:

1.Define a new model: Define a new Python class that inherits from django.db.models.Model. This new class will represent a table in your database.
  
  
  from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    In this example, we defined a new model called Person that has three fields: name, age, and email.


      2.Specify the fields: In the model class, you need to specify the fields that correspond to the columns in your database table.
        Django provides several field types you can use, such as CharField, IntegerField, and EmailField.



3.Define relationships: If you want to define relationships between tables, you can use the ForeignKey, OneToOneField, and ManyToManyField fields. 
  For example, if you want to define a one-to-many relationship between the Person and Address tables, you can add a foreign key field to the Person model:
    
    class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    In this example, we added a ForeignKey field called address to the Person model, which establishes a one-to-many relationship with the Address model.




4. Migrate the changes: Once youve defined your new models or updated the existing ones, 
  you need to generate a database migration and apply it to the database. Run the following commands in your terminal:
    
    python manage.py makemigrations
python manage.py migrate


These commands will create a new migration file based on the changes you made to your models, and then apply the migration to the database.

That's it! You've now customized your Django database schema.









































































































































































































...
