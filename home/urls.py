from django.urls import path, include
from home import views
from rest_framework import routers

router=routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    
]
