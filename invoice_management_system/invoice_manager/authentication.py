from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

class TokenAuthentication(authentication.BaseAuthentication):
    """Authentication for Token """

    def authenticate(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise exceptions.AuthenticationFailed('Please Provide Token ')
        try:
            token_obj = Token.objects.get(key=token)
        except Token.DoesNotExist:
            exceptions.AuthenticationFailed('Invalid token.')
        return token_obj.user, None
