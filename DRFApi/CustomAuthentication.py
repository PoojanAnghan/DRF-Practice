from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print("🔐 CustomAuthentication called")

        username = request.GET.get('username')
        print(f"➡️ Username: {username}")

        if username is None:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('User not registered')
    
        return (user, None)

