In the Urls file of your project.
We have the url patterns and the admin is importedd here.
We can make our customsationsitions to the admine page right here.



from django.contrib import admin    ----> This is the admin imported
from django.urls import path,include


urlpatterns = [
    path('cat/',include('store.urls')),
    path('admin/', admin.site.urls),
]




Here we can intercept the admin , and make changes to it like here We change the Header of the admin site.






from django.contrib import admin    ----> This is the admin imported
from django.urls import path,include

admin.site_site_header = 'Storefront Admin'   
admin.site.index_title = 'Admin'



urlpatterns = [
    path('cat/',include('store.urls')),
    path('admin/', admin.site.urls),
]










































































....
