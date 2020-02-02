
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from . import views
from .forms import UserSignUpForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.utils import timezone
from .models import Product
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def main_page(request):
    return render(request, 'discountsApp/mainPage.html')

def index(request):
    latest_item_list = Product.objects.order_by('PubTime')
    endding_item_list = Product.objects.order_by('EndTime')
    TodaySpecial =[]
    lastChance =[]
    luxury =[]
    electronic_product=[]
    clothing=[]
    now =timezone.now()
    for i in range(len(latest_item_list)):
        if len(TodaySpecial)==4  and len(luxury)==4 and len(electronic_product) ==4 and len(clothing) ==4:
            break
        else:
            if latest_item_list[i].Tag == 'Luxury' and len(luxury)<4:
                luxury.append(latest_item_list[i])
            if latest_item_list[i].Tag == 'electronic product' and len(electronic_product)<4:
                electronic_product.append(latest_item_list[i])
            if latest_item_list[i].Tag == 'Clothing' and len(clothing)<4:
                clothing.append(latest_item_list[i])
            if now - latest_item_list[i].PubTime < datetime.timedelta(days=1) and len(TodaySpecial)<4:
                TodaySpecial.append(latest_item_list[i])
    for j in range(len(endding_item_list)):
        print()
        if endding_item_list[j].EndTime - datetime.timedelta(days=2)< now and len(lastChance)<4 and endding_item_list[j].isExpired() ==False:
                lastChance.append(endding_item_list[j])

    context ={
        'latest_item_list':latest_item_list,
        'lastChance':lastChance,
        'TodaySpecial':TodaySpecial,
        'luxury':luxury,
        'electronic_product':electronic_product,
        'clothing':clothing,

    }
    return render(request,'discountsApp/index.html',context)

def search(request):
    keyWord = request.POST.get('keyWord',"")
    print('keyword is',keyWord)
    response ={'keyWord':keyWord}
    # return JsonResponse(response)
    return HttpResponse(request.POST.items())

def allPorduct(request):
    item_list = Product.objects.order_by('PubTime')


    context={
        'item_list':item_list,
    }  
    return render(request,'discountsApp/all.html',context)

def luxury(request):
    item_list = Product.objects.all()
    luxury =[]

    for item in item_list:
        if item.Tag == 'Luxury':
            luxury.append(item)
    
    paginator = Paginator(luxury,2)
   

    page = request.GET.get('page') 
    try:
        luxury = paginator.page(page)  
    except PageNotAnInteger:  
        luxury = paginator.page(1) 
    except EmptyPage:  
        luxury = paginator.page(paginator.num_pages)  

    context={
        'luxury':luxury,
    }  
    return render(request,'discountsApp/luxury.html',context)

def electronic (request):
    item_list = Product.objects.all()
    electronic  =[]

    for item in item_list:
        if item.Tag == 'electronic product':
            electronic.append(item)
    
    paginator = Paginator(electronic,2)
   

    page = request.GET.get('page') 
    try:
        electronic = paginator.page(page)  
    except PageNotAnInteger:  
        electronic = paginator.page(1) 
    except EmptyPage:  
        electronic = paginator.page(paginator.num_pages)  

    context={
        'electronic':electronic,
    }  
    return render(request,'discountsApp/electronic.html',context)

def clothing (request):
    item_list = Product.objects.all()
    clothing  =[]

    for item in item_list:
        if item.Tag == 'Clothing':
            clothing.append(item)
    
    paginator = Paginator(clothing,2)
 

    page = request.GET.get('page') 
    try:
        clothing = paginator.page(page)  
    except PageNotAnInteger:  
        clothing = paginator.page(1) 
    except EmptyPage:  
        clothing = paginator.page(paginator.num_pages)  

    context={
        'clothing':clothing,
    }  
    return render(request,'discountsApp/clothing.html',context)

def lastChancePage(request):
    endding_item_list = Product.objects.order_by('EndTime')
    lastchance  =[]
    now =timezone.now()
    for item in endding_item_list:
        if item.EndTime - datetime.timedelta(days=2)< now:
                lastchance.append(item)


    context={
        'lastchance':lastchance,
    }  
    return render(request,'discountsApp/lastChance.html',context)



def signUp(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print('valid')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account {username} created! Please sign in now!')
            return redirect('signIn')
    else:
        form = UserSignUpForm()
        print('invalid')

    # if request.method == 'POST' and form.is_valid():
    #     new_user = form.save()
    #     return HttpResponseRedirect('/')
    # form = forms.signUpForm()
    # if request == 'POST':
    #     form = forms.signUpForm(request.POST)
    #     if form.is_valid():

    #         user_name = form.cleaned_data.get('user_name')
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         new_user = User(name=user_name, password=password, email=email)
    #         new_user.save()

    #     else:
    #         form = forms.signUpForm()
    # return render(request, 'discountsApp/signUp.html', {'form': form})
    return render(request, 'discountsApp/signUp.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if user_update_form.is_valid() and user_profile_update_form.is_valid():
            user_update_form.save()
            user_profile_update_form.save()
            messages.success(request, f'Profile updated!')
            return redirect('profile')
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        user_profile_update_form = UserProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_update_form': user_update_form,
        'user_profile_update_form': user_profile_update_form
    }
    return render(request, 'discountsApp/profile.html', context)

@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product,pk=id)
    user_profile = request.user.profile
    if not user_profile.wishlisted_products.filter(Product_ID=id):
        user_profile.wishlisted_products.add(product)
        messages.success(request, f'Item added!')
    else:
        messages.warning(request, f'Item already in your wishlist!')
    return redirect('discountsApp:discounts-main')

@login_required
def remove_from_wishlist(request, id):
    product = get_object_or_404(Product,pk=id)
    user_profile = request.user.profile
    if user_profile.wishlisted_products.filter(Product_ID=id):
        user_profile.wishlisted_products.remove(product)
        messages.success(request, f'Item removed!')

    return redirect('discountsApp:wishlist')

@login_required
def wishlist(request):
    user_profile = request.user.profile
    wishlisted_products = user_profile.wishlisted_products.all()
    context = {
        'wishlisted_products': wishlisted_products
    }

    return render(request, 'discountsApp/wishlist.html',context)