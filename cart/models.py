from django.db import models
from django.contrib.auth.models import User
from store.models import Product
# Create your models here.
class Cart(models.Model):

    cart_id = models.CharField(max_length=250)
    date_field = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Cart")
        verbose_name_plural = ("Carts")

    def __str__(self):
        return self.cart_id
    
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color_value = models.CharField(max_length=150)
    size_value = models.CharField(max_length=150)

    def __str__(self) -> str:
        return str(self.id)    

class Cart_item(models.Model):
    name=models.CharField( max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variations = models.ForeignKey(Variation, on_delete=models.CASCADE,blank=True,null=True,)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)


    def sub_total(self):
        return (self.product.price)* self.quantity
    class Meta:
        verbose_name = ("Cart_item")
        verbose_name_plural = ("Cart_items")
        
    def save(self,*args, **kwargs):
        self.name=f"{self.product}/{self.variations.color_value}/{self.variations.size_value}"
        super(Cart_item,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

class Coupon(models.Model):
    name = models.CharField(max_length=150)
    value = models.CharField(max_length=100)
    ratio = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    

    class Meta:
        verbose_name = ("Coupon")
        verbose_name_plural = ("Coupons")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Coupon_detail", kwargs={"pk": self.pk})


    

 