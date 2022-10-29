from django.urls import path
from .views import DisplayList, DetailList

urlpatterns = [
    path('profiles/', DisplayList.as_view()),
    path('profiles/<int:pk>', DetailList.as_view())
]
