Django QuerySet

A QuerySet is a collection of data from a database.

A QuerySet is built up as a list of objects.

QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data at an early stage.

In this tutorial we will be querying data from the Member table.



Member:

 id 	 firstname 	 lastname 	 phone 	 joined_date 
 1 	 Emil 	 Refsnes 	 5551234 	 2022-01-05 
 2 	 Tobias 	 Refsnes 	 5557777 	 2022-04-01 
 3 	 Linus 	 Refsnes 	 5554321 	 2021-12-24 
 4 	 Lene 	 Refsnes 	 5551234 	 2021-05-01 
 5 	 Stalikken 	 Refsnes 	 5559876 	 2022-09-29 






Querying Data

In views.py, we have a view for testing called testing where we will test different queries.

In the example below we use the .all() method to get all the records and fields of the Member model:






The object is placed in a variable called mydata, and is sent to the template via the context object as mymembers, and looks like this:

<QuerySet [
  <Member: Member object (1)>,
  <Member: Member object (2)>,
  <Member: Member object (3)>,
  <Member: Member object (4)>,
  <Member: Member object (5)>
]>





As you can see, our Member model contains 5 records, and are listed inside the QuerySet as 5 objects.

In the template you can use the mymembers object to generate content:

Template
templates/template.html:

<table border='1'>
  <tr>
    <th>ID</th>
    <th>Firstname</th>
    <th>Lastname</th>
  </tr>
  {% for x in mymembers %}
    <tr>
      <td>{{ x.id }}</td>
        <td>{{ x.firstname }}</td>
      <td>{{ x.lastname }}</td>
    </tr>
  {% endfor %}
</table>

















































































































...
