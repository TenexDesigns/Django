URLs
*********************************************************************************************************************************************8
Create a file named urls.py in the same folder as the views.py file, and type this code in it: We can name it anything , but by convection, we call it , urls.py

    
    Here we map our urls to our view functions.
    NOTE --> wE ALWAYS END OUR ROUTS WITH A BACK SLASH


my_tennis_club/members/urls.py:

from django.urls import path
from . import views              // From the current folder , import the viws folder

                       # Here we define the url pattters vaiable. This is what django looks for . 
                       # Inside the url patters , we define a function that takes argumnets , 1st arguent is  a route which is a string, next is a view wuch we impoeted. We do not call the view(put parrenthesis )
                       # The path function returns a url pattern object
    
    
  # This below is a url configuration 
  # Each app can have its own url configuration
  # Now we need to import this url configuration into the main url configuration of this project

    
    urlpatterns = [
    path('members/', views.members, name='members'),
]




The urls.py file you just created is specific for the members application.
We have to do some routing in the root directory my_tennis_club as well.
This may seem complicated, but for now, just follow the instructions below.

There is a file called urls.py on the my_tennis_club folder,
open that file and add the include module in the import statement,
and also add a path() function in the urlpatterns[] list, with arguments that will route users that comes in via 127.0.0.1:8000/.

Then your file will look like this:

my_tennis_club/my_tennis_club/urls.py:

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),      // What ever we put in the quotes as the route , will be appened to wht evr we used as the rout in our app level url configuration 
    path('admin/', admin.site.urls),        // So if here we have 'members/' and in our app level url configuration, we  have 'members/ coooks/'
]                                          // What this means is that, it tells django thatall urls starting with 'members/' will ne handled by the item  in the include i.e memebrs.urls.
                                          // So when we go to the memebers.url url configuration, we have the path 'memebers/cooks'. So we can remove this member part since it is handled in the root url configuration
                                          // So in the app level url configuration we can just put , 'cooks/'


If the server is not running, navigate to the /my_tennis_club folder and execute this command in the command prompt:


py manage.py runserver



NOTE

from django.urls import path
from . import views

urlpatterns = [
    #This is the path in the url
    # The views is what we use to direct that get response to the named view
   # The nameis just used as an identifier
    path('members', views.members, name='members'),
    path('king',views.king,name="King")
]




WHENEVER WE MAKE  ANY CHANGES IN YOUR CODE ,THE SERVER RESTARTS ITSELF 



































































































..
