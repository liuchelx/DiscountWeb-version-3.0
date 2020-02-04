from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
import datetime

class Product(models.Model):

    Product_ID = models.AutoField(primary_key=True) 
    ProductName = models.CharField(max_length=200)

    twoWeeks =timezone.now() + datetime.timedelta(days=14)


    PubTime = models.DateTimeField(auto_now=False, auto_now_add=False) 
    #if there's no endding time, make the default endding time two weeks until now
    EndTime = models.DateTimeField(auto_now=False, auto_now_add=False) 

    OriPrice = models.FloatField(default=0) #original price
    DisPrice = models.FloatField(default=0) #price after discount

    Shoplink = models.URLField(max_length=500)
    imglink = models.URLField(max_length=500)

    Tag = models.CharField(max_length=200)  #tag for the product, at present only luxury, clothing, electronic
    click = models.IntegerField(default=0)  # count how many times of this product has been clicked
    

    def __str__(self):
        return self.ProductName

    #check if the item's discount has ended, if end= Ture, not end: False
    def isExpired(self):
        now = timezone.now()
        if self.EndTime >now:
            return False
        else:
            return True

    isExpired.admin_order_field = 'PubTime'

    #change the display form to calculate how many time left for endding
    def showEndTime(self):
        return self.EndTime.strftime('%D')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_pic.png', upload_to='profile_pics')
    wishlisted_products= models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.user.username}' 

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)