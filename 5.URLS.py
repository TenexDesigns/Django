URLs
*********************************************************************************************************************************************8
Create a file named urls.py in the same folder as the views.py file, and type this code in it:



my_tennis_club/members/urls.py:

from django.urls import path
from . import views

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
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]



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






































































































..
