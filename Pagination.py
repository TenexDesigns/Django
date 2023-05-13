Adding pagination

When you start adding content to your blog, you might easily reach the point where
tens or hundreds of posts are stored in your database. Instead of displaying all the
posts on a single page, you may want to split the list of posts across several pages.
This can be achieved through pagination. You can define the number of posts you
want to be displayed per page and retrieve the posts that correspond to the page
requested by the user. Django has a built-in pagination class that allows you to
manage paginated data easily.


Edit the views.py file of the blog application to import the Django paginator
classes and modify the post_list view, as follows:
  
  
  
  
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
def post_list(request):
object_list = Post.published.all()
paginator = Paginator(object_list, 3) # 3 posts in each page
page = request.GET.get('page')
try:
posts = paginator.page(page)
except PageNotAnInteger:
# If page is not an integer deliver the first page
posts = paginator.page(1)
except EmptyPage:
# If page is out of range deliver last page of results
posts = paginator.page(paginator.num_pages)
return render(request,
'blog/post/list.html',
{'page': page,
'posts': posts})



This is how pagination works:
  
1. You instantiate the Paginator class with the number of objects that you want
to display on each page.
2. You get the page GET parameter, which indicates the current page number.
3. You obtain the objects for the desired page by calling the page() method of
Paginator.
4. If the page parameter is not an integer, you retrieve the first page of results.
If this parameter is a number higher than the last page of results, you retrieve
the last page.
5. You pass the page number and retrieved objects to the template.


Now you have to create a template to display the paginator so that it can be
included in any template that uses pagination. In the templates/ folder of the blog
application, create a new file and name it pagination.html. Add the following
HTML code to the file:
<div class="pagination">
<span class="step-links">
{% if page.has_previous %}
<a href="?page={{ page.previous_page_number }}">Previous</a>
{% endif %}
<span class="current">
Page {{ page.number }} of {{ page.paginator.num_pages }}.
</span>
{% if page.has_next %}
<a href="?page={{ page.next_page_number }}">Next</a>
{% endif %}
</span>
</div>
The pagination template expects a Page object in order to render the previous and
next links, and to display the current page and total pages of results. Let's return to
the blog/post/list.html template and include the pagination.html template at
the bottom of the {% content %} block, as follows:
{% block content %}
...
{% include "pagination.html" with page=posts %}
{% endblock %}
Since the Page object you are passing to the template is called posts, you include
the pagination template in the post list template, passing the parameters to render
it correctly. You can follow this method to reuse your pagination template in the
paginated views of different models.
Building a Blog Application
[ 36 ]
Now open http://127.0.0.1:8000/blog/ in your browser. You should see
the pagination at the bottom of the post list and should be able to navigate
through pages

































































































































































































































































