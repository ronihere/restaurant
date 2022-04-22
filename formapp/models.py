from django.db import models

# Create your models here.
class contactform(models.Model):

    name= models.CharField(default="none",max_length=20)
    email=models.EmailField(default="none",max_length=30)
    message=models.TextField(default="none",max_length=200)
    phone=models.CharField(default="none",max_length=13)
    def __str__(self):
        return self.name
class booktable(models.Model):
    name = models.CharField(default="none", max_length=20)
    email = models.EmailField(default="none", max_length=30)
    phone = models.CharField(default="none", max_length=13)
    date = models.DateField(default="none")
    time = models.TimeField(default="none")
    people = models.IntegerField(default="none")
    message = models.TextField(default="none", max_length=200)
    def __str__(self):
        f=f"{self.time} --> {self.date} -->{self.name}"
        return f
class menu(models.Model):
    name = models.CharField(max_length=19)
    desc = models.TextField(max_length=50)
    img = models.ImageField(default="none",upload_to="menu_pics")
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name
class specials(models.Model):
    id= models.IntegerField(primary_key=True)
    name = models.CharField(max_length=19)
    short_desc = models.TextField(max_length=70)
    big_desc = models.TextField(max_length=200)
    img = models.ImageField(default="none", upload_to="special_pics")

    def __str__(self):
        return self.name
class Gallery(models.Model):
    name = models.CharField(max_length=10,default="none")
    img = models.ImageField(default="none", upload_to="gallery_pics")
    def __str__(self):
        return self.name
class subscription(models.Model):
    email = models.EmailField(default="none", max_length=30)
    def __str__(self):
        return self.email