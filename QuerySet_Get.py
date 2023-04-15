Get Data
There are different methods to get data from a model into a QuerySet.

The values() Method
****************************************************************************************************************************************************

The values() method allows you to return each object as a Python dictionary, with the names and values as key/value pairs:




Example

views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))






Return Specific Columns
****************************************************************************************************************************************************

The values_list() method allows you to return only the columns that you specify.

Example
Return only the firstname columns:

views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.values_list('firstname')
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))






Return Specific Rows
****************************************************************************************************************************************************
You can filter the search to only return specific rows/records, by using the filter() method.

Example
Return only the records where firstname is 'Emil'

views.py:

from django.http import HttpResponse
from django.template import loader
from .models import Member

def testing(request):
  mydata = Member.objects.filter(firstname='Emil').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))







You will learn more about the filter() method in the next chapter.









































































































...
