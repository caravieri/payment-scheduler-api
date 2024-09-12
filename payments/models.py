from django.db import models

class PaymentSchedule(models.Model):
    data_pagamento = models.DateField()  
    permite_recorrencia = models.BooleanField(default=False)  
    quantidade_recorrencia = models.IntegerField(null=True, blank=True)  
    intervalo_recorrencia = models.IntegerField(null=True, blank=True)  
    status_recorrencia = models.CharField(max_length=50)  
    agencia = models.IntegerField()  
    conta = models.IntegerField()  
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return f"Pagamento de {self.valor_pagamento} na agência {self.agencia}, conta {self.conta} para {self.data_pagamento}"
