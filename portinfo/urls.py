from django.urls import path
from . import views


urlpatterns = [
    path('', views.portinfo_home, name='portinfo'),

]
