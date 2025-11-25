from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return F"{self.name} ({self.email})"

class Emp(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    salary=models.IntegerField()
    
class FormModel(models.Model):
    username=models.CharField(max_length=255)
    email=models.CharField(unique=True)
    password= models.CharField(max_length=100)

class Blogpost(models.Model):
    title=models.CharField(max_length=50)
    post=models.CharField(max_length=500,default="")
    #we are uploading images as well so we make a image folder to store them and also put null=True as if image is not there it should show null
    thumbnail=models.ImageField(upload_to="images/",null=True, blank=True )
    def __str__(self):
        return self.title
