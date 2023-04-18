You need to instal python in your system


To check the puthon version -------->   python --version


Next check if pip is installed    --------->  pip --version



NEXT IS TO CREATA A VIRTUAL ENVIROMENT
It is suggested to have a dedicated virtual environment for each Django project,
and in the next chapter you will learn how to create a virtual environment, and then install Django in it.



Virtual Environment
************************************************************************************************************************************************
It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python.

The name of the virtual environment is your choice, in this tutorial we will call it myworld.

Type the following in the command prompt, remember to navigate to where you want to create your project:
  
  Windows:

-------------------> py -m venv myworld
  
  
This will set up a virtual environment, and create a folder named "myworld" with subfolders and files, like this:

myworld
  Include
  Lib
  Scripts
  pyvenv.cfg


Then you have to activate the environment, by typing this command:

Windows:

myworld\Scripts\activate.bat




Once the environment is activated, you will see this result in the command prompt:

Windows:

(myworld) C:\Users\Your Name>





INSTALL DJANGO
************************************************************************************************************************************************

Now, that we have created a virtual environment, we are ready to install Django.

Note: Remember to install Django while you are in the virtual environment!



Django is installed using pip, with this command:

Windows:

(myworld) C:\Users\Your Name>py -m pip install Django



ThaTs it! Now you have installed Django in your new project, running in a virtual environment!



Windows, Mac, or Unix?
You can run this project on either one. There are some small differences,
like when writing commands in the command prompt, Windows uses py as the first word in the command line, while Unix and MacOS use python:


Windows:

py --version
Unix/MacOS:

python --version




In the rest of this tutorial, we will be using the Windows command.





Django Create Project
************************************************************************************************************************************************


Once you have come up with a suitable name for your Django project,
like mine: my_tennis_club, navigate to where in the file system you want to store the code (in the virtual environment), 
  I will navigate to the myworld folder, and run this command in the command prompt:

django-admin startproject my_tennis_club



Django creates a my_tennis_club folder on my computer, with this content:

my_tennis_club
    manage.py         --- This is a wrapper around django admin.So going forward instead of using django admin, we are going to use manage.py because manage.py takes the settings of the appp into consideration. for example to run a server  instead of doing django-admin  runserver , we are going to do it like "py manage.py runserver" . This is because django at this point doen't know about the settings of our project.
    my_tennis_club/
        __init__.py   --- Defines this directory as a package
        asgi.py                                                          --- Used for deployment
        settings.py   --- where we define our application settings
        urls.py       --- Where we define the urls of our application
        wsgi.py                                                          --- Used for deplayment


These are all files and folders with a specific meaning, you will learn about some of them later in this tutorial,
but for now, it is more important to know that this is the location of your project, and that you can start building applications in it.

CONTINUES HERE__________________________________________________________________________________________________________________________________________________________
FOR EXAMPLE IN THE SETTINGS.PY FILE WE HAVE a section of code for installed app


# Application definition

// Thse are all app used in djabgo with their own functionality

INSTALLED_APPS = [
    # each app has its own functionality, we can even create ou own apps.
    'django.contrib.admin',# Gives us an admin interface for managing our data
    'django.contrib.auth',# Used for authenticatin users
    'django.contrib.contenttypes',
    'django.contrib.sessions',# we do'nt use sessions any more ,as it is kind of legacy
    'django.contrib.messages',# used for displaying one time notifications to the user
    'django.contrib.staticfiles',# used for sefing static files , like images ,css files and so on
     'stores'  // Here we regester the app that we create


]





































































































































































CONTINUES HERE__________________________________________________________________________________________________________________________________________________________




Run the Django Project
************************************************************************************************************************************************

Now that you have a Django project, you can run it, and see what it looks like in a browser.

Navigate to the /my_tennis_club folder and execute this command in the command prompt:

  
  py manage.py runserver



Open a new browser window and type 127.0.0.1:8000 in the address bar.
 if you run  py manage.py runserver without specifying a port e.g    py manage.py runserver 9000, by default 

  
  
  
  
  
  
  
  
  
  We have a Django project!

The next step is to make an app in your project.

You cannot have a web page created with Django without an app.

Next we have to create a django app











































































































..
