from django.urls import path
from . import views

app_name = 'words'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('search/', views.search, name='search'),
]
