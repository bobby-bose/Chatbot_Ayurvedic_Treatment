from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('checkout/', views.checkout, name='checkout'),
    path('payments/', views.payments, name='payments'),
]
