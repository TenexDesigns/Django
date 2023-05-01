A custom model manager can be used to override the get_queryset function to always filter certain objects.
For example, a CustomManager can be created that filters out cancelled objects:


class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(canceled=False)

class MyModel(models.Model):
    objects = CustomManager()



When calling MyModel.objects.all(), it will always exclude cancelled objects.
A custom manager can be attached to another property, other than objects, to make queries more explicit and readable.




A model manager can be overridden in Django to add custom filtration methods.
A custom queryset can be created with custom methods.
The managers get_queryset method can be overridden to return the custom queryset.
The manager can be made to look for undefined methods in the queryset.



There are multiple approaches to overriding the base queryset in Django, and each has its pros and cons. Here are some possible approaches:

1.Custom model manager:
  A custom model manager can be created to override the get_queryset function to always filter certain objects. 
  This approach is simple and straightforward, and can be very effective for certain use cases. 
  However, it can also be limiting and inflexible, as it applies to all queries on the model.

2.Multiple managers:
  A model can have multiple managers, each with different querysets. 
  This approach is more flexible and allows for more fine-grained control over queries.
  However, it can also be more complex and difficult to manage, especially for larger projects.

3.Custom queryset: 
  A custom queryset can be created with custom methods, and the managers get_queryset method can be overridden to return the custom queryset. 
This approach allows for even more fine-grained control over queries, and can be very powerful for complex use cases.
However, it can also be more complex and difficult to manage, especially for larger projects.

4.Override get_queryset in model admin:
  To override the default queryset in Django admin,
  the get_queryset method can be overridden in the model admin. This approach is specific to Django admin, 
  and may not be applicable for other use cases. However, it can be a simple and effective solution for certain projects.

When choosing an approach to overriding the base queryset in Django, its important to consider the specific requirements and constraints of the project,
as well as the tradeoffs and implications of each approach.


















































































































...
