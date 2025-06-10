# from django.urls import path,include
# from . import views

# urlpatterns = [
#     path('list' ,views.car_lsit, name='list'),
  
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('list', views.car_list_view, name='list'),
    path('<int:pk>', views.car_list_detail, name='car_detail'),
    path('showroom/', views.ShowroomView.as_view(), name='showroom-list'),
    path('showroom/<int:pk>/', views.Showroom_details.as_view(), name='showroom-detail'),
    path('review', views.ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),  # ✅ Removed redundant 'car/'
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('list', views.car_list_view, name='list'),
#     path('<int:pk>', views.car_list_detail, name='car_detail'),
#     path('showroom/',views.ShowroomView.as_view(), name='showroom-list'),
#     path('showroom/<int:pk>/', views.Showroom_details.as_view(), name='showroom-detail'),
#     path('review',views.ReviewList.as_view(), name='review_list'),
#     path('car/review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
# ]