In Django, you can customize your database schema using model metadata.
Model metadata is a set of options that you can use to define the behavior and structure of your models and database tables.
i.e We use the Meta cclass to custmise our database e.g to change the name of a table in your database


Here is a brief explanation of some of the most common model metadata options:
  
  
  app_label:
    This option specifies the name of the Django application that the model belongs to.
    By default, Django uses the name of the directory that contains the model file as the app label.
    
    
  base_manager_name: 
    This option specifies the name of the base manager that is used for the model. 
    By default, Django uses the objects manager for all models.  

db_table:
  This option specifies the name of the database table that the model corresponds to.
  By default, Django generates a table name based on the app label and model name.


db_table_comment:
  This option allows you to add a comment to the database table for documentation purposes.

db_tablespace:
  This option specifies the database tablespace to use for the model's database table.

default_manager_name: 
  This option specifies the name of the default manager that is used for the model.

default_related_name:
  This option specifies the default name to use for the reverse relation from another model to this model.

get_latest_by: 
  This option specifies the name of the field to use for getting the latest object of the model.

managed:
  This option specifies whether Django should create the database table for the model or not.

ordering:
  This option specifies the default ordering for the model.

permissions: 
  This option specifies the default permissions for the model.

proxy:
  This option specifies whether the model is a proxy model or not.

indexes: 
  This option specifies the indexes to create for the model's database table.

unique_together:
  This option specifies the fields that should be used to create a unique constraint on the model's database table.

index_together:
  This option specifies the fields that should be used to create a composite index on the model's database table.

constraints:
  This option allows you to define custom database constraints for the model's database table.

verbose_name:
  This option specifies the human-readable name for the model.

verbose_name_plural:
  This option specifies the plural name for the model.

  
  Heres an example of how to use some of these options:



class MyModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    
    class Meta:
        app_label = 'myapp'
        db_table = 'my_table'
        db_table_comment = 'This is my table'
        default_manager_name = 'my_manager'
        default_related_name = 'related_objects'
        get_latest_by = 'name'
        managed = True
        ordering = ['name', 'age']
        permissions = [('can_view', 'Can view MyModel')]
        proxy = False
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['age'], name='age_idx'),
        ]
        unique_together = [('name', 'age')]
        index_together = [('name', 'age')]
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
            models.UniqueConstraint(fields=['name'], name='unique_name'),
        ]
        verbose_name = 'My Object'
        verbose_name_plural = 'My Objects'

































































































































































































































































....
