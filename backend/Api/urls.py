from django.urls import path, include
from rest_framework import routers
from .views import ToDoView

router = routers.DefaultRouter()
router.register(r'todos', ToDoView,'todo')
urlpatterns = [
    path('', include(router.urls)),
]