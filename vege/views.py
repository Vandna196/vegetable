from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from .models import Order,OrderItem,BillingAddress,Payment,Top,Nav,Drop,Left,Slider,Service,Category,Product,Item1,Oneitem,Test,Testimonial,Pattern,Form,Footer,Fooitem,Fooitem1,Fooitem2,About,Disc,Count,Counter,Blog,Blogdetail,Blogdis,Ccategory,Recblog,Cloud,Food,Thing,Author,Comment,Data,Cart1,Cartdtl,Head,Cart,Coupon,Shipping,Total,Checkot,Option,Contact,Contactinfo,Msg,Singpro,Singleitem,Value,Shop,Categry,Page,Wishlist,Wish,Wishitem
from .forms import CartForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from .forms import CheckoutForm,CouponForm
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_key = "sk_test_OtFBZlUabocwLMM0AVOM7bq300UvcMZVk8"




def messageform(request):
    if request.method =='POST':
        form  = Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('index')
        else:
            form = Form()
        return render(request,'index.html',{'form':form})

# Create your views here.
@login_required
def index(request):
    top = Top.objects.all()#fetching all objects from models
    nav = Nav.objects.all()
    drop = Drop.objects.all()
    left = Left.objects.all
    slider = Slider.objects.all()
    service = Service.objects.all()
    category = Category.objects.all()
    product = Product.objects.all()
    item1 = Item1.objects.all()
    oneitem = Oneitem.objects.all()
    test = Test.objects.all()
    testimonial = Testimonial.objects.all()
    pattern = Pattern.objects.all()
    form = Form.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()
    
    context ={
        'tops':top,
        'navs':nav,
        'drops':drop,
        'lefts':left,
        'sliders':slider,
        'services':service,
        'categorys':category,
        'products':product,
        'item1s':item1,
        
        'oneitems':oneitem,
        'tests':test,
        'testimonials':testimonial,
        'patterns':pattern,
        'forms':form,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,
        
        
        
        }
    return render(request,"index.html",context)
def about(request):
    top = Top.objects.all()
    nav = Nav.objects.all()
    drop = Drop.objects.all()
    left = Left.objects.all
    about = About.objects.all()
    disc = Disc.objects.all()
    form = Form.objects.all()
    count = Count.objects.all()
    counter = Counter.objects.all()
    test = Test.objects.all()
    testimonial = Testimonial.objects.all()
    service = Service.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()
    context ={
        'tops':top,
        'navs':nav,
        'drops':drop,
        'lefts':left,
        'abouts':about,
        'discs':disc,
        'forms':form,
        'counts':count,
        'counters':counter,
        'tests':test,
        'testimonials':testimonial,
        'services':service,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,

        }
    return render(request,"about.html",context)
def blog(request):
    top = Top.objects.all()
    nav = Nav.objects.all()
    drop = Drop.objects.all()
    left = Left.objects.all()
    blog = Blog.objects.all()
    blogdetail = Blogdetail.objects.all()
    blogdis = Blogdis.objects.all()
    ccategory = Ccategory.objects.all()
    recblog = Recblog.objects.all()
    cloud = Cloud.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()
    context = {
        'tops':top,
        'navs':nav,
        'drops':drop,
        'lefts':left,
        'blogs':blog,
        'blogdetails':blogdetail,
        'blogdiss':blogdis,
        'ccategorys':ccategory,
        'recblogs':recblog,
        'clouds':cloud,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,
        
        
        }
    return render(request,"blog.html",context)
def blogsingle(request):
    top = Top.objects.all()
    nav = Nav.objects.all()
    drop = Drop.objects.all()
    left = Left.objects.all()
    blog = Blog.objects.all()
    food = Food.objects.all()
    thing = Thing.objects.all()
    author = Author.objects.all()
    comment = Comment.objects.all()
    data = Data.objects.all()
    ccategory = Ccategory.objects.all()
    recblog = Recblog.objects.all()
    cloud = Cloud.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()

    context = {
        'tops':top,
        'navs':nav,
        'drops':drop,
        'lefts':left,
        'blogs':blog,
        'foods':food,
        'things':thing,
        'authors':author,
        'comments':comment,
        'datas':data,
        'ccategorys':ccategory,
        'recblogs':recblog,
        'clouds':cloud,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,

        
        }
    return render(request,"blogsingle.html",context)
class OrderSummaryView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                    'order':order
                    }
            return render(self.request,"cart.html",context)
        except ObjectDoesNotExist:
            messages.error(self.request,"You do not have an active order")
            return redirect("cart")
    






def cart(request):
    try:
        order = Order.objects.get(user=request.user, ordered=False)
        top = Top.objects.all()
        nav = Nav.objects.all()
        drop = Drop.objects.all()
        left = Left.objects.all()
        cartdtl =Cartdtl.objects.all()
        head = Head.objects.all()
        item1 = Item1.objects.all()
        cart1 = Cart1.objects.all()
        cart = Cart.objects.all()
        coupon = Coupon.objects.all()
        shipping = Shipping.objects.all()
        total = Total.objects.all()
        form = Form.objects.all() 
        footer = Footer.objects.all()
        fooitem = Fooitem.objects.all()
        fooitem1 = Fooitem1.objects.all()
        fooitem2 = Fooitem2.objects.all()
        context = {
                   'order':order,
                   'tops':top,
                   'navs':nav,
                   'drops':drop,
                   'lefts':left,
                   'cart1':cart1,
                   'item':item1,
                   'cartdtls':cartdtl,
                   'heads':head,
                   'cart':cart,
                   'coupons':coupon,
                   'shippings':shipping,
                   'totals':total,
                   'forms':form,
                   'footers':footer,
                   'fooitems':fooitem,
                   'fooitem1s':fooitem1,
                   'fooitem2s':fooitem2,
                }
        return render(request,"cart.html",context)
    except ObjectDoesNotExist:
        messages.error(request,"You do not have an active order")
        return redirect("cart")
    

@login_required
def update_cart(request,id):
    product = get_object_or_404(Product,id=id)
    order_item,created = OrderItem.objects.get_or_create(
        product = product,
        user = request.user,
        ordered = False
       
        )
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item in the order
        if order.products.filter(product__id = product.id).exists():    
            order_item.quantity +=1
            order_item.save()
            return redirect("cart")
            
        else:
            order.products.add(order_item)
            return redirect("cart")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user = request.user,ordered_date = ordered_date)
        order.products.add(order_item)
        messages.info(request,"This item was added to your cart.")
        return redirect("cart")
@login_required
def remove_from_cart(request,id):
    product = get_object_or_404(Product,id=id)
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item in the order
        if order.products.filter(product__id = product.id).exists():
            order_item = OrderItem.objects.filter(
            product = product,
            user = request.user,
            ordered = False
            )[0]
            order.products.remove(order_item)  
            messages.info(request,"This item was removed from your cart.")
            return redirect("cart")
        else:
           
           messages.info(request,"This item was not in your cart.")
           return redirect("index")
    else:
        #add a message saying the user doesnot have an order
        messages.info(request,"you do not have an active order")
        return redirect("index")
@login_required
def remove_single_product_from_cart(request,id):
    product = get_object_or_404(Product,id=id)
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
        )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item in the order
        if order.products.filter(product__id = product.id).exists():
            order_item = OrderItem.objects.filter(
            product = product,
            user = request.user,
            ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
            else:
                order.products.remove(order_item)
            order_item.save()
            messages.info(request,"This item quantity was updated")
            return redirect("cart")
        else:
           
           messages.info(request,"This item was not in your cart.")
           return redirect("index")
    else:
        #add a message saying the user doesnot have an order
        messages.info(request,"you do not have an active order")
        return redirect("index")
   
    
   
    
    
    
    
    
def wishlist_store(request):
    print(request.POST) 
    #heading = request.POST['title'];
    #quantity = request.POST['quantity'];
   # wishitem = Wishitem(heading = heading,quantity = quantity)
   # wishitem.save();
      
    return render(request,"wishlist.html")
class CheckoutView(View):
     def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user = self.request.user, ordered = False)
            form = CheckoutForm()
            couponform = CouponForm()
            context = {
             'form':form,
             'couponform':couponform,
             'order':order,
             'DISPLAY_COUPON_FORM':True
             }
            return render(self.request,"checkout.html",context)
        except ObjectDoesNotExist:
            messages.error(self.request,"You do not have an active order")
            return redirect("checkout")
        
     def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                #to add functionality to these fields
                #same_shipping_address = form.cleaned_data.get('same_shipping_address')
               # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zip = zip,
                    
                    
                    )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                if payment_option == 'S':
                    return redirect("payment", payment_option='stripe')
                elif payment_option == 'P':
                     return redirect("payment",payment_option='paypal')
                else:
                     messages.warning(self.request, "invalid payment option")
                     return redirect("index")
        except ObjectDoesNotExist:
            messages.error(self.request,"You do not have an active order")
            return redirect("cart")
        
        
class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user,ordered=False)
        if order.billing_address:
            context = {
                'order':order,
                'DISPLAY_COUPON_FORM':False
                }
            return render(self.request,"payment.html",context)
        else:
            messages.warning(self.request,"You have not added billing address")
            return redirect("checkout")
    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user,ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_subtotal())*100
        try:
            charge = stripe.Charge.create(
            amount = amount,
            currency = "usd",
            source = token,
            
            )
            
            order.ordered = True
            #create the payment
            
            payment = Payment()
            payment.stripe_charge_id  = charge['id']
            payment.user = self.request.user
            payment.amount = order.get_subtotal()
            payment.save()
            
            #assign the payment to the order
            order_items = Order.products.all()
            order_items.update(ordered=True)
            for product in order_items:
                product.save()
            order.ordered = True
            order.payment = payment
            order.save()
            
            messages.success(self.request,"your order was successul!")
            return redirect("index")
        
        
        
        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error',{})
            messages.warning(self.request, f"{err.get('message')}")
            return redirect("index")
            
        except stripe.error.RateLimitError as e:
            #too many requests made to the api too quicky
            messages.warning(self.request, "Rate Limit Error")
            return redirect("index")
           
        except stripe.error.InvalidRequestError as e:
            #invalid parameters were supplied to strie api
            messages.warning(self.request, "Invalid parameters")
            return redirect("index")
        except stripe.error.AuthenticationError as e:
            #authentication with stripe failed
            messages.warning(self.request, "Authentication failed")
            return redirect("index")
        except stripe.error.APIConnectionError as e:
            #network communication with stripe failed
            messages.warning(self.request, "Network error ")
            return redirect("index")
        except stripe.error.StripeError as e:
            #GENERIC ERROR TO USER OR MAY SEND EMAIL TO YOUR SELF
            messages.warning(self.request, "Something went wrong.you were not charged,please try again.")
            return redirect("index")
        except Exception as e:
            #send mail to ourselves
            messages.warning(self.request, "A SERIOUS ERROR OCCURRED.WE HAVE BEEN NOTIFIED")
            return redirect("index")
            
def payment(request):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user,ordered=False)
        context = {
            'order':order
            }
        return render(self.request,"payment.html",context)
    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user,ordered=True)
        token = self.request.POST.get('stripeToken')
        amount = order.get_subtotal()
        try:
            charge = stripe.Charge.create(
            amount = amount,
            currency = "usd",
            source = token,
            
            )
            
            order.ordered = True
            #create the payment
            
            payment = Payment()
            payment.stripe_charge_id  = charge['id']
            payment.user = self.request.user
            payment.amount = order.get_subtotal()
            payment.save()
            
            #assign the payment to the order
            order_items = Order.products.all()
            order_items.update(ordered=True)
            for product in order_items:
                product.save()
            order.ordered = True
            order.payment = payment
            order.save()
            
            messages.success(self.request,"your order was successul!")
            return redirect("index")
        
        
        
        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error',{})
            messages.error(self.request, f"{err.get('message')}")
            return redirect("index")
            
        except stripe.error.RateLimitError as e:
            #too many requests made to the api too quicky
            messages.error(self.request, "Rate Limit Error")
            return redirect("index")
           
        except stripe.error.InvalidRequestError as e:
            #invalid parameters were supplied to strie api
            messages.error(self.request, "Invalid parameters")
            return redirect("index")
        except stripe.error.AuthenticationError as e:
            #authentication with stripe failed
            messages.error(self.request, "Authentication failed")
            return redirect("index")
        except stripe.error.APIConnectionError as e:
            #network communication with stripe failed
            messages.error(self.request, "Network error ")
            return redirect("index")
        except stripe.error.StripeError as e:
            #GENERIC ERROR TO USER OR MAY SEND EMAIL TO YOUR SELF
            messages.error(self.request, "Something went wrong.you were not charged,please try again.")
            return redirect("index")
        except Exception as e:
            #send mail to ourselves
            messages.error(self.request, "A SERIOUS ERROR OCCURRED.WE HAVE BEEN NOTIFIED")
            return redirect("index")       
        

def checkout(request):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user = self.request.user, ordered = False)
            form = CheckoutForm()
            couponform = CouponForm()
            context = {
             'form':form,
             'couponform':couponform,
             'order':order
             }
            return render(self.request,"checkout.html",context)
        except ObjectDoesNotExist:
            messages.error(request,"You do not have an active order")
            return redirect("checkout")
        
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                #to add functionality to these fields
                #same_shipping_address = form.cleaned_data.get('same_shipping_address')
               # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')
                billing_address = BillingAddress(
                    user = self.request.user,
                    street_address = street_address,
                    apartment_address = apartment_address,
                    country = country,
                    zip = zip,
                    
                    
                    )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                if payment_option == 'S':
                    return redirect("payment", payment_option='stripe')
                elif payment_option == 'P':
                     return redirect("payment",payment_option='paypal')
                else:
                     messages.warning(self.request, "invalid payment option")
                     return redirect("index")
        except ObjectDoesNotExist:
            messages.error(self.request,"You do not have an active order")
            return redirect("cart")
        
        
        
def get_coupon(request,code):
    
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.error(request,"this coupon does not exist")
        return redirect("checkout")
    
class AddCouponView(View):
    def post(self, *args, **kwargs):
        
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(user=self.request.user, ordered = False)
                order.coupon = get_coupon(self.request,code)
                order.save()
                messages.success(self.request,"successfully added coupon")
                return redirect("checkout")
            except ObjectDoesNotExist:
                messages.error(self.request,"You do not have an active order")
                return redirect("checkout")
           
   
    
def contact(request):
   top = Top.objects.all()
   nav = Nav.objects.all()
   drop = Drop.objects.all()
   left = Left.objects.all()
   contact = Contact.objects.all()
   contactinfo = Contactinfo.objects.all()
   msg = Msg.objects.all()
   footer = Footer.objects.all()
   fooitem = Fooitem.objects.all()
   fooitem1 = Fooitem1.objects.all()
   fooitem2 = Fooitem2.objects.all()

   context = {
      'tops':top,
      'navs':nav,
      'drops':drop,
      'lefts':left,
      'contacts':contact,
      'contactinfos':contactinfo,
      'msgs':msg,
      'footers':footer,
      'fooitems':fooitem,
      'fooitem1s':fooitem1,
      'fooitem2s':fooitem2,
      
        }
   return render(request,"contact.html",context)
def productsingle(request):
   top = Top.objects.all()
   nav = Nav.objects.all()
   drop = Drop.objects.all()
   left = Left.objects.all()
   singpro = Singpro.objects.all()
   singleitem = Singleitem.objects.all()
   value = Value.objects.all()
   product = Product.objects.all()
  
   item1 = Item1.objects.all()
   form = Form.objects.all() 
   footer = Footer.objects.all()
   fooitem = Fooitem.objects.all()
   fooitem1 = Fooitem1.objects.all()
   fooitem2 = Fooitem2.objects.all()
  
   context = {
      'tops':top,
      'navs':nav,
      'drops':drop,
      'lefts':left,
      'singpros':singpro,
      'singleitems':singleitem,
      'values':value,
      'products':product,
      'item1s':item1,
      
      'forms':form,
      'footers':footer,
      'fooitems':fooitem,
      'fooitem1s':fooitem1,
      'fooitem2s':fooitem2
      
      
        }
   return render(request,"productsingle.html",context)
def shop(request):
   top = Top.objects.all()
   nav = Nav.objects.all()
   drop = Drop.objects.all()
   left = Left.objects.all()
   shop = Shop.objects.all()
   categry = Categry.objects.all()
   product = Product.objects.all()
   page = Page.objects.all()
   form = Form.objects.all() 
   footer = Footer.objects.all()
   fooitem = Fooitem.objects.all()
   fooitem1 = Fooitem1.objects.all()
   fooitem2 = Fooitem2.objects.all()
   
   context = {
      'tops':top,
      'navs':nav,
      'drops':drop,
      'lefts':left,
      'shops':shop,
      'categrys':categry,
      'products':product,
      'pages':page,
      'forms':form,
      'footers':footer,
      'fooitems':fooitem,
      'fooitem1s':fooitem1,
      'fooitem2s':fooitem2,
     
        }
   return render(request,"shop.html",context)
def wishlist(request):
   top = Top.objects.all()
   nav = Nav.objects.all()
   drop = Drop.objects.all()
   left = Left.objects.all()
   wishlist = Wishlist.objects.all()
   wish = Wish.objects.all()
   wishitem = Wishitem.objects.all()
   form = Form.objects.all() 
   footer = Footer.objects.all()
   fooitem = Fooitem.objects.all()
   fooitem1 = Fooitem1.objects.all()
   fooitem2 = Fooitem2.objects.all()
   
   context = {
      'tops':top,
      'navs':nav,
      'drops':drop,
      'lefts':left,
      'wishlists':wishlist,
      'wishs':wish,
      'wishitems':wishitem,
      'forms':form,
      'footers':footer,
      'fooitems':fooitem,
      'fooitem1s':fooitem1,
      'fooitem2s':fooitem2
      }
   return render(request,"wishlist.html",context)
class In(View):
    def get(self, request):
        form = Form()
        context = {
             'form':form,
             }
        return render(self.request,"web/index.html",context)
    def post(self, request):
        form = Form(self.request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email_address = form.cleaned_data.get('email_address')
            phone_number = form.cleaned_data.get('phone_number')
            message = form.cleaned_data.get('message')
            message_form = Message_form(
            full_name = full_name,
            email_address = email_address,
            phone_number = phone_number,
            message = message)
            message_form.save()
        return render(self.request,"web/index.html",message_form)