What is an App?
****************************************************************************************************************************************************************
An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

In this tutorial we will create an app that allows us to list and register members in a database.

But first, lets just create a simple Django app that displays "Hello World!".



Create App
****************************************************************************************************************************************************************

I will name my app members.

Start by navigating to the selected location where you want to store the app, in my case the my_tennis_club folder, and run the command below.

If the server is still running, and you are not able to write commands, 
press [CTRL] [BREAK], or [CTRL] [C] to stop the server and you should be back in the virtual environment.


         py manage.py startapp members



Django creates a folder named members in my project, with this content:

  my_tennis_club
    manage.py
    my_tennis_club/
                    -----------------------------> This is the django app. All djsngo apps have the same exact structure i.e they all have migrations folder,admin.py files and e.t.c
    members/
        migrations/ ----------------------------->   This folder is used for generating database tables
            __init__.py
        __init__.py
        admin.py  -------------------------------> Where we define how the admin interface of this app will look like               //
        apps.py --------------------------------->  Where we configure this app
        models.py ---------------------------------> Where we define the model classes for this app. We use model classes to pull data from the databases and present it to the user
        tests.py ---------------------------------> Where we write our unit tests
        views.py ---------------------------------> This is like a request handler


         
         
         We created this app, now we need to registerr this app in th settings module.
         Everytime you create an app, you need to regester it in the list of installed apps.
         You simply add the name of the app and save the changes
         
         

These are all files and folders with a specific meaning. You will learn about most of them later in this tutorial.

First, take a look at the file called views.py.

This is where we gather the information we need to send back a proper response.

You will learn more about views in the next chapter.










































































































..
