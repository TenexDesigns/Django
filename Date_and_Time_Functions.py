Django provides several built-in date and time functions to help developers work with date and time fields in their applications.
Some examples of these functions include:
  
  
  

DATE FUNCTIONS
*******************************************************************************************************************


Extract:
  Extracts a specific part of a date or datetime field, such as the year, month, or day.
  Extracts a specific component of a date or time field. 
  The available components depend on the database backend, but common components include year, month, day, hour, minute, and second. For example:


from django.db.models.functions import Extract
from myapp.models import MyModel

# Extract the year from a date field
year = MyModel.objects.annotate(year=Extract('date_field', 'year')).values('year')




DateField extracts:
  Extracts a specific part of a date field, such as the year, month, or day.
  Similar to Extract, but only works with DateField objects. Available components include year, month, and day. For example:

from django.db.models.functions import ExtractYear
from myapp.models import MyModel

# Extract the year from a date field
year = MyModel.objects.annotate(year=ExtractYear('date_field')).values('year')



DateTimeField extracts:
  Extracts a specific part of a datetime field, such as the year, month, or day.
  Similar to Extract, but only works with DateTimeField objects. 
  Available components include year, month, day, hour, minute, and second. For example:

from django.db.models.functions import ExtractHour
from myapp.models import MyModel

# Extract the hour from a datetime field
hour = MyModel.objects.annotate(hour=ExtractHour('datetime_field')).values('hour')




Now:
  Returns the current date and time.
  This function is similar to the Python datetime.now() function, but returns a timezone-aware datetime object. For example:


from django.utils import timezone

now = timezone.now()



Trunc:
  Truncates a date or datetime field to a specific granularity, such as year, month, or day.
  Truncates a date or time field to a specific precision. 
  The available precisions depend on the database backend, but common options include year, month, day, hour, minute, and second. For example:

from django.db.models.functions import Trunc
from myapp.models import MyModel

# Truncate a datetime field to the nearest hour
truncated = MyModel.objects.annotate(hour=Trunc('datetime_field', 'hour')).values('hour')






DateField truncation:
  Truncates a date field to a specific granularity, such as year, month, or day.
  Similar to Trunc, but only works with DateField objects. Available precisions include year, month, and day. For example:


from django.db.models.functions import TruncMonth
from myapp.models import MyModel

# Truncate a date field to the nearest month
truncated = MyModel.objects.annotate(month=TruncMonth('date_field')).values('month')





DateTimeField truncation:
  Truncates a datetime field to a specific granularity, such as year, month, or day.
  Similar to Trunc, but only works with DateTimeField objects.
  Available precisions include year, month, day, hour, minute, and second. For example:



from django.db.models.functions import TruncSecond
from myapp.models import MyModel

# Truncate a datetime field to the nearest second
truncated = MyModel.objects.annotate(second=TruncSecond('datetime_field')).values('second')




TimeField truncation:
  Truncates a time field to a specific granularity, such as hour, minute, or second.
  Similar to Trunc, but only works with TimeField objects. Available precisions include hour, minute, and second. For example:

from django.db.models.functions import TruncMinute
from myapp.models import MyModel

minute = MyModel.objects.annotate(minute=TruncMinute('time_field')).values('minute')




These functions can be used in combination with querysets to perform advanced filtering, aggregation, and annotation operations on date and time fields.









TIME FUNCTIONS
*******************************************************************************************************************


now():
  Returns the current date and time.
  
  from django.utils import timezone

current_time = timezone.now()


date():
  Returns the date part of a datetime field.
  
  
  
  from myapp.models import MyModel

date_field = MyModel.objects.values('datetime_field__date')




time():
  Returns the time part of a datetime field.
  
from myapp.models import MyModel

time_field = MyModel.objects.values('datetime_field__time')



year(): Returns the year part of a date field.
  
  from myapp.models import MyModel

year = MyModel.objects.values('date_field__year')



month(): Returns the month part of a date field.
  
  from myapp.models import MyModel

month = MyModel.objects.values('date_field__month')





day(): Returns the day part of a date field.
  
  from myapp.models import MyModel

day = MyModel.objects.values('date_field__day')



hour(): Returns the hour part of a time field.
  
  from myapp.models import MyModel

hour = MyModel.objects.values('time_field__hour')



minute(): Returns the minute part of a time field.
  
  from myapp.models import MyModel

minute = MyModel.objects.values('time_field__minute')



second(): Returns the second part of a time field.
  
  from myapp.models import MyModel

second = MyModel.objects.values('time_field__second')



These functions can be used in combination with querysets to filter and order objects based on date and time fields.









































..
