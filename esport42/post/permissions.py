from rest_framework import permissions

class IsAdminOfSite(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.method == 'GET':
            return True
        if request.user.is_admin == True:
            return True
        return False