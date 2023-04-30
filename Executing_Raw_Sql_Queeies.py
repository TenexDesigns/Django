
Django provides a powerful ORM (Object-Relational Mapping) that allows you to interact with the database using Python code.
However, there may be cases where you need to execute a raw SQL query in Django. This can be done using the django.db.connection object,
which represents the default database connection.

Heres an example of how to execute a raw SQL query in Django:


from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM myapp_mymodel WHERE id = %s", [1])
    row = cursor.fetchone()

    
    

In the above example, were using the with statement to create a cursor object and execute a SQL query. 
The cursor.execute() method takes two arguments - the SQL query string and a list of parameters.
The parameters are passed as a separate list to avoid SQL injection attacks.

After executing the query, we can use the cursor.fetchone() method to fetch the first row of the result set. 
You can also use other cursor methods like fetchall() and fetchmany() to fetch multiple rows.

Its important to note that executing raw SQL queries can be dangerous and can expose your application to SQL injection attacks.
You should always validate user input and escape any special characters before including them in your SQL queries. 
Its recommended to use the ORM provided by Django whenever possible, as it handles the escaping of special characters for you.




HERE IS MORE EXPLANATION
************************************************************************************************************************************************************

Performing raw SQL queries in Django can be done using the raw() manager method, which allows you to execute raw SQL queries that return model instances.
The method takes a raw SQL query, executes it, and returns a django.db.models.query.RawQuerySet instance.
This RawQuerySet instance can be iterated over like a normal QuerySet to provide object instances docs.djangoproject.com.

Heres an example of how to use the raw() method with a Person model:


class Person(models.Model):
    first_name = models.CharField(...)
    last_name = models.CharField(...)
    birth_date = models.DateField(...)

for p in Person.objects.raw('SELECT * FROM myapp_person'):
    print(p)





This example is equivalent to running Person.objects.all(). However, the raw() method provides more options that make it very powerful docs.djangoproject.com.

You can also manipulate raw queries by slicing the objects or using more complex queries.
For instance, you can limit the number of objects returned by slicing the objects:




sql = 'SELECT * FROM student_student'
SD_DATA = Student.objects.raw(sql)[:2]



This will return only the first two rows of the student_student table delftstack.com.

Keep in mind that no checking is done on the SQL statement passed to the raw() method.
Django expects that the statement will return a set of rows from the database but does nothing to enforce that.
If the query does not return rows, a (possibly cryptic) error will result django.readthedocs.io.

It is important to note that the raw() method should generally be your first option when you want to execute raw SQL queries,
as the structure of the raw query set class instance is very similar to the query set class instance.
This allows you to perform other actions in raw queries, such as indexing and slicing








































































































...
