QUERY METHODS
*******************************************************************************************************************************************


In Django, a manager is a class that encapsulates the database access logic for a particular model.
It provides methods for querying the database to retrieve, create, update, and delete records.

Some of the commonly used query methods in the manager in Django are:



all() - Returns all the records for the model.
filter() - Returns a QuerySet containing the records that match the specified criteria.
exclude() - Returns a QuerySet containing the records that do not match the specified criteria.
get() - Returns a single record that matches the specified criteria. Raises an exception if multiple records are found.
create() - Creates a new record with the specified data.
update() - Updates one or more records that match the specified criteria.
delete() - Deletes one or more records that match the specified criteria.
values() - Returns a QuerySet containing a subset of fields for each record.
order_by() - Returns a QuerySet containing the records sorted by one or more fields.
































































































.
