from django.conf import settings
import jwt

from rest_framework.permissions import BasePermission


class Check_API_KEY_Auth(BasePermission):
    def has_permission(self, request, view):
        api_key_secret = request.META.get('HTTP_X_API_KEY')
        return api_key_secret == settings.API_KEY_SECRET
