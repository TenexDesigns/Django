In Django, migrations are used to manage changes to your database schema over time. 
Migrations are created using the manage.py command-line tool and are stored as Python code in the migrations directory of your app.


Heres how to create, run, and reverse migrations in Django:
  
  
  

1.Create a migration:
  To create a migration, you can use the makemigrations command. 
  This command looks for all installed apps in your django project and makes migrtions for each installed app
  This command analyzes your models and creates a migration file that contains the changes to your database schema.
  This command creates a migration folder.
  This folder contains files with a numbers sequrnce that indcates the changes to your datatbase, e.g the 0001initial.py indicates 
  
  'python manage.py makemigrations'
  
  The  above code in your django project , e.g If it has a Memebers App and  A Products App installed. The Memebers app can have the Customer, Orders and  Cart models and the Products app can have Promotion, Price and  Collection models
  Django looks at the installed apps In you project and makes migrations fort he models in each app. Here is an example
  
  'Migrations for 'MemebersApp':'
  MembersApp\migrations\0001_initial.py
    - Create model Customer
    - Create model Orders
    - Create model Cart

  'Migrations for 'ProductssApp':'
  MembersApp\migrations\0001_initial.py
    - Create model Promotions
    - Create model Price
    - Create model Collection
  
  
  
  
  

2.Run migrations:
  
To apply the changes to your database, you can use the migrate command. 
This command runs any outstanding migrations that havent been applied to your database.

  'python manage.py migrate



3.Reverse migrations:
  
If you need to reverse a migration and undo the changes it made to your database schema,
you can use the migrate command with the --reverse flag.

 ' python manage.py migrate your_app_name 0001 --reverse

This command will revert the migration with the specified version number.





This command will revert the migration with the specified version number.



1.Create a model in your apps models.py file:
  
 ' from django.db import models

'class Person(models.Model):
 '   name = models.CharField(max_length=100)
  '  age = models.IntegerField()'




2.Create a migration for the model:
  
  'python manage.py makemigrations

  This will create a migration file in the migrations directory of your app.




3.Run the migration:
  
  'python manage.py migrate

  This will apply the changes to your database schema.



4.Reverse the migration:
  
 'python manage.py migrate your_app_name 0001 --reverse

  This will revert the changes made by the migration with the specified version number.




These are the basic steps for creating, running, and reversing migrations in Django.
Migrations are an important part of managing your database schema and ensuring that your applications data is stored correctly over time.


































































































































































...
