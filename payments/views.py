from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import PaymentSchedule
import json


@csrf_exempt
def listar_agendamentos(request):
    if request.method == 'GET':
        agendamentos = PaymentSchedule.objects.all()
        dados = [{
            'id': agendamento.id,
            'data_pagamento': agendamento.data_pagamento,
            'permite_recorrencia': agendamento.permite_recorrencia,
            'quantidade_recorrencia': agendamento.quantidade_recorrencia,
            'intervalo_recorrencia': agendamento.intervalo_recorrencia,
            'status_recorrencia': agendamento.status_recorrencia,
            'agencia': agendamento.agencia,
            'conta': agendamento.conta,
            'valor_pagamento': agendamento.valor_pagamento / 100  
        } for agendamento in agendamentos]
        return JsonResponse(dados, safe=False)

    elif request.method == 'POST':
      
        try:
            dados = json.loads(request.body)
            valor_pagamento = float(dados['valor_pagamento']) * 100  
            agendamento = PaymentSchedule(
                data_pagamento=dados['data_pagamento'],
                permite_recorrencia=dados['permite_recorrencia'],
                quantidade_recorrencia=dados['quantidade_recorrencia'],
                intervalo_recorrencia=dados['intervalo_recorrencia'],
                status_recorrencia=dados['status_recorrencia'],
                agencia=dados['agencia'],
                conta=dados['conta'],
                valor_pagamento=int(valor_pagamento)  
            )
            agendamento.full_clean()  
            agendamento.save()
            return JsonResponse({'message': 'Agendamento criado com sucesso!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)
@csrf_exempt
def detalhar_agendamento(request, id):
    try:
        agendamento = PaymentSchedule.objects.get(id=id)
    except PaymentSchedule.DoesNotExist:
        return JsonResponse({'error': 'Agendamento não encontrado'}, status=404)
    
    if request.method == 'GET':
        dados = {
            'data_pagamento': agendamento.data_pagamento,
            'permite_recorrencia': agendamento.permite_recorrencia,
            'quantidade_recorrencia': agendamento.quantidade_recorrencia,
            'intervalo_recorrencia': agendamento.intervalo_recorrencia,
            'status_recorrencia': agendamento.status_recorrencia,
            'agencia': agendamento.agencia,
            'conta': agendamento.conta,
            'valor_pagamento': agendamento.valor_pagamento / 100
        }
        return JsonResponse(dados)
    
    return JsonResponse({'error': 'Método não permitido'}, status=405)

@csrf_exempt
def deletar_agendamento(request, id):
    try:
        agendamento = PaymentSchedule.objects.get(id=id)
    except PaymentSchedule.DoesNotExist:
        return JsonResponse({'error': 'Agendamento não encontrado'}, status=404)
    
    if request.method == 'DELETE':
        agendamento.delete()
        return JsonResponse({'message': 'Agendamento deletado com sucesso!'}, status=204)
    return JsonResponse({'error': 'Método não permitido'}, status=405)
