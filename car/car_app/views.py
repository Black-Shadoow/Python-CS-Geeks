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

# from django.http import JsonResponse, HttpResponse  # Corrected: HttpResponse was misspelled and not imported
# from .models import Carlist
import json  # Required for json.dumps

#2. View to list all cars
# def car_list_view(request):
#     cars = Carlist.objects.all()
#     data = {
#         'cars': list(cars.values())
#     }
#     data_json = json.dumps(data, indent=4)  # Optional: formatted JSON
#     return HttpResponse(data_json, content_type='application/json')  # Corrected: HttpResponse spelling

# # View to get a single car by primary key (pk)
# def car_list_detail(request, pk):
#     try:
#         car = Carlist.objects.get(pk=pk)
#         data = {
#             'name': car.name,
#             'desc': car.desc,
#             'active': car.active,
#         }
#     except Carlist.DoesNotExist:
#         return JsonResponse({'error': 'Car not found'}, status=404)

#     return JsonResponse(data, json_dumps_params={'indent': 4})


from django.http import JsonResponse, HttpResponse  
from .models import Carlist
from .api_file.serializer import CarSerializer  # Corrected import

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])  # Optional: specify method(s)
def car_list_view(request):
    cars = Carlist.objects.all()
    serializer = CarSerializer(cars, many=True)  # many=True because it's a queryset
    return Response(serializer.data)

@api_view()  
def car_list_detail(request, pk):  # ✅ FIXED: added 'request' and 'pk' to parameters
    car = Carlist.objects.get(pk=pk)  # ✅ FIXED: corrected arguments to .get()
    serializer = CarSerializer(car)
    return Response(serializer.data)
