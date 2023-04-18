****************************************************************************************************************************************************88

Sometimes we want to limit  the list of values that can be stored in a field.
For example in the code below, We create a column called memebership in our table .
This column will accept three values S,G,P  for S-> Silver, G -> Gold, P -> PLatnum
How can we limit the number of choises in t eh menbership column to only three.


FOR EXAMPLE.

class Product(models.Model):
      membership = models.CharField(max_length=1)





****************************************************************************************************************************************************88
The above solution limits the number of choises we have for entering into the memebership column.



All fileds in django share the Fied.Choises option
To create the field.choises option we create array of tuples.
This tuples will contains two values e.g  [('FR','Freshman'),
                                        ('JR', 'Junior'),
                                        ('SR','Senior')
                                       ]

The first value , is the actual value we arestoring in the database. And the second value is a human readable explanation of the first vaues

The above solution limits the number of choises we have for entering into the memebership column.





HERE IS HOW WE APPLY IT IN OUR MODEL
****************************************************************************************************************************************************88
Here we create our choises in an array of tuples. The tuples have two values, the first value will be stored in the database , while the second , which is in human readable form can be used in a dropdown menu
We then use the choises we created in the memebership column. This limits the number of choises to the ones we defined in the MEEMBERSHIP_CHOISES variable.
We can also set a default value.

class Product(models.Model):
      MEMEBERSHIP_CHOISES = [
                                ('B','Bronze'),
                                ('S', 'Silver'),
                                ('G','Gold')
                            ]
    
      membership = models.CharField(max_length=1,choise= MEMEBERSHIP_CHOISES, default = 'B')
      title = models.CharField(max_length =255)
      inventory = models.IntegerField()








However there is aproblem with the following above approach
****************************************************************************************************************************************************88
The problem is that whenever we want toupdate one value, wehave to do it it in multiple places.
Example, if we want to change the default from B  to T -> Tiatanin, we have to change it in multiple places



WE CAN SOLVE THE ABOVE PROBLEM LIKE THIS




class Product(models.Model):
      MEMBERSHIP_BRONZE = 'B'
      MEMBERSHIP_SILVER = 'S'
      MEMBERSHIP_GOLD = 'G'
      MEMEBERSHIP_CHOISES = [
                                (MEMBERSHIP_BRONZE,'Bronze'),
                                (MEMBERSHIP_SILVER, 'Silver'),
                                (MEMBERSHIP_GOLD,'Gold')
                            ]
    
      membership = models.CharField(max_length=1,choise= MEMEBERSHIP_CHOISES, default = MEMBERSHIP_BRONZE)
      title = models.CharField(max_length =255)
      inventory = models.IntegerField()







































































































...
