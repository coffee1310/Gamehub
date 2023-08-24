from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from phone_field import PhoneField

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=255,)
    phone_number = PhoneField()
    address = models.CharField(max_length=255,)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/product_images/')

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание", blank=True)
    images = models.ManyToManyField(ProductImage, related_name="product_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField("Comments", related_name='comments_article', blank=True)


class Comments(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Комментарий")
    advantages = models.TextField(verbose_name="Преимущества")
    disadvantages = models.TextField(verbose_name="Недостатки")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
