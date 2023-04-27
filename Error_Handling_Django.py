Django Exceptions

An exception is an abnormal event that leads to program failure. 
To deal with this situation, Django uses its own exception classes and supports all core Python exceptions as well.

Django core exceptions classes are defined in django.core.exceptions module. This module contains the following classes.




AppRegistryNotReady:
  It is raised when attempting to use models before the app loading process.
  This error occurs when Djangos app registry is not ready yet, usually because the app has not finished loading. 
  To handle this error, you can catch it using a try-except block and return an appropriate error message to the user. 
  Heres an example:
    
  EXAMPLE:
    
    
    from django.apps import apps
from django.core.exceptions import AppRegistryNotReady
from django.http import HttpResponseServerError

def my_view(request):
    try:
        # Use app registry here
    except AppRegistryNotReady:
        apps.populate(settings.INSTALLED_APPS)
        # Try again
    except Exception:
        return HttpResponseServerError("Internal server error")




ObjectDoesNotExist:
  This error occurs when an object with the specified primary key or unique constraint does not exist in the database.
  To handle this error, you can catch it
  
  
  def getdata(request):  
    try:  
        data = Employee.objects.get(id=12)  
    except ObjectDoesNotExist:  
        return HttpResponse("Exception: Data not found")  
    return HttpResponse(data);  










EmptyResultSet: 
  If a query does not return any result, this exception is raised.
  This error occurs when a query returns an empty result set. It usually happens when the query is incorrect or the filters are too restrictive.
  To handle this error, you can catch it using a try-except block and return an appropriate error message to the user. Heres an example:
  
  EXAMPLE:
  
  from django.db.models import EmptyResultSet
from django.http import HttpResponseNotFound

def my_view(request):
    try:
        # Execute query here
    except EmptyResultSet:
        return HttpResponseNotFound("No matching records found")

  






FieldDoesNotExist: 
  It raises when the requested field does not exist.
  This error occurs when you try to access a field that does not exist in the model.
  To handle this error, you can catch it using a try-except block and return an appropriate error message to the user.
  Heres an example:
    
    
    from django.core.exceptions import FieldDoesNotExist
from django.http import HttpResponseBadRequest

def my_view(request):
    try:
        # Access field here
    except FieldDoesNotExist:
        return HttpResponseBadRequest("Field does not exist")





MultipleObjectsReturned: 
  This exception is raised by a query if only one object is expected, but multiple objects are returned.
  This error occurs when a query returns multiple objects when you expected only one. 
  To handle this error, you can catch it using a try-except block and return an appropriate error message to the user. 
  Heres an example:
    
    
    from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponseBadRequest

def my_view(request):
    try:
        # Execute query here
    except MultipleObjectsReturned:
        return HttpResponseBadRequest("Multiple objects found")






ViewDoesNotExist: 
  It is raised by django.urls when a requested view does not exist.
  This error occurs when you try to access a view that does not exist in the URL configuration.
  To handle this error, you can catch it using a try-except block and return an appropriate error message to the user.
  Heres an example:


from django.urls import Resolver404
from django.http import HttpResponseNotFound

def my_view(request):
    try:
        # Access view here
    except Resolver404:
        return HttpResponseNotFound("View does not exist")







MiddlewareNotUsed:
  It is raised when a middleware is not used in the server configuration.
  This error occurs when a middleware component is not used in the middleware stack. 
  To handle this error, you can check the middleware configuration in the MIDDLEWARE setting and add the missing middleware component.
  Heres an example:
    
    
    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'myapp.middleware.MyMiddleware',
    # ...
]



ImproperlyConfigured: 
  The ImproperlyConfigured exception is raised when Django is somehow improperly configured.
  This error occurs when theres a configuration error in Django, such as a missing setting or an invalid value. 
  To handle this error, you can check the error message and fix the configuration issue. 
  Heres an example:
    
    from django.core.exceptions import ImproperlyConfigured

def my_function():
    if not MY_SETTING:
        raise ImproperlyConfigured("












Django URL Resolver Exceptions
                                   
These exceptions are defined in django.urls module.
                                   
                                   
                                   
    
                                   
NoReverseMatch:
 This error occurs when Django cannot reverse the URL for a given view name or URL pattern.
 To handle this error, you can catch it using a try-except block and return an appropriate error message to the user. 
 Here's an example:
                                   
                                   
from django.urls import NoReverseMatch
from django.http import HttpResponseNotFound

def my_view(request):
    try:
        url = reverse('my_view_name')
    except NoReverseMatch:
        return HttpResponseNotFound("View not found")




Django Database Exceptions
                                   
The following exceptions are defined in django.db module.




DatabaseError:
   It occurs when the database is not available.
  This error occurs when theres an error while communicating with the database. 
  It can happen due to various reasons, such as a connection failure, a database server crash, or an invalid SQL query. To handle this error, you can catch it using a try-except block and return an appropriate error message to the user. 
  Heres an example:
                                   
From django.db import DatabaseError
from django.http import HttpResponseServerError

def my_view(request):
    try:
        # Execute SQL query here
    except DatabaseError:
        return HttpResponseServerError("Database error occurred")





IntegrityError: 
        This error occurs when there's a violation of the database's integrity constraints, such as a foreign key constraint or a unique constraint.
        To handle this error, you can catch it using a try-except block and return an appropriate error message to the user. Here's an example:
                                   
from django.db import IntegrityError
from django.http import HttpResponseBadRequest

def my_view(request):
    try:
        # Save object to the database here
    except IntegrityError:
        return HttpResponseBadRequest("Integrity constraint violation")






DataError:
  This error occurs when the data being stored in the database is too large or too small for the field 
  its being stored in. To handle this error, you can catch it using a try-except block and return an appropriate error message to the user.
  Heres an example:
                                   
from django.db import DataError
from django.http import HttpResponseBadRequest

def my_view(request):
    try:
        # Save object to the database here
    except DataError:
        return HttpResponseBadRequest("Invalid data size")












Django Http Exceptions
                                   
The following exceptions are defined in django.http module.
                                   
                                   
                                   


UnreadablePostError:
        It is raised when a user cancels an upload.
       This error occurs when Django cannot read the POST data from the request. 
       It usually happens when the form submission is malformed or the form data is too large.
      To handle this error, you can add a try-except block around the code that handles the POST request and return an appropriate error message to the user. Here's an example:


                                   
from django.http import HttpResponseBadRequest

def my_view(request):
    try:
        # Handle POST request here
    except UnreadablePostError:
        return HttpResponseBadRequest("Malformed form data")




Django Transaction Exceptions
                                   
The transaction exceptions are defined in django.db.transaction.

TransactionManagementError:	It is raised for any and all problems related to database transactions.



















































































































...
