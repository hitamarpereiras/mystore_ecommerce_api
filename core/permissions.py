from rest_framework.permissions import BasePermission

class IsOwnerOfSale(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'account'):
            return obj.account and obj.account.user == user
        
        return False
    
class IsOwnerOfBanner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'account'):
            return obj.account and obj.account.user == user
        
        return False
    
class IsOwnerOfOder(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if hasattr(obj, 'customer'):
            return obj.customer and obj.customer.user == user
        
        return False