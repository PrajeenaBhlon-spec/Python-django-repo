from django.urls import path
from . import views
urlpatterns = [
  path('view/' , views.login_form_show),
  path('home/' , views.home_page, name="home")
]