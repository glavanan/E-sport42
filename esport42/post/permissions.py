from rest_framework import permissions

class IsAdminOfSite(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.user:
            return request.user.is_admin
        return False