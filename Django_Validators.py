
Django provides a wide range of built-in validators that you can use to validate form data. 
Heres an overview of some of the most commonly used validators and how to use them in Django:



1.Required Validator

The Required Validator ensures that a form field is not empty.

from django import forms
from django.core.validators import Required

class MyForm(forms.Form):
    name = forms.CharField(validators=[Required()])



2.Email Validator

The Email Validator ensures that a form field contains a valid email address.


from django import forms
from django.core.validators import EmailValidator

class MyForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator()])


3.Max Value Validator

The Max Value Validator ensures that a form field is not greater than a specified maximum value.

from django import forms
from django.core.validators import MaxValueValidator

class MyForm(forms.Form):
    age = forms.IntegerField(validators=[MaxValueValidator(100)])



4.Min Value Validator

The Min Value Validator ensures that a form field is not less than a specified minimum value.

from django import forms
from django.core.validators import MinValueValidator

class MyForm(forms.Form):
    age = forms.IntegerField(validators=[MinValueValidator(18)])



5.Max Length Validator

The Max Length Validator ensures that a form field is not longer than a specified maximum length.

from django import forms
from django.core.validators import MaxLengthValidator

class MyForm(forms.Form):
    message = forms.CharField(validators=[MaxLengthValidator(200)])

    
    

7.Min Length Validator

The Min Length Validator ensures that a form field is not shorter than a specified minimum length.

from django import forms
from django.core.validators import MinLengthValidator

class MyForm(forms.Form):
    password = forms.CharField(validators=[MinLengthValidator(8)])



8.Regular Expression Validator

The Regular Expression Validator ensures that a form field matches a specified regular expression.


from django import forms
from django.core.validators import RegexValidator

class MyForm(forms.Form):
    code = forms.CharField(validators=[RegexValidator('^X-[0-9]{3}$')])


9.RegexValidator

The RegexValidator ensures that a form field matches a specified regular expression pattern.

from django import forms
from django.core.validators import RegexValidator

class MyForm(forms.Form):
    code = forms.CharField(validators=[RegexValidator(r'^[A-Z]{2}-\d{4}$', 'Code should be in the format XX-YYYY.')])



10.EmailValidator

The EmailValidator ensures that a form field contains a valid email address.


from django import forms
from django.core.validators import EmailValidator

class MyForm(forms.Form):
    email = forms.EmailField(validators=[EmailValidator('Enter a valid email address.')])



11.URLValidator

The URLValidator ensures that a form field contains a valid URL.


from django import forms
from django.core.validators import URLValidator

class MyForm(forms.Form):
    website = forms.CharField(validators=[URLValidator('Enter a valid URL.')])

    
    

12.validate_email

The validate_email function checks whether an email address is valid and can be delivered.

from django.core.validators import validate_email

try:
    validate_email('example@example.com')
except ValidationError:
    # Handle invalid email address
    pass


13.validate_slug

The validate_slug function checks whether a string is a valid slug.


from django.core.validators import validate_slug

try:
    validate_slug('example-slug')
except ValidationError:
    # Handle invalid slug
    pass




14.validate_unicode_slug

The validate_unicode_slug function checks whether a string is a valid Unicode slug.


from django.core.validators import validate_unicode_slug

try:
    validate_unicode_slug('example-slug')
except ValidationError:
    # Handle invalid slug
    pass




15.validate_ipv4_address

The validate_ipv4_address function checks whether a string is a valid IPv4 address.



from django.core.validators import validate_ipv4_address

try:
    validate_ipv4_address('192.168.1.1')
except ValidationError:
    # Handle invalid IPv4 address
    pass



16.validate_ipv46_address

The validate_ipv46_address function checks whether a string is a valid IPv4 or IPv6 address.



from django.core.validators import validate_ipv46_address

try:
    validate_ipv46_address('192.168.1.1')
except ValidationError:
    # Handle invalid IP address
    pass

try:
    validate_ipv46_address('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
except ValidationError:
    # Handle invalid IP address
    pass




17.validate_comma_separated_integer_list

The validate_comma_separated_integer_list function checks whether a string contains a list of integers separated by commas.

from django.core.validators import validate_comma_separated_integer_list

try:
    validate_comma_separated_integer_list('1,2,3')
except ValidationError:
    # Handle invalid comma-separated list of integers
    pass





18.validate_slug: 
  This is a standalone function that can be used to validate slugs.


  from django.core.validators import validate_slug

try:
    validate_slug('hello_world!')
except ValidationError as e:
    print(e)



19.int_list_validator: 
  This is a custom validator that can be used to validate a list of integers.


from django.core.validators import BaseValidator

class int_list_validator(BaseValidator):
    message = 'Enter a comma separated list of integers'
    code = 'invalid'
    
    def __call__(self, value):
        try:
            values = [int(i) for i in value.split(',')]
            if not all(isinstance(i, int) for i in values):
                raise ValidationError(self.message, code=self.code)
        except ValueError:
            raise ValidationError(self.message, code=self.code)

class Person(models.Model):
    age_list = models.CharField(validators=[int_list_validator])





20.DecimalValidator: This validator is used to validate decimal numbers.



from django.core.validators import DecimalValidator

class Product(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[DecimalValidator(
        max_value=1000,
        message='Price should not exceed 1000',
        code='invalid_price'
    )])



21.FileExtensionValidator: This validator is used to validate file extensions.

from django.core.validators import FileExtensionValidator

class Document(models.Model):
    file = models.FileField(validators=[FileExtensionValidator(
        allowed_extensions=['pdf', 'doc', 'docx'],
        message='File should be either a PDF or a Word document',
        code='invalid_file_extension'
    )])



22.validate_image_file_extension: This is a standalone function that can be used to validate image file extensions.

from django.core.validators import validate_image_file_extension

try:
    validate_image_file_extension('image.png')
except ValidationError as e:
    print(e)


23.ProhibitNullCharactersValidator: This validator is used to check if a string contains null characters.

  from django.core.validators import ProhibitNullCharactersValidator

class Person(models.Model):
    name = models.CharField(max_length=50, validators=[ProhibitNullCharactersValidator(
        message='Name should not contain null characters',
        code='invalid_name'
    )])
``


24.URLValidator: Used to validate a URL field. For example:
    
    from django.core.validators import URLValidator

class MyModel(models.Model):
    url = models.URLField(validators=[URLValidator()])




































































































































































































...
