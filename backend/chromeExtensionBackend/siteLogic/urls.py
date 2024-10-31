from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    path('daily_quote/', views.generate_motivational_quote, name='daily_quote'),
]
