from django.db import models
from django.conf import settings


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='customer',
        verbose_name='Cliente'
    )
    name = models.CharField(
        max_length=100, 
        verbose_name='Nome'
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone'
    )
    address = models.TextField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Endereço'
    )
    house_number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Número da casa'
    )
    coins = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Moedas de troca'
    )
    premium = models.BooleanField(
        default=False,
        verbose_name='Cliente Premium'
    )
    avatar_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='Avatar URL'
    )
    avatar_path = models.URLField(
        blank=True,
        null=True,
        verbose_name='Avatar Caminho'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em',
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.name}"
