from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView  
from rest_framework import status, mixins, generics, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from django.shortcuts import get_object_or_404

from .models import Carlist, Showroom, Review
from .api_file.serializer import CarSerializer, ShowroomSerializer, ReviewSerializer

# --- MIXIN + GENERIC VIEWS FOR REVIEW ---

class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions] 

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [DjangoModelPermissions]

# --- VIEWSET FOR SHOWROOM ---


class ShowroomViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Showroom.objects.all()
        serializer = ShowroomSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        showroom = get_object_or_404(Showroom, pk=pk)
        serializer = ShowroomSerializer(showroom, context={'request': request})
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ShowroomSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- CLASS BASED VIEW FOR SHOWROOM LIST/CREATE ---

class ShowroomView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        showrooms = Showroom.objects.all()
        serializer = ShowroomSerializer(showrooms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ShowroomSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- CLASS BASED DETAIL VIEW FOR SHOWROOM ---

class ShowroomDetails(APIView):
    def get_object(self, pk):
        return get_object_or_404(Showroom, pk=pk)

    def get(self, request, pk):
        showroom = self.get_object(pk)
        serializer = ShowroomSerializer(showroom, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        showroom = self.get_object(pk)
        serializer = ShowroomSerializer(showroom, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        showroom = self.get_object(pk)
        showroom.delete()
        return Response({"message": "Showroom deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# --- FUNCTION BASED VIEWS FOR CARLIST ---

@api_view(['GET', 'POST'])  
def car_list_view(request):
    if request.method == 'GET':
        cars = Carlist.objects.all()
        serializer = CarSerializer(cars, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])  
def car_list_detail(request, pk):  
    try:
        car = Carlist.objects.get(pk=pk)
    except Carlist.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car.delete()
        return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
