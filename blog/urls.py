from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('study/',views.study, name='study'),
    path('rf/', views.rf, name='rf'),
]