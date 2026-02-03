from django.shortcuts import render,redirect,get_object_or_404
from .models import Category,Clothitems
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CategoryForm,ClothItemsForm
from django.contrib import messages

# Create your views here.

@staff_member_required
def category_list(request):
    items=Category.objects.all()
    return render(request,'dress/category_list.html',{"items":items})



@staff_member_required
def admin_dashboard(request):
    items=Clothitems.objects.all()
    categories=Category.objects.all().order_by('-id')
    context={
        'items':items,
        'categories':categories,
        'itemcount':items.count(),
        'catcount':categories.count()
    }
    return render(request,'dress/dashboard.html',context)



@staff_member_required
def dress_create(request):
    if request.method=="POST":
        form=ClothItemsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"new dress added successfully")
            return redirect('dashboard')
    else:
        form=ClothItemsForm()
    return render(request,'dress/dress_form.html',{"form":form})



@staff_member_required
def category_create(request):
    if request.method=="POST":
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"category added sucessfully")
            return redirect('category_list')
    else:
        form=CategoryForm()
    return render(request,'dress/category_form.html',{"form":form})



@staff_member_required
def category_update(request,pk):
    item=get_object_or_404(Category,pk=pk)
    if request.method=="POST":
        form=CategoryForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,'category updated sucessfully')
            return redirect('category_list')
    else:
        form=CategoryForm(instance=item)
    return render(request,'dress/category_form.html',{"form":form})