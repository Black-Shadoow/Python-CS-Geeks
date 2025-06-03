# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path('list' ,views.car_lsit, name='list'),
  
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.car_list_view, name='list'),
    path('<int:pk>', views.car_list_detail, name='car_detail')
]