To register models in Django, you need to create a file called admin.py within your Django app and import the models you want to register.

Here is an example of how to register a model:
  
  
  
  # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
      # HERE WE ARE GOING TO PUT THE MODEL ADMIN OPTIONS LIKE 
     list_display =['title','unit_price','id']
     list_editable = ['unit_price']
     list_per_page = 4
    pass



In this example, we are importing the MyModel model from the myapp.models module and then registering it with the 
admin site by using the @admin.register decorator. We are also creating a MyModelAdmin class that inherits from admin.ModelAdmin.
You can customize this class to add functionality such as custom form fields, custom validation, or custom views.



Once you have registered your models, you can access them through the Django admin site by navigating to the URL http://localhost:8000/admin/.
    You will be prompted to log in with a user account that has been granted admin privileges.
    Once you are logged in, you should be able to see your registered models and interact with them through the admin site.






THER ARE THE MODEL OPTIONSIN DJANGO
*****************************************************************************************************************************************

In Django, the ModelAdmin class provides several options that can be used to customize the behavior of the admin site for a particular model.
Here are some commonly used options with code samples:



1.list_display

This option is used to specify the fields to display in the list view of a model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')





2.list_filter

This option is used to specify the fields that can be used to filter the results in the list view of a model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)




3.search_fields

This option is used to specify the fields that can be used to search for a particular model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)




4.ordering

This option is used to specify the default ordering for a model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    ordering = ('-created_at',)




5.list_per_page

This option is used to specify the number of objects to display per page in the list view of a model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_per_page = 50




6.fields and exclude

These options are used to specify which fields should be displayed on the add/edit page of a model in the admin site. 
You can either use fields to explicitly list the fields to display or use exclude to specify fields to exclude.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price')
    # or
    # exclude = ('created_at',)



7.readonly_fields

This option is used to specify which fields should be read-only on the add/edit page of a model in the admin site.



# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)




8.date_hierarchy

This option is used to specify a date field that can be used to navigate through objects by day, month, or year in the list view of a model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'




9.inlines

This option is used to specify related models that should be edited inline with the parent model on the add/edit page in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel, RelatedModel

class RelatedModelInline(admin.TabularInline):
    model = RelatedModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    inlines = [RelatedModelInline]





10.actions

This option is used to specify custom actions that can be performed on one or more objects in the list view of a model in the admin site.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        # implementation of the custom action
        pass

    export_as_csv.short_description = 'Export selected objects as CSV'







11.raw_id_fields

This option is used to specify fields that should be displayed as raw IDs on the add/edit page of a model in the admin site. 
This is useful when you have a large number of related objects and dont want to load them all into a drop-down menu.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('related_model',)




12.autocomplete_fields

This option is used to specify fields that should be displayed as autocomplete inputs on the add/edit page of a model in the admin site. 
This is useful when you have a large number of related objects and want to provide a quick way to search for them.



# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('related_model',)




13.save_as

This option is used to add a "Save as new" button on the add/edit page of a model in the admin site, which allows you to create a copy of an existing object.


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    save_as = True



14.save_on_top

This option is used to add the save buttons at the top of the add/edit page of a model in the admin site, as well as at the bottom


# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    save_on_top = True



15.form

This option is used to specify a custom form to use for the add/edit page of a model in the admin site.

# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel
from myapp.forms import MyModelForm

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm



    
    
    
16.list_display_links
    
This option is used to specify which fields in the list view of a model in the admin site should be clickable to go to the edit page for that object. 
By default, the first field in the list_display is used as the link.
    
    
  # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_display_links = ('name',)
  
    
    
    
    
  17.list_filter
  
This option is used to add filters to the list view of a model in the admin site. The filter options are based on the type of the field being filtered.  

# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('created_at', 'category')

    
    
    
    
    
    18.search_fields
    
This option is used to specify fields that should be searched when using the search box in the list view of a model in the admin site.
    
  
  # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description')

    
    
   19.ordering
  
This option is used to specify the default ordering for objects in the list view of a model in the admin site. 
    
   # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    ordering = ('name',)
 
    
    
    20.list_per_page
    
This option is used to specify the number of objects to display per page in the list view of a model in the admin site.
    
    
    # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_per_page = 20

    
    
    
  21. actions
  
This option is used to add custom actions to the list view of a model in the admin site.
Actions are functions that perform some operation on selected objects. 
    
 # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status='published')
    make_published.short_description = 'Mark selected items as published'
   
    
    
    
   22. date_hierarchy
    
This option is used to add a date-based drilldown navigation by a field in the list view of a model in the admin site.
    
    
    
    # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    date_hierarchy = 'created_at'

    
    
    
    
   23. readonly_fields
    
This option is used to specify fields that should be read-only on the add/edit page of a model in the admin site.
    
    # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    readonly_fields = ('created_at',)

    
    
    
    
 24. exclude
  
This option is used to specify fields that should be excluded from the add/edit page of a model in the admin site.  
    
    # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    exclude = ('slug',)

    
    
 25.inlines

This option is used to specify related objects that should be edited inline on the add/edit page of a model in the admin site.   
    
    
   # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel, RelatedModel

class RelatedModelInline(admin.TabularInline):
    model = RelatedModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    inlines = [RelatedModelInline]
 
    
    
 26.  list_filter
  
This option is used to specify fields that should be used as filters in the list view of a model in the admin site. 
    
  
  # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('category',)

    
    
  27. list_select_related
  
This option is used to specify related objects that should be fetched in a single query when objects are displayed on the list view of a model in the admin site. 
    
    
    # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_select_related = ('category',)

    
    
    
    
   28. save_as
    
This option is used to add a "Save as new" button to the edit page of a model in the admin site,
which allows users to save a copy of an object with a new primary key.
    
    
    
    # myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    save_as = True

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














...
