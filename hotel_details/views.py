from django.shortcuts import render,redirect
from .models import Hotel
from .forms import HotelForm
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    # give me all the items.
    
    all_items = Hotel.objects.all()
    return render(request,'home.html',{'all_items':all_items}) 



def create(request):
    all_items = Hotel.objects.all()
    form = HotelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,("New date is added in the list!"))
        return redirect(home)
    else:
        
        return render(request,'create.html',{'all_items':all_items})



def update(request,id):
    if request.method == 'POST':
        item = Hotel.objects.get(pk=id)
        form = HotelForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,( item.name + " is added in the Edited!"))
            return redirect(home)
    else:
        item = Hotel.objects.get(pk=id)
        return render(request,'update.html',{'item':item})


def delete(request,id):



    item = Hotel.objects.get(pk=id)
    item.delete()
    messages.success(request,("Data of " + item.name+ " has been succefully Data has be deleted!"))
    return redirect(home)

    