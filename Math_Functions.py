Django provides several mathematical functions to perform advanced calculations on numeric fields in querysets. Here are some examples:


Abs: Returns the absolute value of a numeric field.

ACos: Returns the arc cosine of a numeric field in radians.

ASin: Returns the arc sine of a numeric field in radians.

ATan: Returns the arc tangent of a numeric field in radians.

ATan2: Returns the arc tangent of two numeric fields in radians.

Ceil: Returns the smallest integer greater than or equal to a numeric field.

Cos: Returns the cosine of a numeric field in radians.

Cot: Returns the cotangent of a numeric field in radians.

Degrees: Converts a numeric field from radians to degrees.

Exp: Returns e raised to the power of a numeric field.

Floor: Returns the largest integer less than or equal to a numeric field.

Ln: Returns the natural logarithm of a numeric field.

Log: Returns the logarithm of a numeric field to a specified base.

Mod: Returns the remainder of a numeric field divided by another numeric field.

Pi: Returns the mathematical constant pi.

Power: Returns the value of a numeric field raised to a specified power.

Radians: Converts a numeric field from degrees to radians.

Random: Returns a random number between 0 and 1.

Round: Returns a numeric field rounded to a specified number of decimal places.

Sign: Returns the sign of a numeric field (-1, 0, or 1).

Sin: Returns the sine of a numeric field in radians.

Sqrt: Returns the square root of a numeric field.

Tan: Returns the tangent of a numeric field in radians.






Abs: 
  Returns the absolute value of a numeric field.
  
  from django.db.models import F, Value
from django.db.models.functions import Abs

# returns the absolute value of the 'quantity' field
qs = MyModel.objects.annotate(abs_quantity=Abs('quantity'))

  
  

ACos:
  Returns the arc cosine of a numeric field in radians.
  
  
  from django.db.models import F, Value
from django.db.models.functions import ACos

# returns the arc cosine of the 'value' field in radians
qs = MyModel.objects.annotate(arc_cosine=ACos('value'))
 
    
  

ASin:
  Returns the arc sine of a numeric field in radians.
    
  from django.db.models import F, Value
from django.db.models.functions import ASin

# returns the arc sine of the 'value' field in radians
qs = MyModel.objects.annotate(arc_sine=ASin('value'))

  
  
  
  
  
  

ATan: 
  Returns the arc tangent of a numeric field in radians.
    
  from django.db.models import F, Value
from django.db.models.functions import ATan

# returns the arc tangent of the 'value' field in radians
qs = MyModel.objects.annotate(arc_tangent=ATan('value'))

  
  
  
  
  
  

ATan2: 
  Returns the arc tangent of two numeric fields in radians.
    
  from django.db.models import F, Value
from django.db.models.functions import ATan2

# returns the arc tangent of the 'x' and 'y' fields in radians
qs = MyModel.objects.annotate(arc_tangent=ATan2('y', 'x'))

  
  
  
  
  
  

Ceil:
  Returns the smallest integer greater than or equal to a numeric field.
    
  
  from django.db.models import F, Value
from django.db.models.functions import Ceil

# returns the smallest integer greater than or equal to the 'value' field
qs = MyModel.objects.annotate(ceil_value=Ceil('value'))

  
  
  
  
  
  

Cos:
  Returns the cosine of a numeric field in radians.
    
  
  from django.db.models import F, Value
from django.db.models.functions import Cos

# returns the cosine of the 'value' field in radians
qs = MyModel.objects.annotate(cosine=Cos('value'))

  
  
  
  
  

Cot: 
  Returns the cotangent of a numeric field in radians.
    
  from django.db.models import F, Value
from django.db.models.functions import Cot

# returns the cotangent of the 'value' field in radians
qs = MyModel.objects.annotate(cotangent=Cot('value'))

  
  
  
  
  
  

Degrees:
  Converts a numeric field from radians to degrees.
    
  
  from django.db.models import F, Value
from django.db.models.functions import Degrees

# converts the 'value' field from radians to degrees
qs = MyModel.objects.annotate(degrees=Degrees('value'))

  
  
  
  
  

Exp: 
  Returns e raised to the power of a numeric field.
    
  from django.db.models import F, Value
from django.db.models.functions import Exp

# returns e raised to the power of the 'value' field
qs = MyModel.objects.annotate(exp_value=Exp('value'))

  
  
  
  
  
  

Floor:
  Returns the largest integer less than or equal to a numeric field.
    
  from django.db.models import F, Value
from django.db.models.functions import Floor

# returns the largest integer less than or equal to the 'value' field
qs = MyModel.objects.annotate(floor_value=Floor('value'))

  
  
  
  
  
  

Ln:
  Returns the natural logarithm of a numeric field.
    
  from django.db.models import F, Value
from django.db.models.functions import Ln

# returns the natural logarithm of the 'value' field
qs = MyModel.objects.annotate(ln_value=Ln('value'))

  
  
  
  
  
  
   

Log:
  Returns the logarithm of a numeric field to a specified base.
    
  from django.db.models import F, Value
from django.db.models.functions import Log

# returns the logarithm of the 'value' field to base 10
qs = MyModel.objects.annotate(log_value=Log('value', 10))
``

  
  
  
  
  
  

Mod:
  Returns the remainder of a numeric field divided by another numeric field.
    

  
  
  
  
  
  

Pi: 
  Returns the mathematical constant pi.
    
  
  
  
  
  
  
  

Power:
  Returns the value of a numeric field raised to a specified power.
    
  
  
  
  
  
  
  

Radians:
  Converts a numeric field from degrees to radians.
    
  
  
  
  
  
  
  

Random:
  Returns a random number between 0 and 1.
    
  
  
  
  
  
  
  

Round:
  Returns a numeric field rounded to a specified number of decimal places.
    
  
  
  
  
  
  
  

Sign: 
  Returns the sign of a numeric field (-1, 0, or 1).
    
  
  
  
  
  
  
  

Sin: 
  Returns the sine of a numeric field in radians.
    
  
  
  
  
  
  
  

Sqrt:
  Returns the square root of a numeric field.
    
  
  
  
  
  
  
  

Tan: 
  Returns the tangent of a numeric field in radians.







































































































































...
