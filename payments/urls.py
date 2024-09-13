from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_agendamentos, name='listar_agendamentos'), 
    path('<int:id>/', views.detalhar_agendamento, name='detalhar_agendamento'),  
    path('deletar/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),  
]
