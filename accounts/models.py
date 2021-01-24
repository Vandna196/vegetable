from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Top(models.Model):
    phone = models.IntegerField()
    gmail = models.EmailField(max_length=255)
    text = models.CharField(max_length=255)
    isactive = models.BooleanField()
    def __str__(self):
        return self.text
class First(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
  name = models.CharField(max_length=255)
  register = models.CharField(max_length=255)
  login = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.name
class Register(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  username = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password1 = models.CharField(max_length=255)
  password2 = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.email
class Login(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Slider(models.Model):
  img = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  btn = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Footer(models.Model):
  heading = models.CharField(max_length=255)
  para = models.TextField(max_length=255)
  link = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  gmail = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  headingb = models.CharField(max_length=255)
  headingc = models.CharField(max_length=255)
  paraa = models.CharField(max_length=255)
  parab = models.CharField(max_length=255)
  parac = models.CharField(max_length=255)
  parad = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Fooitem(models.Model):
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Fooitem1(models.Model):
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Fooitem2(models.Model):
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text