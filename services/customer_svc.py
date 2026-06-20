from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.customers.models import Customer
from apps.users.models import User

from services import (
    validators,
    pillow_svc,
    supabase_svc
)


class CustomerService:

    @staticmethod
    @transaction.atomic
    def register_customer(validated_data):
        
        #Cria User + Customer, processa imagem e atualiza os campos adicionais
        
        image = validated_data.pop("image", None)
        username = validated_data.pop("username")
        email = validated_data.pop("email")
        password = validated_data.pop("password")

        # Verifica o Email
        if User.objects.filter(email=email).exists():
            raise ValidationError("Esse email já esta em uso!")
        
        # Verifica o username
        if User.objects.filter(username=username).exists():
            raise ValidationError("Esse username já existe!")

        # Criar User
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Criar Customer
        customer = Customer.objects.create(
            user=user,
            **validated_data
        )

        avatar_url = None
        avatar_path = None

        if image:
            try:
                validators.validate_image(image)
                buffer, ext = pillow_svc.process_image(image, 300, 300)

                upload = supabase_svc.upload_image(
                    file_bytes=buffer.getvalue(),
                    ext=ext,
                    bucket='clientes'
                )

                avatar_url = upload["url"]
                avatar_path = upload["path"]

            except Exception as e:
                raise ValidationError(f"Erro ao processar a imagem")

        # Atualizar a account
        customer.avatar_url = avatar_url
        customer.avatar_path = avatar_path
        customer.save()

        return customer