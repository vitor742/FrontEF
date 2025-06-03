from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('produtos/', views.listProdutos_view, name='produtos'),
    path('funcionarios/', views.listFuncionarios_view, name='funcionarios'),
    path('estabelecer_acao/', views.listAcao_view, name='estabelecer_acao'),
    path('relatorios/', views.relatorios_view, name='relatorios'),
    path('politica/', views.politica_view, name='politica'),
    path('estatisticas/', views.estatisticas_view, name='estatisticas'),
    path('historico/', views.historico_view, name='historico'),
    path('addAcao/', views.addAcao, name='addAcao'), 
    path('addProdutos/', views.addProdutos, name='addProdutos'),
    path('addFuncionarios/', views.addFuncionarios, name='addFuncionarios'),
    path('delete_acao/', views.delete_acao, name='delete_acao'),
    path('delete_produto/', views.delete_produto, name='delete_produto'),

]
