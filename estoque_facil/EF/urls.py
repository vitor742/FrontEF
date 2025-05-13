from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('produtos/', views.produtos_view, name='produtos'),
    path('funcionarios/', views.funcionarios_view, name='funcionarios'),
    path('estabelecer_acao/', views.listAcao_view, name='estabelecer_acao'),
    path('relatorios/', views.relatorios_view, name='relatorios'),
    path('politica/', views.politica_view, name='politica'),
    path('estatisticas/', views.estatisticas_view, name='estatisticas'),
    path('historico/', views.historico_view, name='historico'),
    path('addAcao/', views.addAcao, name='addAcao'), 
    path('addProdutos/', views.addProdutos, name='addProdutos'),
    path('addFuncionarios/', views.addFuncionario, name='addFuncionarios')

]
