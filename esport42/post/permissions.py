from rest_framework import permissions
from tournoi.models import Tournament

class IsAdminOfSite(permissions.BasePermission):
    def has_permission(self, request, view):
        if request == 'GET' or permissions.IsAdminUser():
            return True
        return False

    def has_object_permission(self, request, view, post):
        if request.method == 'GET' or permissions.IsAdminUser():
            return True
        return False

class IsTornamentOrAdmin(permissions.BasePermission):
    def has_permission(self, request, id=None):
        if permissions.IsAdminUser or request.method == 'GET':
            return True
        item = Tournament.objects.get(id=request.ID)
        data = item.admin.all()
        if request.user in data:
            return True
        return False
    def has_object_permission(self, request, view, post):
        if request.method == 'GET' or permissions.IsAdminUser():
            return True
        return False