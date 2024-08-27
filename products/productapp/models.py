from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    image_url = models.URLField(default='https://example.com/default-image.jpg')
    
    

    def __str__(self) -> str:
        return self.title


