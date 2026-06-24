from django.db import models
from apps.customers.models import Customer
from apps.stores.models import Store


from services.idgenerator_svc import generate_OrderCode


class Order(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.PROTECT,
        verbose_name='Loja',
        db_index=True,
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name='Cliente',
        db_index=True,
    )
    name_customer = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Nome do cliente'
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    observation = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Observação'
    )
    address = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Endereço'
    )
    latitude = models.DecimalField(
        blank=True, 
        null=True,
        max_digits=20, 
        decimal_places=6,
        verbose_name='Latitude'
    )
    longitude = models.DecimalField(
        blank=True, 
        null=True,
        max_digits=20, 
        decimal_places=6, 
        verbose_name='Longitude'
    )
    house_number = models.CharField(
        blank=True,
        null=True,
        verbose_name='Número da casa'
    )
    total = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Total'
    )
    subtotal = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Subtotal'
    )
    remaining = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Troco'
    )
    payment_method = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Pago com'
    )
    rate_delivery = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        verbose_name='Taxa de Entrega'
    )
    code = models.CharField(
        max_length=20,
        unique=True,
        default=generate_OrderCode,
        verbose_name='Código'
    )
    status = models.BooleanField(
        default=False,
        verbose_name='Entregue'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    itens = models.JSONField(
        blank=True,
        null=True,
        verbose_name='Lista de Itens'
    )

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name_customer[:10]} - {self.code[:5]}"
