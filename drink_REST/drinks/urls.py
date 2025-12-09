from django.urls import path
from . import views

urlpatterns = [
  path('view/' , views.drink_list ),
  path('view/<int:id>/' , views.drink_detail)
]