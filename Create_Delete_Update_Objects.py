In Django, creating, updating, and deleting objects in the database is done through the models defined in your application.
Here are some examples of how to perform these operations using Django's built-in models API:

Creating Objects:

To create an object in the database, you can simply instantiate a new object and call its save() method. For example:
  
  In this example, we create a new instance of MyModel and set its fields. Then we call the save() method to save the object to the database.
 After calling the save methos, The created object is return to the obj.

from myapp.models import MyModel



method 1   --> This is a more recommeneded  method due to the intereecece i.e "obj. field" . It shows you the fields need to be field
obj = MyModel() 
# obj.field1 = 'value 1'
# obj.field2 = 'value 2' 
#obj.featured_product = Product(pk=1)
# obj.save()

Method 2
obj = MyModel(field1='value1', field2='value2')  




Method 3   --> This one takes less code to write.
#obj = MyModel() 
#obj.object.create(field1='value 1', field2= 'value 2')
obj.save()







Updating Objects:

To update an existing object, you can retrieve it from the database, update its fields, and then call the save() method. For example:
  
  In this example, we retrieve an existing object with a primary key of 1. We then update its fields and call the save() method to save the changes to the database.


from myapp.models import MyModel

# retrieve an existing object
obj = MyModel.objects.get(pk=1)

# update its fields
obj.field1 = 'new_value1'
obj.field2 = 'new_value2'

# save the changes to the database
obj.save()

#Method 2  --> USed insted of the above method becuase it consumes less memory
# Tis method searches the database for the object with the given id and only updates the specified field.
Mymodel.object.filter(pk=1).update(field1='new_value1')



Deleting Objects:

To delete an object from the database, you can retrieve it from the database and call its delete() method. For example:

from myapp.models import MyModel

# retrieve an existing object
obj = MyModel.objects.get(pk=1)

# delete the object
obj.delete()







In this example, we retrieve an existing object with a primary key of 1. We then call its delete() method to remove the object from the database.

Its worth noting that Django also provides several other methods for creating, updating, and deleting objects, 
such as create() for creating a new object and saving it in a single step, 
and update() for updating multiple objects in a single query.
Additionally, you can use Djangos bulk_create() and bulk_update() methods to create or update multiple objects at once,
which can be much faster than performing individual queries.



HERE IS MORE EXPLANATION
**************************************************************************************************************************************************************
In Django, you can perform CRUD operations (Create, Retrieve, Update, and Delete) using the database-abstraction API provided by the framework.
This allows you to interact with the database in a Pythonic way.
Based on the example models you provided (Blog, Author, and Entry), I will explain how to perform each CRUD operation.




Creating objects

To create an object, instantiate the model class using keyword arguments and then call the save() method to save it to the database. Alternatively, you can use the create() method to create and save an object in a single step.

Example:



from blog.models import Blog

# Using save()
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()

# Using create()
b = Blog.objects.create(name="Beatles Blog", tagline="All the latest Beatles news.")






Retrieving objects

To retrieve objects from the database, you can use the filter() and get() methods on a Manager (e.g., objects). filter() returns a QuerySet, while get() returns a single object directly.

Example:


# Retrieve all Blog objects
all_blogs = Blog.objects.all()

# Retrieve Blog objects with a specific name
beatles_blogs = Blog.objects.filter(name="Beatles Blog")

# Retrieve a single Blog object with a specific primary key (pk)
one_blog = Blog.objects.get(pk=1)







Updating objects

To update an object that's already in the database, modify its attributes and then call the save() method.

Example:




# Assuming b is a Blog instance that has already been saved to the database
b.name = "New name"
b.save()



Deleting objects

To delete an object, call the delete() method on the instance. You can also delete objects in bulk using the delete() method on a QuerySet.

Example:

# Delete a single Blog instance
b.delete()

# Delete all Blog instances with a specific name
Blog.objects.filter(name="Beatles Blog").delete()

# Delete all Blog instances
Blog.objects.all().delete()


#To filter and delete onjects that meet a specified condition
Blog.objects.filter(id_gt=5).delete()



Keep in mind that when you delete an object, Django emulates the behavior of the SQL constraint ON DELETE CASCADE by default.
This means that any objects with foreign keys pointing to the
deleted object will also be deleted. This behavior is customizable using the on_delete argument of the ForeignKey field.

















































































































,..
