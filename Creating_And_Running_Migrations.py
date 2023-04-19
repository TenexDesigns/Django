 CREATING Migrations
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
In django we use migrations to create and update our databases tables based offf of the models we have in our project.
So in django, we are not going to manually create and modifiy our database tables, we are going to let django take care of that through the migrations.


After creating all your model classes, then run this command


-------> py manage.py makemigrations



After this command , django looks for all installed apps in our project , and for each app, it created a new migration file.

This files are put in the migrations folder and are given a sequence.



my_tennis_club
    manage.py
    my_tennis_club/
    members/
        migrations/
           "0001_initial.py"                              ---------> This is the first migration that creates the tabes and columns in the database
           "0002_add_new_field_to_mymodel.py"             ---------> This is the second migration that handles changes made in the model, e.g changing column name. This second  migration depends on the first migration , in that, this is migration uses the first migration, and only makes the changes t it ,e.g changing table name, instead of creating a whole new migration from scratch.
            __init__.py                                       # As you have seen above, these migration files are dependet on each other, so changing the name of a migration file is risky, e.g Changing the name of the first migration file, will nessetate you to manualy change all instances of the first name, to this new name, for esample in the second file, it uses the first migration file, so you have , to change the name of the first migration file in it.
        __init__.py
        admin.py
        apps.py
        models.py


SOME TIMES YOU MIGHT MAKE CHANGES TO THE MODELS CLASSES IN YOUR APP, THEN TRY TO RUN MIGRATIONS, AND SEE THAT THE MOGRATIONS HAVE NOT BEEN IMPLEMENTED.
 This may be, because you have not listed that app in the list of installed aps,
    
    
    RUNNIN MIGRATIONS
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    To apply the migrations to your database, you can use the migrate command. 
This command is responsible for applying and unapplying migrations, ensuring that the database schema is in sync with your models docs.djangoproject.com.
    
    ----------------------------> python manage.py migrate
    
    




HERE IS SOME MORE EXPLANATION
*******************************************************************************************************************************************************************

In Django, migrations are a way to manage changes to the database schema over time.
When you make changes to your models (e.g. add a field or rename a table), 
Django will generate a migration file that describes those changes in a way that can be applied to the database.



Migrations allow you to evolve your database schema over time, while preserving the data that already exists in the database. 
When you run a migration, Django will apply the changes to the database schema and update the database accordingly.
This can involve creating new tables, altering existing tables, adding or removing columns, and so on.


Migrations are essential for maintaining the integrity of your database schema,
and for making it possible to deploy changes to a live site without losing any data. Without migrations,
it would be very difficult to manage changes to the database schema,
and it would be easy to introduce errors or inconsistencies into the database.



HERE IS SOME MORE DIFFREENT  EXPLANATION
*************************************************************************************************************************************
---------> (creating migrations in django, what are migrations, explain this with code samples)

Sure! Heres an example of creating migrations in Django:

Lets say you have a Django app called myapp,
and you want to add a new field to one of your models called MyModel. First, you would make the necessary changes to the model definition in models.py:


from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    new_field = models.BooleanField(default=False) # new field added



Once youve made the changes to models.py, you need to create a new migration to apply those changes to the database schema.
To create a new migration, you can use the makemigrations command:



python manage.py makemigrations myapp



This will generate a new migration file in the myapp/migrations directory. The filename will start with a timestamp and end with a descriptive name,
like 0002_add_new_field_to_mymodel.py. The contents of the migration file will describe the changes you made to the model, like so:



from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='new_field',
            field=models.BooleanField(default=False),
        ),
    ]


As you can see, the operations list contains one item: a call to AddField to add the new new_field boolean field to the MyModel table.

To apply the migration to the database, you can use the migrate command:
  
  python manage.py migrate myapp

  
  This will apply any outstanding migrations for the myapp app, including the new migration that you just created.

And thats it! Youve successfully created a migration to add a new field to your model and applied it to the database schema using Djangos built-in migration tools.





HERE IS SOME MORE DIFFREENT  EXPLANATION
*************************************************************************************************************************************
Migrations in Django serve the purpose of propagating changes made to your models (e.g., adding a field, deleting a model) into your database schema.
They are designed to be mostly automatic,
but you will need to know when to create and run them, and be aware of common issues that may arise docs.djangoproject.com.




There are two main types of migrations in Django:
  
  
  Schema migrations:
    These are automatically generated by Django when you modify your models.
    They handle changes in the database schema, like creating and modifying tables and columns.

  Data migrations: 
    These are used to change the data in the database itself, often in conjunction with schema migrations.
    Django cannot automatically generate data migrations, so you need to write them manually.
    You can create an empty migration file using the command python manage.py makemigrations --empty yourappname 
    and then use the RunPython operation to execute a custom function that manipulates the data docs.djangoproject.com.





To create a migration, you can use the makemigrations command, which will generate new migration files based on the changes made to your models. 
These migration files should be committed and distributed as part of your codebase




To apply the migrations to your database, you can use the migrate command. 
This command is responsible for applying and unapplying migrations, ensuring that the database schema is in sync with your models docs.djangoproject.com.



Migrations can be optimized by "squashing" them. Squashing is the process of reducing a set of many migrations down to one or a few migrations that still represent the same changes.
This can help improve the performance of your migration code when dealing with a large number of migrations



Initial migrations are the first migrations for an app that create the initial version of the apps tables.
These migrations can be treated differently when using the --fake-initial option with the migrate command.
This option will check if the tables or columns already exist in the database and fake-apply the migration if they do docs.djangoproject.com.


Migrations provide several benefits, such as:
  
  Propagating database schema changes in a safe and controlled way across multiple instances of an application (e.g., development, production) stackoverflow.com.
  Allowing the developer to choose the database and its location, while migrations handle the creation and modification of tables and columns stackoverflow.com.


In summary, migrations in Django are a powerful tool for managing changes to your models and database schema.
They allow you to propagate changes across different instances of your application and ensure that your database schema is always in sync with your models.

















































...
