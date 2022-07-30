from rest_framework.permissions import SAFE_METHODS, BasePermission


# permissions what I wrote, but it's no need)))
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
