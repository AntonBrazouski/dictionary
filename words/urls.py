from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
]
