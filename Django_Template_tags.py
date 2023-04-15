Django Template Tags



Template Tags
********************************************************************************************************************************
In Django templates, you can perform programming logic like executing if statements and for loops.

These keywords, if and for, are called "template tags" in Django.

To execute template tags, we surround them in {% %} brackets.



templates/template.html:

{% if greeting == 1 %}
  <h1>Hello</h1>
{% else %}
  <h1>Bye</h1>
{% endif %}




Django Code

The template tags are a way of telling Django that here comes something else than plain HTML.

The template tags allows us to to do some programming on the server before sending HTML to the client.




templates/template.html:

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>




In the next chapters you will learn about the most common template tags.



Tag Reference
A list of all template tags:
                                             
Tag                                             	Description

autoescape                                        Specifies if autoescape mode is on or off
block                                             Specifies a block section
comment                                           Specifies a comment section
csrf_token	                                      Protects forms from Cross Site Request Forgeries
cycle                                             Specifies content to use in each cycle of a loop
debug                                             Specifies debugging information
extends                                           Specifies a parent template
filter	                                          Filters content before returning it
firstof	                                          Returns the first not empty variable
for                                             	Specifies a for loop
if                                              	Specifies a if statement
ifchanged                                         Used in for loops. Outputs a block only if a value has changed since the last iteration
include                                           Specifies included content/template
load	                                            Loads template tags from another library
lorem                                             Outputs random text
now	                                              Outputs the current date/time
regroup	                                          Sorts an object by a group
resetcycle	                                      Used in cycles. Resets the cycle
spaceless	                                        Removes whitespace between HTML tags
templatetag	                                      Outputs a specified template tag
url	Returns                                       the absolute URL part of a URL
verbatim                                          Specifies contents that should not be rendered by the template engine
widthratio                                        Calculates a width value based on the ratio between a given value and a max value
with	                                            Specifies a variable to use in the block
















































































































....
