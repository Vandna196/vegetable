from django.db import models 
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField
# Create your models here.
#index
class Top(models.Model):
    phone = models.IntegerField()
    gmail = models.EmailField(max_length=255)
    text = models.CharField(max_length=255)
    isactive = models.BooleanField()
    def __str__(self):
        return self.text
        
class Left(models.Model):
    name = models.CharField(max_length=255)
    menu = models.CharField(max_length=255)
    isactive = models.BooleanField()
    def __str__(self):
        return self.name       
class Nav(models.Model):
    title = models.CharField(max_length=255)
    titlea = models.CharField(max_length=255)
    titleb = models.CharField(max_length=255)
    titlec = models.CharField(max_length=255)
    titled = models.CharField(max_length=255)
    titlee = models.CharField(max_length=255)
    isactive = models.BooleanField()
    def __str__(self):
        return self.title   
class Drop(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    def __str__(self):
        return self.title
class Slider(models.Model):
  img = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  btn = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Service(models.Model):
  heading = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  headingb = models.CharField(max_length=255)
  headingc = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  textc = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Category(models.Model):
    img = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=100)
    #slug = models.SlugField(max_length=200, db_index=True, unique=True)
    isactive = models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Product(models.Model):
  id = models.AutoField(primary_key=True)
  category_id = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  img = models.ImageField(upload_to = 'images/')
  name = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
  saleprice = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)
  isactive = models.BooleanField()
  def __str__(self):
        return self.name
  def get_update_cart_url(self):
      return reverse("update_cart",kwargs={
          'id':self.id
          })
  def get_remove_from_cart_url(self):
      return reverse("remove_from_cart",kwargs={
          'id':self.id
          })
  
class Item1(models.Model):
  text = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  para = models.TextField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text

class Oneitem(models.Model):
  img = models.ImageField(upload_to = 'images/')
  text = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  para = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  dataa = models.CharField(max_length=255)
  datab = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Test(models.Model):
   text = models.CharField(max_length=255)
   heading = models.CharField(max_length=255)
   para = models.TextField(max_length=255)
   isactive = models.BooleanField()
   def __str__(self):
         return self.heading
class Testimonial(models.Model):
  img = models.ImageField(upload_to = 'images/')
  para = models.TextField(max_length=255)
  heading = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Pattern(models.Model):
  img = models.ImageField(upload_to = 'images/')
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.link
class Form(models.Model):
  heading = models.CharField(max_length=255)
  para = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
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
#about section
class About(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Disc(models.Model):
  img = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  paraa = models.TextField(max_length=255)
  parab = models.TextField(max_length=255)
  link = models.CharField(max_length=255)
  btn = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Counter(models.Model):
  img = models.ImageField(upload_to = 'images/')
  ids = models.CharField(max_length=255)
  isactive = models.BooleanField() 
  def __str__(self):
        return self.ids  
class Count(models.Model):
  number = models.IntegerField()
  num = models.IntegerField()
  heading = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
#blog section
class Blog(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Blogdetail(models.Model):
  link = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  headingb = models.CharField(max_length=255)
  headingc = models.CharField(max_length=255)
  para = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Blogdis(models.Model):
  img = models.ImageField(upload_to = 'images/')
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  heading = models.CharField(max_length=255)
  para = models.CharField(max_length=255)
  btn = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Ccategory(models.Model):
  name = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.name
class Recblog(models.Model):
  img = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Cloud(models.Model):
  link = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.link
#blog single section
class Food(models.Model):
  heading = models.CharField(max_length=255)
  para = models.TextField()
  img = models.ImageField(upload_to = 'images/')
  paraa = models.TextField()
  headinga = models.CharField(max_length=255)
  parab = models.TextField()
  imga = models.ImageField(upload_to = 'images/')
  parai = models.TextField()
  paraj = models.TextField()
  parak = models.TextField()
  paral = models.TextField()
  headingb = models.CharField(max_length=255)
  headingc = models.CharField(max_length=255)
  headingd = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  headine = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Thing(models.Model):
  name = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.name
class Author(models.Model):
  img = models.ImageField(upload_to = 'images/')
  heading = models.CharField(max_length=255)
  para = models.TextField()
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Comment(models.Model):
  heading = models.CharField(max_length=255)
  img = models.ImageField(upload_to = 'images/')
  headinga = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  para = models.TextField()
  btn = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Data(models.Model):
  heading = models.CharField(max_length=255)
  laba = models.CharField(max_length=255)
  labb = models.CharField(max_length=255)
  labc = models.CharField(max_length=255)
  labd = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
#cart section
class Cart1(models.Model):
  products = models.ManyToManyField('Product', blank=True)
  count = models.PositiveIntegerField(default=0)
  total = models.IntegerField()
  timestamp = models.DateTimeField(auto_now_add=False,auto_now=True)
  updated = models.DateTimeField(auto_now_add=False,auto_now=True)
  isactive = models.BooleanField()
  def __str__(self):
        return "their total is ${}".format(self.count,self.total)    
 
class Cartdtl(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Head(models.Model):
  heading = models.CharField(max_length=255)
  headinga = models.CharField(max_length=255)
  headingb = models.CharField(max_length=255)
  headingc = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Cart(models.Model):
  link = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
  product = models.ForeignKey(Product,null=True, on_delete=models.CASCADE) 
  cart1 = models.ForeignKey(Cart1,null=True,blank=True,on_delete=models.CASCADE)
  productid = models.CharField(max_length=255)
  quantity = models.CharField(max_length=255)
  isactive = models.BooleanField()
  
class Coupon(models.Model):
 code = models.CharField(max_length = 15)
 
 def __str__(self):
        return self.code
class Shipping(models.Model):
  heading = models.CharField(max_length=255)
  para = models.TextField()
  laba = models.CharField(max_length=255)
  labb = models.CharField(max_length=255)
  labc = models.CharField(max_length=255)
  btn = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
class Total(models.Model):
  heading = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  data = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  dataa = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  datab = models.CharField(max_length=255)
  textc= models.CharField(max_length=255)
  datac = models.CharField(max_length=255)
  btn = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.heading
#checkout section
class Checkot(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Option(models.Model):
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text



#contact section
class Contact(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Contactinfo(models.Model):
  laba = models.CharField(max_length=255)
  labb = models.CharField(max_length=255)
  labc = models.CharField(max_length=255)
  labd = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  textc = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Msg(models.Model):
  text = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  subject = models.CharField(max_length=255)
  message = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
#single product section
class Singpro(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Singleitem(models.Model):
  img = models.ImageField(upload_to = 'static/images')
  heading = models.CharField(max_length=255)
  value = models.CharField(max_length=255)
  data = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  dataa = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  datab = models.CharField(max_length=255)
  quantity = models.CharField(max_length=255)
  para = models.TextField()
  textc = models.CharField(max_length=255)
  textd = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Value(models.Model):
  text = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Item(models.Model):
  img = models.ImageField(upload_to = 'images/')
  value = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Items(models.Model):
  img = models.ImageField(upload_to = 'images/')
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
# shop section
class Shop(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Categry(models.Model):
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  textc = models.CharField(max_length=255)
  textd = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Itemal(models.Model):
  img = models.ImageField(upload_to = 'images/')
  value = models.CharField(max_length=255)
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  textb = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text
class Itemall(models.Model):
  img = models.ImageField(upload_to = 'images/')
  text = models.CharField(max_length=255)
  texta = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.text  
class Page(models.Model):
  one = models.CharField(max_length=255)
  two = models.CharField(max_length=255)
  three = models.CharField(max_length=255)
  four = models.CharField(max_length=255)
  five = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.one
#wishlist section
class Wishlist(models.Model):
  img = models.ImageField(upload_to = 'images/')
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  titlea = models.CharField(max_length=255)
  body = models.CharField(max_length=255)
  isactive = models.BooleanField()
  def __str__(self):
        return self.title
class Wish(models.Model):
   heading = models.CharField(max_length=255)
   headinga = models.CharField(max_length=255)
   headingb = models.CharField(max_length=255)
   headingc = models.CharField(max_length=255)
   isactive = models.BooleanField()
   def __str__(self):
         return self.heading  
class Wishitem(models.Model):
   img = models.ImageField(upload_to = 'images/')
   name = models.CharField(max_length=255)
   price = models.CharField(max_length=255)
   saleprice = models.CharField(max_length=255)
   link = models.CharField(max_length=255)
   isactive = models.BooleanField()
   def __str__(self):
         return self.name
class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    orderitem_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def get_total_product_price(self):
        return self.quantity * self.product.price
    
    def get_total_product_saleprice(self):
        return self.quantity * self.product.saleprice
    
    def get_amount_saved(self):
        return self.get_total_product_price() - self.get_total_product_saleprice()
    
    def get_final_price(self):
        if self.product.saleprice:
            return self.get_total_product_saleprice()
        return self.get_total_product_price()
            
    
    
    
class Order(models.Model): 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(OrderItem)
    total = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    discount = models.DecimalField(max_digits=4, decimal_places=2,default=0.00)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey('BillingAddress',on_delete=models.SET_NULL,blank=True, null=True)
    payment = models.ForeignKey('Payment',on_delete=models.SET_NULL,blank=True, null=True)
    coupon = models.ForeignKey('Coupon',on_delete=models.SET_NULL,blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    def get_subtotal(self):
        subtotal = 0
        for order_item in self.products.all():
            subtotal += order_item.get_final_price()
        return subtotal
    
class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    
    def __str_(self):
        return self.user.username
class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    amount = models.DecimalField(max_digits=19, decimal_places=10,default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True)
   
    
    def __str_(self):
        return self.user.username
    
        
      