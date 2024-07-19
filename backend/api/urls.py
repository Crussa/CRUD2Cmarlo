from django.urls import path, include
from rest_framework.routers import DefaultRouter
from.views import Itemviewset


router = DefaultRouter()
router.register(r'items', Itemviewset)

urlpatterns = [
    path('', include(router.urls)),
    

]