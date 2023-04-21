EXPRESSION class- Is the base class for all types of expressions. Deriviteves of this class are the following.

    ----> Value() - For representing single values like booleans,number and string.
    ----> F ()  - For referencing fields
    ----> Func () - For calling database functions
    ----> Aggregate() - Which is the base class for all aggregate classes. e.g sum, count and so on.
    ----> Expression wrapper () We use this class when building complex expressions.




HERE IS MORE EXPLANATION
***************************************************************************************************************************

In Django, Query Expressions are used to perform complex queries on the database. 
They allow you to combine different conditions and operations together to build a query that retrieves the data you need.
Here are some examples of the different types of Query Expressions in Django:



Expression wrapper:
  This is used to wrap a value or expression in a specific type of expression.
  It can be used to perform operations like addition, subtraction, multiplication, etc. on database fields.


from django.db.models import F, ExpressionWrapper

# Example: adding two fields together
queryset = MyModel.objects.annotate(
    total=ExpressionWrapper(F('field_one') + F('field_two'), output_field=models.FloatField())
)



Value():
  This is used to wrap a value and create a constant expression that can be used in queries.


from django.db.models import Value

# Example: filtering by a specific value
queryset = MyModel.objects.filter(status=Value('active'))





F():
  This is used to reference a database field in a query expression.
  
  from django.db.models import F

# Example: updating a field based on another field
queryset = MyModel.objects.update(field_one=F('field_two'))





Func(): 
  This is used to call database functions in a query expression.

from django.db.models import Func

# Example: using the substring function to extract a part of a field
queryset = MyModel.objects.annotate(
    substring=Func(F('field_one'), Value(2), Value(4), function='SUBSTRING')
)




Aggregate():
  
 This is used to perform aggregate operations on a set of values, such as sum, count, average, etc.

from django.db.models import Sum

# Example: calculating the total value of a field
queryset = MyModel.objects.aggregate(total_value=Sum('field_one'))






Note that in all these examples, MyModel is the name of the Django model you are working with. 
Also, the annotate() method is used to add the calculated field to the queryset, 
while filter() is used to narrow down the queryset based on a condition. 
The update() method is used to modify the values of the selected fields in the queryset.







HERE IS MORE EXPLANATION
***************************************************************************************************************************


In Django, Query Expressions describe a value or a computation that can be used as part of a filter, order by, annotation, or
aggregate. They allow you to perform complex calculations and transformations on your data using the database, rather than Python.
Some of the built-in expressions include ExpressionWrapper, Value, F, Func, and Aggregate







ExpressionWrapper

ExpressionWrapper is used to wrap an expression and define the output field type.
It is useful when you want to perform a calculation that involves fields of different types,
or when Django cannot automatically determine the output type


Example:

from django.db.models import ExpressionWrapper, F, IntegerField
from .models import Enrollment

sem_score = Enrollment.objects.all().update(
    sem_score=ExpressionWrapper(
        (F("prelim_score") + F("midterm_score") + F("final_score")) / 3,
        output_field=IntegerField(),
    )
)




Value
Value is used to represent a value in a query expression. 
It can be used in combination with other expressions to perform calculations or transformations.

Example:




from django.db.models import Value, F
from .models import Product

discounted_price = Product.objects.annotate(
    discounted_price=F("price") - Value(5)
)



F

F expressions allow you to reference a fields value in an expression without evaluating it in Python. 
This can result in performance improvements, as the expression is executed by the database, not in-memory by Python stackoverflow.com.

Example:


from django.db.models import F
from .models import Product

discounted_products = Product.objects.filter(price=F("discounted_price") + 5)



Func
Func is a generic expression that can be used to call any database function. 
You can use it to perform calculations, transformations, or other operations using built-in or custom database functions act.moveon.org.

Example:


from django.db.models import Func, F
from .models import Product

class Concat(Func):
    function = 'CONCAT'

full_name = Product.objects.annotate(
    full_name=Concat(F('first_name'), Value(' '), F('last_name'))
)






Aggregate

Aggregate expressions are used to perform aggregations on a set of rows. 
They can be used with the annotate or aggregate methods of a queryset to return aggregated values act.moveon.org.

Example:


from django.db.models import Count
from .models import Author

author_book_count = Author.objects.annotate(book_count=Count('books'))




Keep in mind that QuerySets are lazy, meaning they dont do anything until they are evaluated. 
Expressions like F and ExpressionWrapper are for defining expressions that are executed by the database,
rather than in-memory by Python. The expression evaluation takes place strictly on the database, not in Python























...
