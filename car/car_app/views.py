from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView  
from rest_framework import status
from .models import Carlist, Showroom ,Review 
from .api_file.serializer import CarSerializer, ShowroomSerializer ,ReviewSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework import mixins, generics
from rest_framework.permissions import DjangoModelPermissions

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

class ShowroomView(APIView):
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]
    #permission_classes=[AllowAny] # allow everyone 
    #permission_classes=[IsAdminUser]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        showrooms = Showroom.objects.all()
        serializer = ShowroomSerializer(showrooms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Showroom_details(APIView):
    def get(self, request, pk):
        try:
            showroom = Showroom.objects.get(pk=pk)
        except Showroom.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    
        serializer = ShowroomSerializer(showroom)
        return Response(serializer.data)

        
    def put(self,request,pk):
        showrooms = Showroom.objects.get(pk=pk)
        serializer=ShowroomSerializer(Showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,pk):
        showroom=Showroom.objects.get(pk=pk)
        showroom.delete()
        return Response({"message": "Showroom deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])  
def car_list_view(request):
    if request.method == 'GET':
        cars = Carlist.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
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
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        car=Carlist.objects.get(pk=pk)
        car.delete()
        return Response({"message": "Car deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
