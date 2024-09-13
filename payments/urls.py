from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),
    path('agendamentos/<int:id>/', views.detalhar_agendamento, name='detalhar_agendamento'),
    path('agendamentos/deletar/<int:id>/', views.deletar_agendamento, name='deletar_agendamento'),
]
