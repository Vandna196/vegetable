from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Top,Footer,Fooitem,Fooitem1,Fooitem2,Slider
# Create your views here.
def first(request):
    top = Top.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()
    slider = Slider.objects.all()
    context = {
        'tops':top,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,
        'sliders':slider,
       }
    return render(request,'first.html',context)
def register(request):
    top = Top.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()
    slider = Slider.objects.all()
    context = {
        'tops':top,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,
        'sliders':slider,
       }
    if request.method == 'POST':
        first_name = request.POST.get('first_name',False);
        last_name = request.POST.get('last_name',False);
        username = request.POST.get('username',False);
        email = request.POST.get('email',False);
        password1 = request.POST.get('password1',False);
        password2 = request.POST.get('password2',False);
        if password1 == password2:
            if User.objects.filter(username =username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email =email).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,password = password1,email = email,first_name = first_name,last_name = last_name)
                user.save();
                messages.info(request,'User Created')
                return redirect('login')
        
        else:
            messages.info(request,'password not matching..')
            return redirect('register')
        return redirect('')
    else:
        return render(request,'register.html',context)
    
def login(request):
    top = Top.objects.all()
    footer = Footer.objects.all()
    fooitem = Fooitem.objects.all()
    fooitem1 = Fooitem1.objects.all()
    fooitem2 = Fooitem2.objects.all()
    slider = Slider.objects.all()
    context = {
        'tops':top,
        'footers':footer,
        'fooitems':fooitem,
        'fooitem1s':fooitem1,
        'fooitem2s':fooitem2,
        'sliders':slider,
       }
    if request.method == 'POST':
        username = request.POST.get('username',False);
        password = request.POST.get('password',False);
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("vege/index")
        else:
            messages.info(request,"invalid credentials")
            return redirect("login")
    else:
        return render(request,'login.html',context)
def logout(request):
    auth.logout(request)
    return redirect('/')