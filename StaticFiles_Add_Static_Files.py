Django - Add Static File


Create Static Folder
When building web applications, you probably want to add some static files like images or css files.

Start by creating a folder named static in your project, the same place where you created the templates folder:

The name of the folder has to be static.



my_tennis_club
    manage.py
    my_tennis_club/
    members/
        templates/
        static/



        
 Add a CSS file in the static folder, the name is your choice, we will call it myfirst.css in this example:

my_tennis_club
    manage.py
    my_tennis_club/
    members/
        templates/
        static/
            myfirst.css






Open the CSS file and insert the following:

my_tennis_club/members/static/myfirst.css:

body {
  background-color: lightblue;
  font-family: verdana;
}





Modify the Template

Now you have a CSS file, with some CSS styling. The next step will be to include this file in a HTML template:

Open the HTML file and add the following:

{% load static %}
And:

<link rel="stylesheet" href="{% static 'myfirst.css' %}">






Example


my_tennis_club/members/templates/template.html:

{% load static %}
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="{% static 'myfirst.css' %}">
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

</body>
</html>




Restart the server for the changes to take effect:

py manage.py runserver
And check out the result in your own browser: 127.0.0.1:8000/testing/.





*****************************************************************************************************************************************8
Didn't Work?
Just testing? If you just want to play around, and not going to deploy your work, you can set DEBUG = True in the settings.py file, 
and the example above will work.

Plan to deploy? If you plan to deploy your work, you should set DEBUG = False in the settings.py file. The example above will fail,
because Django has no built-in solution for serving static files, but there are other ways to serve static files, you will learn how in the next chapter.





Example (in development):
my_tennis_club/my_tennis_club/settings.py:

.
.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
.
.




This will make the example work, but we want you to choose DEBUG = False, because that is the best way to learn how to work with Django.

Choose Debug = False
For the rest of this tutorial, we will run with DEBUG = False, even in development, because that is the best way to learn how to work with Django.





Example:
my_tennis_club/my_tennis_club/settings.py:

.
.
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

.
.



ALLOWED_HOSTS
When using DEBUG = False you have to specify which host name(s) are allowed to host your work.
You could choose '127.0.0.1' or 'localhost' which both represents the address of your local machine.

We choose '*', which means any address are allowed to host this site.
This should be change into a real domain name when you deploy your project to a public server.




Didn't Work?
That is right, the example still does not work.

You will have install a third-party library in order to handle static files.

There are many alternatives, we will show you how to use a Python library called WhiteNoise in the next chapter.







Installing White Noise
*****************************************************************************************************************************************8

WhiteNoise
Django does not have a built-in solution for serving static files, at least not in production when DEBUG has to be False.

We have to use a third-party solution to accomplish this.

In this Tutorial we will use WhiteNoise, which is a Python library, built for serving static files.







Install WhiteNoise

To install WhiteNoise in your virtual environment, type the command below:

pip install whitenoise





The result should be something like this:

Collecting whitenoise
  Downloading whitenoise-6.2.0-py3-none-any.whl (19 kB)
Installing collected packages: whitenoise
Successfully installed whitenoise-6.2.0










Modify Settings
To make Django aware of you wanting to run WhitNoise, you have to specify it in the MIDDLEWARE list in settings.py file:

my_tennis_club/my_tennis_club/settings.py:

.
.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',]





Collect Static Files


There are one more action you have to perform before you can serve the static file from the example in the previous chapter. 
You have to collect all static files and put them into one specified folder. You will learn how in the next chapter.







Collect Static Files
*****************************************************************************************************************************************8

Handle Static Files
Static files in your project, like stylesheets, JavaScripts, and images, are not handled automatically by Django when DEBUG = False.

When DEBUG = True, this worked fine, all we had to do was to put them in the static folder of the application.

When DEBUG = False, static files have to be collected and put in a specified folder before we can use it.






Collect Static Files
To collect all necessary static files for your project, start by specifying a STATIC_ROOT property in the settings.py file.

This specifies a folder where you want to collect your static files.

You can call the folder whatever you like, we will call it productionfiles:







my_tennis_club/my_tennis_club/settings.py:

.
.

STATIC_ROOT = BASE_DIR / 'productionfiles'

STATIC_URL = 'static/'

.
.





You could manually create this folder and collect and put all static files of your project into this folder, but Django has a command that do this for you:


py manage.py collectstatic



Which will produce this result:

131 static files copied to 'C:\Users\your_name\myworld\my_tennis_club\productionfiles'.




131 files? Why so many? Well this is because of the admin user interface, that comes built-in with Django.
We want to keep this feature in production, and it comes with a whole bunch of files including stylesheets, fonts, images, and JavaScripts.

my_tennis_club
    members/
    my_tennis_club/
    productionfiles/
        admin/
        myfirst.css





The Example Should Work
Now you have collected the static files of your project, and if you have installed WhiteNoise, the example from the Add Static Files chapter will finally work.

Start the server and see the result:

   py manage.py runserver



And check out the result in your own browser: 127.0.0.1:8000/testing/.





my_tennis_club/members/templates/template.html:

{% load static %}
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="{% static 'myfirst.css' %}">
<body>

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}

</body>
</html>





































































































































































































































































...
