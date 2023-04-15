For Loops
A for loop is used for iterating over a sequence, like looping over items in an array, a list, or a dictionary.



Example
Loop through the items of a list:

{% for x in fruits %}
  <h1>{{ x }}</h1>
{% endfor %}






Example
Loop through a list of dictionaries:

{% for x in cars %}
  <h1>{{ x.brand }}</h1>
  <p>{{ x.model }}</p>
  <p>{{ x.year }}</p>
{% endfor %} 









Data From a Model
Data in a model is like a table with rows and columns.

The Member model we created earlier has five rows, and each row has three columns:

 id 	 firstname 	 lastname 	 phone 	 joined_date 
 1 	 Emil 	 Refsnes 	 5551234 	 2022-01-05 
 2 	 Tobias 	 Refsnes 	 5557777 	 2022-04-01 
 3 	 Linus 	 Refsnes 	 5554321 	 2021-12-24 
 4 	 Lene 	 Refsnes 	 5551234 	 2021-05-01 
 5 	 Stalikken 	 Refsnes 	 5559876 	 2022-09-29 
When we fetch data from the model, it comes as a QuerySet object, with a similar format as the cars example above: a list with dictionaries:



<QuerySet [
  {
    'id': 1,
    'firstname': 'Emil',
    'lastname': 'Refsnes',
    'phone': 5551234,
    'joined_date': datetime.date(2022, 1, 5)
  },
  {
    'id': 2,
    'firstname': 'Tobias',
    'lastname': 'Refsnes'
    'phone': 5557777,
    'joined_date': datetime.date(2021, 4, 1)
  },
  {
    'id': 3,
    'firstname': 'Linus',
    'lastname': 'Refsnes'
    'phone': 5554321,
    'joined_date': datetime.date(2021, 12, 24)
  },
  {
    'id': 4,
    'firstname': 'Lene',
    'lastname': 'Refsnes'
    'phone': 5551234,
    'joined_date': datetime.date(2021, 5, 1)
  },
  {
    'id': 5,
    'firstname': 'Stalikken',
    'lastname': 'Refsnes'
    'phone': 5559876,
    'joined_date': datetime.date(2022, 9, 29)
  }
]> 






Example
Loop through items fetched from a database:

{% for x in members %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %}











Reversed
The reversed keyword is used when you want to do the loop in reversed order.

Example
{% for x in members reversed %}
  <h1>{{ x.id }}</h1>
  <p>
    {{ x.firstname }}
    {{ x.lastname }}
  </p>
{% endfor %}  







Empty
The empty keyword can be used if you want to do something special if the object is empty.

Example
<ul>
  {% for x in emptytestobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul> 



The empty keyword can also be used if the object does not exist:

Example
<ul>
  {% for x in myobject %}
    <li>{{ x.firstname }}</li>
  {% empty %}
    <li>No members</li>
  {% endfor %}
</ul> 








Loop Variables
Django has some variables that are available for you inside a loop:

forloop.counter
forloop.counter0
forloop.first
forloop.last
forloop.parentloop
forloop.revcounter
forloop.revcounter0







forloop.counter
The current iteration, starting at 1.

Example
<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter }}</li>
  {% endfor %}
</ul>









forloop.counter0

The current iteration, starting at 0.

Example
<ul>
  {% for x in fruits %}
    <li>{{ forloop.counter0 }}</li>
  {% endfor %}
</ul> 












forloop.first

Allows you to test if the loop is on its first iteration.

Example
Draw a blue background for the first iteration of the loop:

<ul>
  {% for x in fruits %}
    <li
      {% if forloop.first %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul> 












forloop.last
Allows you to test if the loop is on its last iteration.

Example
Draw a blue background for the last iteration of the loop:

<ul>
  {% for x in fruits %}
    <li
      {% if forloop.last %}
        style='background-color:lightblue;'
      {% endif %}
    >{{ x }}</li>
  {% endfor %}
</ul> 








forloop.revcounter
The current iteration if you start at the end and count backwards, ending up at 1.

Example
<ul>
  {% for x in fruits %}
    <li>{{ forloop.revcounter }}</li>
  {% endfor %}
</ul> 







forloop.revcounter0
The current iteration if you start at the end and count backwards, ending up at 0.

Example
<ul>
  {% for x in fruits %}
    <li>{{ forloop.revcounter0 }}</li>
  {% endfor %}
</ul> 























































































































...
