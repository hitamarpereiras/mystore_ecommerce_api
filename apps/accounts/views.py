from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.accounts.serializers import UserSerializer
from apps.accounts.models import User

class AccountViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return User.objects.all().order_by('-created_at')

        return User.objects.filter(user=user).order_by('-created_at')