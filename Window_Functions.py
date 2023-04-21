Window functions are a powerful feature of SQL that allow us to perform aggregate calculations across a group of rows in a table, 
similar to the way that GROUP BY works, but with the added ability to perform calculations on a sliding window of rows.

In Django, we can use window functions by using the Window object provided by the django.db.models.functions module. 
Here are some examples of how to use window functions in Django:


  
CumeDist
****************************************************************************************************************************************************************

CumeDist calculates the cumulative distribution of a value in a result set.  
  
  In this example, were calculating the cumulative distribution of the value field in the MyModel table.
  
  from django.db.models import Window
from django.db.models.functions import CumeDist

queryset = MyModel.objects.annotate(
    cume_dist=Window(
        expression=CumeDist(),
        order_by='value'
    )
)

  
  
  
 FirstValue
****************************************************************************************************************************************************************


FirstValue returns the first value in a result set.
  
  In this example, were returning the first value in the MyModel table, based on the ascending order of the created_at field.
  
  from django.db.models import Window
from django.db.models.functions import FirstValue

queryset = MyModel.objects.annotate(
    first_value=Window(
        expression=FirstValue('value'),
        order_by='created_at'
    )
)

  
  
  Lag
****************************************************************************************************************************************************************
  
Lag returns the value from a row that is before the current row.

In this example, were returning the value from the preceding row in the MyModel table, based on the ascending order of the created_at field.
  
  from django.db.models import Window
from django.db.models.functions import Lag

queryset = MyModel.objects.annotate(
    previous_value=Window(
        expression=Lag('value'),
        order_by='created_at'
    )
)







LastValue
****************************************************************************************************************************************************************

LastValue returns the last value in a result set.

In this example, were returning the last value in the MyModel table, based on the ascending order of the created_at field.

from django.db.models import Window
from django.db.models.functions import LastValue

queryset = MyModel.objects.annotate(
    last_value=Window(
        expression=LastValue('value'),
        order_by='created_at'
    )
)




Lead
****************************************************************************************************************************************************************

Lead returns the value from a row that is after the current row.

In this example, were returning the value from the following row in the MyModel table, based on the ascending order of the created_at field.

from django.db.models import Window
from django.db.models.functions import Lead

queryset = MyModel.objects.annotate(
    next_value=Window(
        expression=Lead('value'),
        order_by='created_at'
    )
)





NthValue
****************************************************************************************************************************************************************

NthValue returns the value from the nth row in a result set.

In this example, were returning the value from the third row in the MyModel table, based on the ascending order of the created_at field.

from django.db.models import Window
from django.db.models.functions import NthValue

queryset = MyModel.objects.annotate(
    third_value=Window(
        expression=NthValue('value', 3),
        order_by='created_at'
    )
)





Ntile
****************************************************************************************************************************************************************

Ntile assigns an integer value to each row based on the number of partitions specified.

In this example, were assigning each row in the MyModel table to a quartile based on the value field.

from django.db.models import Window
from django.db.models.functions import Ntile

queryset = MyModel.objects.annotate(
    quartile=Window(
        expression=Ntile(4),
        order_by='value'
    )
)








PercentRank
****************************************************************************************************************************************************************
PercentRank calculates the percentile rank of a value in a result



 
  
  

ROW_NUMBER
****************************************************************************************************************************************************************

ROW_NUMBER assigns a unique integer to each row in the result set.
This can be useful for generating unique identifiers or for pagination.

In this example, were assigning a row_number to each row in the MyModel table, based on the descending order of the created_at field.


from django.db.models import Window, F
from django.db.models.functions import RowNumber

queryset = MyModel.objects.annotate(
    row_number=Window(
        expression=RowNumber(),
        order_by=F('created_at').desc()
    )
)






RANK
****************************************************************************************************************************************************************

RANK assigns a unique integer to each distinct value in a result set, with ties receiving the same rank and leaving gaps in the sequence.

In this example, were assigning a rank to each distinct value of the value field in the MyModel table, based on the descending order of the value field.

from django.db.models import Window, F
from django.db.models.functions import Rank

queryset = MyModel.objects.annotate(
    rank=Window(
        expression=Rank(),
        order_by=F('value').desc()
    )
)



DENSE_RANK
****************************************************************************************************************************************************************

DENSE_RANK is similar to RANK, but it does not leave gaps in the sequence.


from django.db.models import Window, F
from django.db.models.functions import DenseRank

queryset = MyModel.objects.annotate(
    dense_rank=Window(
        expression=DenseRank(),
        order_by=F('value').desc()
    )
)


In this example, were assigning a dense_rank to each distinct
value of the value field in the MyModel table, based on the descending order of the value field, without leaving gaps in the sequence.





SUM
****************************************************************************************************************************************************************

SUM calculates the sum of a specified field over a window.

from django.db.models import Window, F
from django.db.models.functions import Sum

queryset = MyModel.objects.annotate(
    running_total=Window(
        expression=Sum('value'),
        order_by=F('created_at').asc(),
        frame=Window.range(
            start=-1,  # include the current row
            end=0,  # include the current row
        ),
    )
)


In this example, were calculating the running total of the value field in the MyModel table,
based on the ascending order of the created_at field, using a window that includes the current row and the preceding row.




LEAD and LAG
****************************************************************************************************************************************************************

LEAD and LAG allow us to access values from rows that are ahead or behind the current row, respectively.


from django.db.models import Window, F
from django.db.models.functions import Lag, Lead

queryset = MyModel.objects.annotate(
    previous_value=Window(
        expression=Lag('value'),
        order_by=F('created_at').asc(),
    ),
    next_value=Window(
        expression=Lead('value'),
        order_by=F('created_at').asc(),
    ),
)


In this example, were accessing the value from the preceding row with Lag('value'), and from the following



















































































































































































....
