from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import generics, status
from .models import *
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.

### auth stuff ###

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['neighbourhood'] = user.neighbourhood
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

### Register View ###

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account =serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['username']= account.username
            data['name']= account.name
            data['neighbourhood']= account.neighbourhood
        else:
            data = serializer.errors
        return Response(data)


### product CRUD ###

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def productDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance= product , data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response("Product successfully deleted")




### Neighbourhood CRUD ###



@api_view(['GET'])
def neighbourhoodList(request):
    neighbourhood = Neighbourhood.objects.all()
    serializer = ProductSerializer(neighbourhood, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def neighbourhoodDetail(request, pk):
    neighbourhood = Neighbourhood.objects.get(id=pk)
    serializer = NeighbourhoodSerializer(neighbourhood, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def neighbourhoodCreate(request):
    serializer = NeighbourhoodSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def neighbourhoodUpdate(request, pk):
    neighbourhood = Neighbourhood.objects.get(id=pk)
    serializer = NeighbourhoodSerializer(instance= neighbourhood , data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def neighbourhoodDelete(request, pk):
    neighbourhood = Neighbourhood.objects.get(id=pk)
    neighbourhood.delete()
    return Response("neighbourhood successfully deleted")



### Event CRUD ###



@api_view(['GET'])
def eventList(request):
    event = Event.objects.all()
    serializer = ProductSerializer(event, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def eventCreate(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def eventUpdate(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance= event , data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eventDelete(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return Response("Event successfully deleted")



### facility CRUD ###



@api_view(['GET'])
def facilityList(request):
    facility = Facility.objects.all()
    serializer = ProductSerializer(facility, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def facilityDetail(request, pk):
    facility = Facility.objects.get(id=pk)
    serializer = FacilitySerializer(facility, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def facilityCreate(request):
    serializer = FacilitySerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def facilityUpdate(request, pk):
    facility = Facility.objects.get(id=pk)
    serializer = FacilitySerializer(instance= facility , data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def facilityDelete(request, pk):
    facility = Facility.objects.get(id=pk)
    facility.delete()
    return Response("facility successfully deleted")



### Article CRUD ###



@api_view(['GET'])
def articleList(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def articleDetail(request, pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializer(article, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def articleUpdate(request, pk):
    facility = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance= facility , data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def articleDelete(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return Response("article successfully deleted")



### job CRUD ###



@api_view(['GET'])
def jobList(request):
    job = Job.objects.all()
    serializer = JobSerializer(job, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def jobDetail(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def jobCreate(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def jobUpdate(request, pk):
    job = Job.objects.get(id=pk)
    serializer = JobSerializer(instance= job , data=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def jobDelete(request, pk):
    job = Job.objects.get(id=pk)
    job.delete()
    return Response("job successfully deleted")




