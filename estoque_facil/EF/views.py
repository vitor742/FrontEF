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

def politica_view(request):
    return render(request, 'politica/politica.html')

def relatorios_view(request):
    return render(request, 'relatorios/relatorios.html')

def addProdutos(request):
    if request.method == 'POST':
        db = initialize_firebase()

        nome_produto = request.POST.get('nomeProduto')
        qtd_produto = int(request.POST.get('qntCxProduto', 0))
        qtd_produtoPCx = int(request.POST.get('qntPCxProduto', 0))
        lote_produto = request.POST.get('loteProduto')
        data_fab = request.POST.get('dataFabProduto')
        data_val = request.POST.get('dataValProduto')

        doc_ref = db.collection("produtos").document()
        doc_ref.set({
            "nome_produto": nome_produto,
            "qtd_produto": qtd_produto,
            "lote_produto": lote_produto,
            "data_fabricacao": data_fab,
            "data_validade": data_val,
            "qtd_produtoPCx": qtd_produtoPCx
        })

        print("Produto cadastrado com sucesso!")  # Isso vai para o console

        return redirect('produtos')  # Isso redireciona o usuário de volta para a página
    else:
        return JsonResponse({"erro": "Método não permitido"}, status=405)

def addAcao(request):
    if request.method == 'POST':
        db = initialize_firebase()

        nome_acao = request.POST.get('nomeAcao')
        desc_acao = request.POST.get('descAcao')
        resp_acao = request.POST.get('respAcao')
        urge_acao = request.POST.get('urgeAcao')

        doc_ref = db.collection("tarefas").document()
        doc_ref.set({
            "nome_acao": nome_acao,
            "desc_acao": desc_acao,
            "resp_acao": resp_acao,
            "urge_acao": urge_acao,
        })

        print("Tarefa cadastrada com sucesso!")  # Isso vai para o console

        return redirect('estabelecer_acao')  # Isso redireciona o usuário de volta para a página
    else:
        return JsonResponse({"erro": "Método não permitido"}, status=405)

def listAcao_view(request):
    db = initialize_firebase()
    tarefas_ref = db.collection('tarefas')
    tarefas = tarefas_ref.stream()

    tarefas_list = []
    for tarefa in tarefas:
        tarefa_data = tarefa.to_dict()
        tarefa_data['id'] = tarefa.id
        tarefas_list.append(tarefa_data)

    return render(request, 'estabelecer_acao/estabelecer_acao.html', {'tarefas': tarefas_list})
    


def listProdutos_view(request):
    db = initialize_firebase()
    produtos_ref = db.collection('produtos')
    produtos = produtos_ref.stream()

    produtos_list = []
    for produto in produtos:
        produto_data = produto.to_dict()
        produto_data['id'] = produto.id
        produtos_list.append(produto_data)

    return render(request, 'produtos/produtos.html', {'produtos': produtos_list})


def home(request):
    return render(request,'funcionarios/funcionarios.html')
