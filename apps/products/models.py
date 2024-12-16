from django.db import models
from models import BaseModel

class Category(BaseModel):
    title = models.CharField(max_length=256,
                             null=True,
                             blank=True
                             )

    def __str__(self):
        return self.title



class Product(BaseModel):
    name = models.CharField(max_length=256,
                            null=True,
                            blank=True
                            )

    description = models.TextField(null=True,
                                   blank=True
                                   )

    price = models.DecimalField( max_digits=10,
                                       decimal_places=2,
                                       null=False,
                                       default=0.0
                                       )

    stock = models.PositiveIntegerField(verbose_name="Amount ")

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE
                                 )

    def __str__(self):
        return self.name



class ProductImage(BaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images",
                                verbose_name="Product"
                                )

    image = models.ImageField(upload_to='products/images/', verbose_name="Image")
    is_main = models.BooleanField(default=False, verbose_name="Main image")
    order = models.PositiveIntegerField(default=0, verbose_name="Order of display")
