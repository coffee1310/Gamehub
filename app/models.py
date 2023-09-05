from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html
from phone_field import PhoneField

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=255)
    phone_number = PhoneField()
    address = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class ProductImage(models.Model):
    image = models.ImageField(upload_to='Img/')

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return format_html(f'<img src="{self.image.url}" width="50" height="50" />')

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name="Цена")
    description = models.TextField(verbose_name="Описание", blank=True)
    images = models.ManyToManyField(ProductImage, related_name="product_images", blank=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField("Comments", related_name='product_comments', blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

class Manufacturer(models.Model):
    title = models.CharField(max_length=255, verbose_name="Производитель")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

class Mouse(Product):
    SIZE_CHOICES = (
        ("Big", "Большой"),
        ("Middle", "Средний"),
        ("Small", "Маленький")
    )

    DPI_CHOSES = (
        ("less than 5000", "Менее 5000"),
        ("5001-10000", "5000-10000"),
        ("10001-15000", "10001-15000"),
        ("15001-20000", "15001-20000")
    )

    CASE_COLOR_CHOSES = (
        ("Beige", "Бежевый"),
        ("White", "Белый"),
        ("Turquoise", "Бирюзовый"),
        ("Blue", "Синий"),
        ("Yellow", "Желтый"),
        ("Black", "Черный")
    )

    SENSOR_TYPE_CHOICES = (
        ("Laser", "Лазерный"),
        ("Optical LED", "Оптический светодиодный")
    )

    manufacturer = models.ForeignKey('Manufacturer',on_delete=models.CASCADE, verbose_name="Производитель")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default="Middle", verbose_name="Размер мыши")
    DPI = models.CharField(max_length=20, choices=DPI_CHOSES, default="5000-10000")
    case_color = models.CharField(max_length=10, choices=CASE_COLOR_CHOSES, default="Black", verbose_name="Цвет корпуса")
    sensor_type = models.CharField(max_length=20, choices=SENSOR_TYPE_CHOICES, default="Laser", verbose_name="Тип сенсора")

    class Meta:
        verbose_name = "Мышь"
        verbose_name_plural = "Мыши"




class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Комментарий")
    advantages = models.TextField(verbose_name="Преимущества", blank=True)
    disadvantages = models.TextField(verbose_name="Недостатки", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"