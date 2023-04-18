Views
***********************************************************************************************************************************************************
Django views are Python functions that takes http requests and returns http response, like HTML documents.

This view functions are request handlers , or in other frame works they are called,action

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.

There is a views.py in your members folder that looks like this:

  my_tennis_club/members/views.py:

                    from django.shortcuts import render

                    # Create your views here.




Find it and open it, and replace the content with this:

     my_tennis_club/members/views.py:

                       from django.shortcuts import render
                       from django.http import HttpResponse
          
          
          
                      # This is a view function that takes in a request i.e (the request between the brackets of the function) and returna a httpresponser
                       def members(request):
                          # Here we can  send data,  Pull data from database, Transform data and e.t.c
                            return HttpResponse("Hello world!")
                           # All views must return a httpresponse




Note: The name of the view does not have to be the same as the application.

I call it members because I think it fits well in this context.



This is a simple example on how to send a response back to the browser.

But how can we execute the view? Well, we must call the view via a URL. i.r map url's to views

You will learn about URLs in the next chapter.






































































































..
