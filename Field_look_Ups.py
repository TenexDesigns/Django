In Django, field lookups are used to perform queries against a database to retrieve specific data.
Field lookups are typically used in conjunction with querysets, which represent a collection of objects from a particular database table.

There are many field lookups available in Django, including:




Exact lookup:
  This lookup returns objects where the value of a field exactly matches the specified value. Example: MyModel.objects.filter(name__exact='John')

Contains lookup: 
  This lookup returns objects where the value of a field contains the specified value. Example: MyModel.objects.filter(name__contains='John')

StartsWith lookup:
  This lookup returns objects where the value of a field starts with the specified value. Example: MyModel.objects.filter(name__startswith='J')

EndsWith lookup:
  This lookup returns objects where the value of a field ends with the specified value. Example: MyModel.objects.filter(name__endswith='n')

GreaterThan lookup: 
  This lookup returns objects where the value of a field is greater than the specified value. Example: MyModel.objects.filter(age__gt=18)

LessThan lookup:
  This lookup returns objects where the value of a field is less than the specified value. Example: MyModel.objects.filter(age__lt=30)

In lookup:
  This lookup returns objects where the value of a field is in the specified list of values. Example: MyModel.objects.filter(name__in=['John', 'Mary'])

Range lookup:
  This lookup returns objects where the value of a field is within the specified range of values. Example: MyModel.objects.filter(age__range=(18, 30))


iexact lookup: 
  This lookup performs a case-insensitive exact match of a field. Example: MyModel.objects.filter(name__iexact='john')

icontains lookup:
  This lookup performs a case-insensitive containment match of a field. Example: MyModel.objects.filter(name__icontains='john')

istartswith lookup:
  This lookup performs a case-insensitive match for fields that start with a specified value. Example: MyModel.objects.filter(name__istartswith='j')

iendswith lookup: 
  This lookup performs a case-insensitive match for fields that end with a specified value. Example: MyModel.objects.filter(name__iendswith='n')

regex lookup:
  This lookup performs a regular expression match on a field. Example: MyModel.objects.filter(name__regex=r'^J.*n$')

isnull lookup:
  This lookup returns objects where the value of a field is null or not null. Example: MyModel.objects.filter(name__isnull=True)

date lookup:
  This lookup returns objects where the value of a date field matches a specified date. Example: MyModel.objects.filter(date_field__date=date(2022, 1, 1))

year lookup: 
  This lookup returns objects where the year of a date field matches a specified year. Example: MyModel.objects.filter(date_field__year=2022)

month lookup: 
  This lookup returns objects where the month of a date field matches a specified month. Example: MyModel.objects.filter(date_field__month=1)

day lookup: 
  This lookup returns objects where the day of a date field matches a specified day. Example: MyModel.objects.filter(date_field__day=1)



year__range lookup:
  This lookup returns objects where the year of a date field is within a specified range. Example: MyModel.objects.filter(date_field__year__range=(2010, 2022))

week_day lookup:
  This lookup returns objects where the day of the week of a date field matches a specified day. Example: MyModel.objects.filter(date_field__week_day=1)

time lookup: 
  This lookup returns objects where the value of a time field matches a specified time. Example: MyModel.objects.filter(time_field__time=time(12, 0))

hour lookup: 
  This lookup returns objects where the hour of a time field matches a specified value. Example: MyModel.objects.filter(time_field__hour=12)

minute lookup: 
  This lookup returns objects where the minute of a time field matches a specified value. Example: MyModel.objects.filter(time_field__minute=30)

second lookup:
  This lookup returns objects where the second of a time field matches a specified value. Example: MyModel.objects.filter(time_field__second=0)

isnumeric lookup:
  This lookup returns objects where the value of a field is numeric. Example: MyModel.objects.filter(age__isnumeric=True)

len lookup:
  This lookup returns objects where the length of a field matches a specified value. Example: MyModel.objects.filter(name__len=4)

ForeignKey lookup:
  This lookup returns objects related to a specific foreign key field. Example: MyModel.objects.filter(foreign_key_field__id=1)

































































































































...
