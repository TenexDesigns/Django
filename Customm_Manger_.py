In Django, you can define custom managers for your models to encapsulate common querysets and methods.
A custom manager is a class that inherits from models.Manager and can provide custom querysets and methods to your model.

Heres an example of how to define a custom manager for a model:



from django.db import models

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(published=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    
    objects = models.Manager()
    published_objects = PublishedManager()




In this example, the PublishedManager class inherits from models.Manager and overrides the get_queryset() method to return only published books.
The Book model defines two manager instances: objects and published_objects. 
  The default manager instance objects is the default manager for the model and provides the default queryset for the model.
  The published_objects manager instance is the custom manager we defined and provides a queryset of only published books.

To use the custom manager, you can call the objects or published_objects manager instance on the model:



published_books = Book.published_objects.all()



This will return a queryset of only published books.

You can define other methods in your custom manager to provide additional functionality.
For example, you can define a method that returns the average rating of books:


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset()
        
    def average_rating(self):
        return self.get_queryset().aggregate(models.Avg('rating'))
        
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    
    objects = BookManager()






In this example, we defined a custom method average_rating() in the BookManager class. 
This method calculates the average rating of all books in the queryset.

To use this custom method, you can call it on the objects manager instance:


average_rating = Book.objects.average_rating()


This will return the average rating of all books.




































































































...
