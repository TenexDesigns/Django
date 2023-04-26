QuerySet Filter

The filter() method is used to filter your search, and allows you to return only the rows that matches the search term.

As we learned in the previous chapter, we can filter on field names like this:


NOTE-> THE OBJECTS TO BE APPLIED THIS QUERY SET METHODS COME FROM YOUR APPS MODELS FOLDER. FOR EXAMPLE IF YOUR APP IS CALLED STORE, AND IT HAS A MODEL CALLED MEMEBERS THEN YU CAN IMPORT IT LIKE THIS
from store.models import Product
Example

Return only the records where the firstname is 'Emil':
  from store.models import Product

mydata = Member.objects.filter(firstname='Emil').values()



In SQL, the above statement would be written like this:

SELECT * FROM members WHERE firstname = 'Emil';






AND
*************************************************************************************************************************************************************


The filter() method takes the arguments as **kwargs (keyword arguments), so you can filter on more than one field by separating them by a comma.



Example

Return records where lastname is "Refsnes" and id is 2:
  
  from store.models import Product

mydata = Member.objects.filter(lastname='Refsnes', id=2).values()




In SQL, the above statement would be written like this:

SELECT * FROM members WHERE lastname = 'Refsnes' AND id = 2;







OR
*************************************************************************************************************************************************************

To return records where firstname is Emil or firstname is Tobias (meaning: returning records that matches either query, 
not necessarily both) is not as easy as the AND example above.

We can use multiple filter() methods, separated by a pipe | character. The results will merge into one model.



Example

Return records where firstname is either "Emil" or Tobias":

mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()



Another common method is to import and use Q expressions:

Example
Return records where firstname is either "Emil" or Tobias":

from django.http import HttpResponse
from django.template import loader
from store.models import Member
from django.db.models import Q

def testing(request):
  mydata = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))





In SQL, the above statement would be written like this:

SELECT * FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';




Field Lookups
*************************************************************************************************************************************************************


Django has its own way of specifying SQL statements and WHERE clauses.

To make specific where clauses in Django, use "Field lookups".

Field lookups are keywords that represents specific SQL keywords.



Example:
Use the __startswith keyword:

.filter(firstname__startswith='L');
Is the same as the SQL statement:

WHERE firstname LIKE 'L%'
The above statement will return records where firstname starts with 'L'.



*************************************************************************************************************************************************************


In Django QuerySets, Field Lookups allow you to filter data based on specific fields of a model.
Heres the syntax for using Field Lookups in Django QuerySets:


  Model.objects.filter(field__lookup=value)

  
  In the above syntax, Model refers to the name of the model you want to query,
  field refers to the name of the specific field you want to filter on, 
  lookup is the type of comparison you want to make (e.g. "exact", "contains", "gte" for greater than or equal to),
  and value is the value you want to compare the field to.

Here are some examples of using Field Lookups in Django QuerySets:

Retrieve all instances of a model where the name field is "John":


Model.objects.filter(name__exact='John')


Retrieve all instances of a model where the age field is greater than or equal to 18:


  Model.objects.filter(age__gte=18)


Retrieve all instances of a model where the name field contains the substring "doe":


Model.objects.filter(name__contains='doe')


Retrieve all instances of a model where the created_at field is within a specific date range:


Model.objects.filter(created_at__range=[start_date, end_date])



These are just a few examples of the many Field Lookups you can use in Django QuerySets to filter data based on specific fields of a model.





Field Lookups Reference
*************************************************************************************************************************************************************

A list of all field look up keywords:

Keyword                                   	  Description

contains                                   		Contains the phrase
icontains	                                   	Same as contains, but case-insensitive
date	                                   	    Matches a date
day	                                        	Matches a date (day of month, 1-31) (for dates)
endswith	                                   	Ends with
iendswith                                    	Same as endswidth, but case-insensitive
exact                                    		  An exact match
iexact                                   		  Same as exact, but case-insensitive
in	                                   	      Matches one of the values
isnull                                   		  Matches NULL values
gt	                                   	      Greater than
gte                                   		    Greater than, or equal to
hour                                    		  Matches an hour (for datetimes)
lt                                   		      Less than
lte                                   		    Less than, or equal to
minute                                   		  Matches a minute (for datetimes)
month                                   		  Matches a month (for dates)
quarter                                   		Matches a quarter of the year (1-4) (for dates)
range                                   		  Match between
regex                                   		  Matches a regular expression
iregex                                   		  Same as regex, but case-insensitive
second                                   		  Matches a second (for datetimes)
startswith                                   	Starts with
istartswith                                   Same as startswith, but case-insensitive
time                                   		    Matches a time (for datetimes)
week                                   		    Matches a week number (1-53) (for dates)
week_day                                   		Matches a day of week (1-7) 1 is sunday
iso_week_day                                 	Matches a ISO 8601 day of week (1-7) 1 is monday
year	                                      	Matches a year (for dates)
iso_year                                   		Matches an ISO 8601 year (for dates)




in the above context, provide A list of all field look up keywords, with code samples
*************************************************************************************************************************************************************


Sure, heres a list of some common Field Lookups in Django QuerySets along with code samples:

exact - Filters objects where the value of the field exactly matches the specified value.
Model.objects.filter(name__exact='John')




iexact - Filters objects where the value of the field exactly matches the specified value, but case-insensitive.
Model.objects.filter(name__iexact='john')



contains - Filters objects where the value of the field contains the specified value.
Model.objects.filter(name__contains='doe')



icontains - Filters objects where the value of the field contains the specified value, but case-insensitive.
Model.objects.filter(name__icontains='DOE')



startswith - Filters objects where the value of the field starts with the specified value.
Model.objects.filter(name__startswith='J')



istartswith - Filters objects where the value of the field starts with the specified value, but case-insensitive.
Model.objects.filter(name__istartswith='j')



endswith - Filters objects where the value of the field ends with the specified value.
Model.objects.filter(name__endswith='n')



iendswith - Filters objects where the value of the field ends with the specified value, but case-insensitive.
Model.objects.filter(name__iendswith='N')



gt - Filters objects where the value of the field is greater than the specified value.
Model.objects.filter(age__gt=18)



gte - Filters objects where the value of the field is greater than or equal to the specified value.
Model.objects.filter(age__gte=18)





lt - Filters objects where the value of the field is less than the specified value.
Model.objects.filter(age__lt=18)



lte - Filters objects where the value of the field is less than or equal to the specified value.
Model.objects.filter(age__lte=18)





range - Filters objects where the value of the field is within the specified range.
Model.objects.filter(age__range=[18, 25])



in - Filters objects where the value of the field is in the specified list.
Model.objects.filter(name__in=['John', 'Jane', 'Bob'])






isnull - Filters objects where the value of the field is null.
Model.objects.filter(name__isnull=True)






regex - Filters objects where the value of the field matches the specified regular expression.
Model.objects.filter(name__regex=r'^(J|B).*n$')

We can also use the table names in our model
---------------------------------------------------------------------------------------------------


products = Product.objects.filter(collection__id =1)   -- This Gets the collection whose id is one


products = Product.objects.filter(collection__id__range =(3:9))   -- This Gets the collection whose id is between the range of 3 to 9




These are just some of the many Field Lookups available in Django QuerySets. For a complete list of available lookups, you can refer to the Django documentation.


























































































..
