from django.shortcuts import render

def login(request):
    return render(request, 'login/login.html')

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def produtos_view(request):
    return render(request, 'produtos/produtos.html')

def funcionarios_view(request):
    return render(request, 'funcionarios/funcionarios.html')

def estatisticas_view(request):
    return render(request, 'estatisticas/estatisticas.html')

def historico_view(request):
    return render(request, 'historico/historico.html')

def acao_view(request):
    return render(request, 'estabelecer_acao/estabelecer_acao.html')

def politica_view(request):
    return render(request, 'politica/politica.html')

def relatorios_view(request):
    return render(request, 'relatorios/relatorios.html')