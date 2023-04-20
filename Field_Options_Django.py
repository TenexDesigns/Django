Field options
************************************************************************************************************************************************************
The following arguments are available to all field types. All are optional.
 They are ---> NULL
               Blank
               Choises
      
      
      
      
NULL
************************************************************************************************************************************************************


Field.null¶

If True, Django will store empty values as NULL in the database. Default is False.

Avoid using null on string-based fields such as CharField and TextField.
If a string-based field has null=True, that means it has two possible values for “no data”: NULL,
  and the empty string. In most cases, it’s redundant to have two possible values for “no data;” 
  the Django convention is to use the empty string, not NULL. One exception is when a CharField has 
  both unique=True and blank=True set. In this situation, null=True is required to avoid unique constraint 
  violations when saving multiple objects with blank values.

For both string-based and non-string-based fields, you will also need to set blank=True if you wish to permit empty values in forms,
as the null parameter only affects database storage (see blank).







BLANK
************************************************************************************************************************************************************

Field.blank¶
If True, the field is allowed to be blank. Default is False.

Note that this is different than null. null is purely database-related, whereas blank is validation-related. 
If a field has blank=True, form validation will allow entry of an empty value. If a field has blank=False, the field will be required.




CHOISES
************************************************************************************************************************************************************

Field.choices¶
A sequence consisting itself of iterables of exactly two items (e.g. [(A, B), (A, B) ...]) to use as choices for this field. 
If choices are given, they’re enforced by model validation and the default form widget will be a select box with these choices instead of the standard text field.

The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. For example:

YEAR_IN_SCHOOL_CHOICES = [
    ("FR", "Freshman"),
    ("SO", "Sophomore"),
    ("JR", "Junior"),
    ("SR", "Senior"),
    ("GR", "Graduate"),
]
Generally, it’s best to define choices inside a model class, and to define a suitably-named constant for each value:

from django.db import models


class Student(models.Model):
    FRESHMAN = "FR"
    SOPHOMORE = "SO"
    JUNIOR = "JR"
    SENIOR = "SR"
    GRADUATE = "GR"
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, "Freshman"),
        (SOPHOMORE, "Sophomore"),
        (JUNIOR, "Junior"),
        (SENIOR, "Senior"),
        (GRADUATE, "Graduate"),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
Though you can define a choices list outside of a model class and then refer to it, defining the choices and names
for each choice inside the model class keeps all of that information with the class that uses it,
and helps reference the choices (e.g, Student.SOPHOMORE will work anywhere that the Student model has been imported).

************************************************************************************************************************************************************












HERE IS SOME MORE EXPLANATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In Django, a field is a class attribute that defines the type of data that a model attribute can hold.
There are several field options available in Django that can be used to customize the behavior of a field:



null - Allows null values to be stored in the database. By default, its set to False, which means the field cannot be empty.

blank - Allows the field to be empty. By default, its set to False, which means the field is required.

choices - Defines a list of choices for the field. The syntax is a tuple of tuples, where the first value is the actual value stored in the database, and the second value is the human-readable label.

default - Sets the default value for the field.

max_length - Sets the maximum length of the field. This is typically used for character fields.

unique - Ensures that each value in the field is unique.

verbose_name - Sets a human-readable name for the field.

help_text - Provides additional help text for the field.

auto_now - Automatically sets the field to the current date and time when the object is saved.

auto_now_add - Automatically sets the field to the current date and time when the object is created.

editable - Allows the field to be edited. By default, its set to True.

db_index - Creates an index for the field in the database, which can improve query performance.

upload_to - Specifies the directory where uploaded files should be stored.

related_name - Specifies the name of the reverse relation from the related model back to the model with the ForeignKey.

validators - A list of functions that are used to validate the field's value.

editable - A boolean that specifies whether the field should be editable in the admin interface.

verbose_name_plural - The plural name for the field.

db_column - The name of the database column for the field. If not specified, Django will use the name of the field.

db_tablespace - The name of the tablespace to use for the database table that holds the field.

db_collation - The collation to use for the database column.

db_constraint - A boolean that specifies whether a database constraint should be created for the field.

choices - A list of choices for the field. This is useful for fields that have a fixed set of options, such as gender or country.

blank - A boolean that specifies whether the field can be left blank.

null - A boolean that specifies whether the field can be null. If this is set to True, the field can be empty.

default - The default value for the field.

unique - A boolean that specifies whether the field's value must be unique.

help_text - Help text for the field.

validators - A list of validation functions that are run on the field's value.

auto_created - A boolean that specifies whether the field was automatically created by Django.
  
  
  
  These are some of the most common field options available in Django.
  However, there are many other options available, depending on the specific field type and use case.

















































































































...
