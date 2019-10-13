from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import item
# Create your views here.


def sampleView(request):
    all_items = item.objects.all()
    return render(request, 'sample.html', {'all_items': all_items})


def addItem(request):
    new_item = item(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/sample/')


def deleteItem(request, item_id):
    item_to_delete = item.objects.get(id=item_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/sample/')


def index(request):
    return render(request, 'home.html')