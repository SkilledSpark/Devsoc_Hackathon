from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.form_submission),
    path('home/', views.redirect),
    path('', views.login),
]
