from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from covid import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('trackings/', views.TrakingList.as_view()),
    path('trackings/<int:pk>/', views.TrackingDetail.as_view()),
    path('pois/', views.PoiList.as_view()),
    path('pois/<int:pk>/', views.PoiDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    #path('rest-auth/facebook/connect/$', views.FacebookConnect.as_view(), name='fb_connect'),
]
