# from django.shortcuts import render

# # Create your views here.
# from .models import Carlist
# from django.http import JsonResponse

# def car_list_view(request):
#     car = Carlist.objects.all()
#     data = {
#         'cars': list(car.values()),
#     }
#     return JsonResponse(data)

from django.http import JsonResponse
from .models import Carlist

def car_list_view(request):
    cars = Carlist.objects.all()
    data = {
        'cars': list(cars.values())
    }
    return JsonResponse(data,json_dumps_params={'indent': 4})

def car_list_detail(request,pk):
    car=Carlist.objects.get(pk=pk)
    data={
        'name':car.name,
        'desc':car.desc,
        'active':car.active,
    }
    return JsonResponse(data,json_dumps_params={'indent': 4})
