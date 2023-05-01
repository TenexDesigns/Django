





@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
     list_display =['title','unit_price','id','inventory_status']
     list_editable = ['unit_price']
     list_per_page = 4
    
    
    def inventory_stattus(self,product)
        if product.inventory < 10:
           return 'Low'
        return 'OK'







For the inventoy staus to be ordered




@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
     list_display =['title','unit_price','id','inventory_status']
     list_editable = ['unit_price']
     list_per_page = 4
    
    @admin.display(ordering = 'inventory')
    def inventory_stattus(self,product)
        if product.inventory < 10:
           return 'Low'
        return 'OK'



















User

Adding computed columns to the django admine site


Adding computed columns to the Django admin site involves a few steps:

Define the computed property in your model.
Define a method on the ModelAdmin class that computes the value of the property.
Add the method to the list_display option of the ModelAdmin class.
Here's an example:



# myapp/models.py

from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()

    @property
    def total(self):
        return self.price * self.quantity




In this example, we have defined a total property that is computed as the product of the price and quantity fields.

Next, we need to define a method on the ModelAdmin class that computes the value of the total property:




# myapp/admin.py

from django.contrib import admin
from myapp.models import MyModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'total')

    def total(self, obj):
        return obj.total
    total.admin_order_field = 'total'  # Optional - allows sorting by total column





In this example, we have defined a total method on the MyModelAdmin class that takes an object of MyModel as input and returns the computed value of the total
property for that object. We have also added the total method to the list_display option of the MyModelAdmin class so that it will be displayed as a column
in the list view of the model in the admin site.

Note that we have also added an admin_order_field attribute to the total method, which allows the total column to be sorted in ascending or descending order.

Thats it! Now you should be able to see the computed total column in the list view of your model in the admin site.

























































































...
