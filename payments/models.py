from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class PaymentSchedule(models.Model):
    data_pagamento = models.DateField()  
    permite_recorrencia = models.BooleanField(default=False)  
    quantidade_recorrencia = models.IntegerField(null=True, blank=True)  
    intervalo_recorrencia = models.IntegerField(null=True, blank=True) 
    status_recorrencia = models.CharField(max_length=50)  
    agencia = models.IntegerField() 
    conta = models.IntegerField()  
    valor_pagamento = models.DecimalField(max_digits=10, decimal_places=2)  

    def clean(self):
        if self.data_pagamento > timezone.now().date():
            raise ValidationError("A data de pagamento não pode ser no futuro.")

    def __str__(self):
        return f"Pagamento {self.valor_pagamento / 100} na agência {self.agencia}, conta {self.conta}"
