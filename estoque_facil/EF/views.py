from django.shortcuts import render, redirect
from django.http import JsonResponse
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from django.conf import settings

# Isso aqui é o que tá inicializando o firebase, NAO MEXE
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
        firebase_admin.initialize_app(cred)
    return firestore.client()

# Essa parte é a parte do login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        access_key = request.POST.get('access_key')

# I

        try:
            # Inicializa o Firestore
            db = initialize_firebase()

            # Verifica as credenciais no Firestore
            users_ref = db.collection('clients')
            query = users_ref.where('username', '==', username).where('access_key', '==', access_key).get()

            if query:
                # Se o usuário for encontrado e as credenciais estiverem corretas
                return JsonResponse({"message": "Login bem-sucedido!"}, status=200)
            else:
                return JsonResponse({"error": "Credenciais inválidas!"}, status=401)

        except Exception as e:
            return JsonResponse({"error": f"Erro ao autenticar: {str(e)}"}, status=500)

    return render(request, 'login.html')  # Renderiza o template de login

def login_view(request):
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
