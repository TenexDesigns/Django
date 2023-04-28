
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)




def kimani(request):
    book = Product.objects.values('id','title','collection__title')  ---> Here we are able to acces the values of the collection table by taking advantage of the one to many relationship it has with the products table. We then use the tale nameand add two undescores to get the values.   
    return render(request,'hello.html',{'book':book})





























































































...
