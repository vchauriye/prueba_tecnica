from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('weight', index),
    path('grass', index),
    path('flying_10', index),
    path('inverted_name', index)
]
