from django.db import models
from django.utils.text import slugify

# Create your models here.
def image_upload(instance,file_name:str):
    extension=file_name.split('.')[1]
    return f"category/{instance.name}.{extension}"
class Category(models.Model):

    name=models.CharField(max_length=50)
    slug=models.SlugField()
    image=models.ImageField(upload_to=image_upload)
    description=models.TextField()
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.name
