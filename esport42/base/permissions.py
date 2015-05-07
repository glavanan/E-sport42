from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, account):
        if request.user:
            return account == request.user
        return False

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'retrieve' or view.action == 'destroy' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.user:
            return request.user.is_staff or obj == request.user
        return False

