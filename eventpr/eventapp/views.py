from django.shortcuts import render,redirect
from.models import *
from.forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def review(request):
    return render(request,'review.html')

def makeup(request):
    dict_mak={
        'mak':Makeup.objects.all()
    }
    return render(request,'makeup.html',dict_mak)

def decorator(request):
    dict_dec={
        'dec':Decorator.objects.all()
    }
    return render(request,'decorator.html',dict_dec)

def invitation(request):
    dict_inv={
        'inv':Invitation.objects.all()
    }
    return render(request,'invitation.html',dict_inv)

def catering(request):
    dict_cat={
        'cat':Catering.objects.all()
    }
    return render(request,'catering.html',dict_cat)

def gift(request):
    dict_gif={
        'gif':Gift.objects.all()
    }
    return render(request,'gift.html',dict_gif)

def wear(request):
    dict_wea={
        'wea':Wear.objects.all()
    }
    return render(request,'wear.html',dict_wea)

def jewellery(request):
    dict_jew={
        'jew':Jewellery.objects.all()
    }
    return render(request,'jewellery.html',dict_jew)

def photographer(request):
    dict_pho={
        'pho':Photographer.objects.all()
    }
    return render(request,'photographer.html',dict_pho)

def hotel(request):
    dict_ven={
        'ven':Hotel.objects.all()
    }
    return render(request,'hotel.html',dict_ven)

def choreographer(request):
    dict_cho={
        'cho':Choreographer.objects.all()
    }
    return render(request,'choreographer.html',dict_cho)

def mehendi(request):
    dict_meh={
        'meh':Mehendi.objects.all()
    }
    return render(request,'mehendi.html',dict_meh)

def djs(request):
    dict_djs={
        'djs':Dj.objects.all()
    }
    return render(request,'djs.html',dict_djs)

def mak(request):
    if request.method=='POST':
        form=MakForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form=MakForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/mak.html',dict_form)

def dec(request):
    if request.method=='POST':
        form=DecForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=DecForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/dec.html',dict_form)

def inv(request):
    if request.method=='POST':
        form=InvForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=InvForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/inv.html',dict_form)

def cat(request):
    if request.method=='POST':
        form=CatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=CatForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/cat.html',dict_form)

def gif(request):
    if request.method=='POST':
        form=GifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=GifForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/gif.html',dict_form)

def wea(request):
    if request.method=='POST':
        form=WeaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=WeaForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/wea.html',dict_form)

def jew(request):
    if request.method=='POST':
        form=JewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=JewForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/jew.html',dict_form)

def cho(request):
    if request.method=='POST':
        form=ChoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=ChoForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/cho.html',dict_form)


def ven(request):
    if request.method=='POST':
        form=VenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    form=VenForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/ven.html',dict_form)


def pho(request):
    if request.method=='POST':
        form=PhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=PhoForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/pho.html',dict_form)

def meh(request):
    if request.method=='POST':
        form=MehForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=MehForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/dj.html',dict_form)

def dj(request):
    if request.method=='POST':
        form=DjForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=DjForm()
    dict_form={
        'form':form
    }
    return render(request,'booking/dj.html',dict_form)