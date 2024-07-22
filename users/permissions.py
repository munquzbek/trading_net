from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """
    Custom permission to only allow active employees to access the API,
    and has network connection.
    """
    def has_permission(self, request, view):
        # check permission that user exists, authenticated, active and network not None
        if request.user and request.user.is_authenticated and request.user.is_active:
            if request.user.network:
                return True
        return False
