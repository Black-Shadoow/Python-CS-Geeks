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

from django.http import JsonResponse, HttpResponse  # Corrected: HttpResponse was misspelled and not imported
from .models import Carlist
import json  # Required for json.dumps

# View to list all cars
def car_list_view(request):
    cars = Carlist.objects.all()
    data = {
        'cars': list(cars.values())
    }
    data_json = json.dumps(data, indent=4)  # Optional: formatted JSON
    return HttpResponse(data_json, content_type='application/json')  # Corrected: HttpResponse spelling

# View to get a single car by primary key (pk)
def car_list_detail(request, pk):
    try:
        car = Carlist.objects.get(pk=pk)
        data = {
            'name': car.name,
            'desc': car.desc,
            'active': car.active,
        }
    except Carlist.DoesNotExist:
        return JsonResponse({'error': 'Car not found'}, status=404)

    return JsonResponse(data, json_dumps_params={'indent': 4})
