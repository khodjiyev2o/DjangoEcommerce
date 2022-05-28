from rest_framework.authentication import TokenAuthentication as BaseTokenAuth


class TokenAuthentication(BaseTokenAuth):
    key = 'Bearer'
