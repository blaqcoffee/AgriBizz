from django.db import models
from django.db.models.fields import CharField, SmallIntegerField
from django.db.models.fields.files import ImageField


class PostProduct(models.Model):
    # Region choices
    
    CHOICES = (
        ('Arusha', 'Arusha'),
        ('Dar es Salaam', 'Dar es Salaam'),
        ('Geita', 'Geita'),
        ('Kagera', 'Kagera'),
        ('Mwanza', 'Mwanza'),
        ('Morogoro', 'Morogoro'),
        ('Shinyanga', 'Shinyanga'),
        ('Tabora', 'Tabora'),
        ('Singida', 'Singida'),
        ('Simiyu', 'Simiyu'),
        ('Mbeya', 'Mbeya'),
        ('Mara', 'Mara'),
        ('Kilimanjaro', 'Kilimanjaro'),
        ('Tanga', 'Tanga'),
        ('Kigoma', 'Kigoma'),
        ('Mtwara', 'Mtwara'),
        ('Pwani', 'Pwani'),
        ('Simiyu', 'Simiyu'),
        ('Songwe', 'Songwe'),
        ('Lindi', 'Lindi'),
        ('Dodoma', 'Dodoma'),
        ('Singida', 'Singida'),
        ('Ruvuma', 'Ruvuma'),
        ('Njombe', 'Njombe'),
    )

    # Product Choices
    PRODUCT_CHOICES = (
        ('Maize', 'Maize'),
        ('Rice', 'Rice'),
        ('Beans', 'Beans'),
        ('Carrot', 'Carrot'),
        ('Cabage', 'Cabage'),
        ('Beans', 'Beans'),
        ('Vegetables', 'Vegetables'),
        ('Ginger', 'Ginger'),
        ('Garlic','Garlic'),
        ('Banana', 'Banana'),
        ('Tomato', 'Tomato'),
        ('Lemon', 'Lemon'),
        ('Coffee', 'Coffee'),

    )

    # Scale Choice
    SCALE_CHOICES = (
        ('Kg', 'Kg'),
        ('Debe', 'Debe'),
        ('Sack', 'Sack'),
        ('Tons', 'Tons'),
    )

    # Person's Details
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254,blank= True, null=True )
    phone_number = models.CharField(max_length=13,null=False, blank=False)
    region = models.CharField(max_length=50, choices=CHOICES, ) 
    district = models.CharField(max_length=150, default='')
    ward = models.CharField(max_length=150, default='')


    def __str__(self):
        return self.full_name

    # Product's Detials
    product_name = models.CharField(max_length=100, choices= PRODUCT_CHOICES,)
    scale = models.CharField(max_length=50, choices=SCALE_CHOICES,)
    amount = models.IntegerField(null=False, blank=False, default='Enter Amount')
    price = models.FloatField(max_length=100, null=False, blank=False, default='Enter Price')
    date_created = models.DateTimeField(auto_now_add = True)
    thumbnail = ImageField(upload_to='static/img/', default='No-Image-Placeholder.svg')

    def __str__(self):
        return self.product_name
        