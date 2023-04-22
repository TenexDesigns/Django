Django Admin - Include Member

Include Member in the Admin Interface

To include the Member model in the admin interface, we have to tell Django that this model should be visible in the admin interface.

This is done in a file called admin.py, and is located in your app's folder, which in our case is the members folder.

Open it, and it should look like this:



my_tennis_club/members/admin.py:

from django.contrib import admin

# Register your models here.




Insert a couple of lines here to make the Member model visible in the admin page:

my_tennis_club/members/admin.py:

from django.contrib import admin
from . models import Member            // Here we import the models folder from the current folder i.e through the dot --> . //We import the memeber models.

# Register your models here.
admin.site.register(Member)       // Here we regesetr the imported model



# Method 2
#from django.contrib import admin     
#from . import models               // Here we import the models folder from the current folder i.e through the dot --> . //We import the memeber models.

#admin.site.register(models.Product)      // Here we regesetr the imported model







Now go back to the browser and you should get this result: You should see ,your memebers module

Click Members and see the five records we inserted earlier in this tutorial:


  Change Display
In the list in the screenshot above, we see "Member object (1)", "Member object (2)" etc.
which might not be the data you wanted to be displayed in the list.

It would be better to display "firstname" and "lastname" instead.

This can easily be done by changing some settings in the models.py and/or the admin.py files. You will learn more about this in the next chapter.





HERE IS HOW TO CUSTOMISE THE CHANGE THE DISPLAY OF THE MODELS IN THE ADMIN PANNEL
**************************************************************************************************************************************************

from django.contrib import admin
from . models import Member            // Here we import the models folder from the current folder i.e through the dot --> . //We import the memeber models.

# Register your models here.
admin.site.register(Member) 




Here the Memebrs will be displayed , by their default implementation.
To change this, we havve to go back to the memeber model class 
and overide the __str__ method. This method is clalled on every python object, when it is converted to a string. The original method is this          def __str__(self) -> str:
                                                                                                                                                           return super().__str__()

  This method returns by defaut a string , which is seen in the admin site,
  But we aer going to overide this method.        def __str__(self) -> str:
                                                      return self.title
  
  
class Memebr(models.Model):
    title = models.CharField(max_length =255)
    description = models.TextField()

    def __str__(self) -> str:
         return self.title



This will make the  Memeber objects be represented by their titles insted of defualt strings.

But our memebers are not oredered. Here we are going to define a middle class to order our memebers

class Memebr(models.Model):
    title = models.CharField(max_length =255)
    description = models.TextField()

    def __str__(self) -> str:
         return self.title

      
    class Meta:  
          ordering = ['title']    // This will order the goods based on their title.





HERE IS HOW TO CUSTOMISE THE ADMIN SITE
**************************************************************************************************************************************************

In the projects folder, Go to the Urls.py of the  project  


from django.contrib import admin
from django.urls import path,include
import debug_toolbar

admin.site.site_header = 'The Gacau Admin site'    // This Changes the site header title
admin.site.index_title = 'Kimani Ichungwa'         // This changes the index title header.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', include('stores.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]












































































































..
