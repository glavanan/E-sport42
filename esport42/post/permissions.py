from rest_framework import permissions

class IsAdminOfSite(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.method == 'GET' or permissions.IsAdminUser():
            return True
        return False