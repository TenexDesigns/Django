Template Variables
In Django templates, you can render variables by putting them inside {{ }} brackets:



  templates/template.html:

<h1>Hello {{ firstname }}, how are you?</h1>




Create Variable in View
**************************************************************************************************************************************88
The variable firstname in the example above was sent to the template via a view:




views.py:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))






As you can see in the view above, we create an object named context and fill it with data, 
and send it as the first parameter in the template.render() function.







Create Variables in Template
**************************************************************************************************************************************88

You can also create variables directly in the template, by using the {% with %} template tag.

The variable is available until the {% endwith %} tag appears:


  
  views.py:

from django.http import HttpResponse
from django.template import loader

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'firstname': 'Linus',
  }
  return HttpResponse(template.render(context, request))




As you can see in the view above, we create an object named context and fill it with data,
and send it as the first parameter in the template.render() function.






Create Variables in Template
**************************************************************************************************************************************88

You can also create variables directly in the template, by using the {% with %} template tag.

The variable is available until the {% endwith %} tag appears:



  templates/template.html:

{% with firstname="Tobias" %}
<h1>Hello {{ firstname }}, how are you?</h1>
{% endwith %}


You will learn more about template tags in the next chapter.









Data From a Model
**************************************************************************************************************************************88

The example above showed a easy approach on how to create and use variables in a template.

Normally, most of the external data you want to use in a template, comes from a model.

We have created a model in the previous chapters, called Member, which we will use in many examples in the next chapters of this tutorial.

To get data from the Member model, we will have to import it in the views.py file, and extract data from it in the view:






members/views.py:

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))




Now we can use the data in the template:

templates/template.html:

<ul>
  {% for x in mymembers %}
    <li>{{ x.firstname }}</li>
  {% endfor %}
</ul>





We use the Django template tag {% for %} to loop through the members.

You will learn more about template tags in the next chapter.













































..
