from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from store.forms import DishForm, UpdateDishForm
from store.models import Dish

from django.views import View
def index(request):
    return HttpResponse(f"Hello {request.user.username}!")


def dishes(request):
    all_dishes = Dish.objects.all()
    return render(request, 'dishes_list.html', {"all_dishes": all_dishes})


def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'dish.html', {'dish': dish})


def dish_create(request):
    instance = None
    if request.method == 'POST':
        form = DishForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect("/dishes")

    return render(request, 'create_dish.html', {'form': DishForm(instance=instance)})


def dish_update(request, pk):
    if request.method == 'POST':
        form = UpdateDishForm(request.POST)

        if form.is_valid():
            price = form.cleaned_data['price']
            Dish.objects.filter(pk=pk).update(price=price)
            return HttpResponseRedirect("/dishes")

    return render(request, 'update_dish.html', {'form': UpdateDishForm()})
