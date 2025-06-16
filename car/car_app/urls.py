from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('showroom', views.ShowroomViewSet, basename='showroom')

urlpatterns = [
    # Function-based car list views
    path('list/', views.car_list_view, name='list'),
    path('<int:pk>/', views.car_list_detail, name='car_detail'),

    # ViewSet route (automatically handles /showroom/ and /showroom/<pk>/)
    path('', include(router.urls)),

    # Review endpoints (Class-based generic views)
    path('review/', views.ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review_detail'),
]
