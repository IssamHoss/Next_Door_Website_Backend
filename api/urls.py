from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [

    ### Auth stuff ###

    path ('', views.getRoutes),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    ### Register ###

    path('register/', views.registration_view, name= "register"),
    
    ### products ###

    path('product-list/', views.productList, name="product-list"),
    path('product-detail/<str:pk>/', views.productDetail, name="product-detail"),
    path('product-create/', views.productCreate, name="product-create"),
    path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
    path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),

    ### Neighbourhood ###

    path('neighbourhood-list/', views.neighbourhoodList, name="neighbourhood-list"),
    path('neighbourhood-detail/<str:pk>/', views.neighbourhoodDetail, name="neighbourhood-detail"),
    path('neighbourhood-create/', views.neighbourhoodCreate, name="neighbourhood-create"),
    path('neighbourhood-update/<str:pk>/', views.neighbourhoodUpdate, name="neighbourhood-update"),
    path('neighbourhood-delete/<str:pk>/', views.neighbourhoodDelete, name="neighbourhood-delete"),

    ### Event ###
    
    path('event-list/', views.eventList, name="event-list"),
    path('event-detail/<str:pk>/', views.eventDetail, name="event-detail"),
    path('event-create/', views.eventCreate, name="event-create"),
    path('event-update/<str:pk>/', views.eventUpdate, name="event-update"),
    path('event-delete/<str:pk>/', views.eventDelete, name="event-delete"),

    ### Facility ###

    path('facility-list/', views.facilityList, name="facility-list"),
    path('facility-detail/<str:pk>/', views.facilityDetail, name="facility-detail"),
    path('facility-create/', views.facilityCreate, name="facility-create"),
    path('facility-update/<str:pk>/', views.facilityUpdate, name="facility-update"),
    path('facility-delete/<str:pk>/', views.facilityDelete, name="facility-delete"),

    ### Article ###

    path('article-list/', views.articleList, name="article-list"),
    path('article-detail/<str:pk>/', views.articleDetail, name="article-detail"),
    path('article-create/', views.articleCreate, name="article-create"),
    path('article-update/<str:pk>/', views.articleUpdate, name="article-update"),
    path('article-delete/<str:pk>/', views.articleDelete, name="article-delete"),

    ### Jobs ###

    path('job-list/', views.jobList, name="job-list"),
    path('job-detail/<str:pk>/', views.jobDetail, name="job-detail"),
    path('job-create/', views.jobCreate, name="job-create"),
    path('job-update/<str:pk>/', views.jobUpdate, name="job-update"),
    path('job-delete/<str:pk>/', views.jobDelete, name="job-delete"),

]
