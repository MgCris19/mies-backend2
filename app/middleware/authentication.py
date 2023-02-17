from datetime import timedelta

from django.utils import timezone
from rest_framework.authentication import TokenAuthentication

from core.settings.base import TOKEN_EXPIRED_AFTER_SECONDS

from app.modelBase.enum import MESSAGE

class ExpiringTokenAuthentication(TokenAuthentication):
    expired = False
    # calcula tiempo de expiracion
    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(
            seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    # indica si expiró
    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    # verifica token
    def token_expire_handler(self, token):
        is_expire = self.is_token_expired(token)
        #print(is_expire)
        if is_expire:
            print('Token expiró')
            # expired = True
            # elimino y creo un token
            user = token.user
            token.delete()
            # token = self.get_model().objects.create(user = user)
        return is_expire#, token

    def authenticate_credentials(self, key):
        message, user, token = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)           
            user = token.user
        except self.get_model().DoesNotExist:
           
            message =  MESSAGE.UNAUTHORIZED     
            self.expired = True      
        
        if token is not None:
            if not token.user.is_active:
                message = MESSAGE.NOT_SESSION

            is_expired = self.token_expire_handler(token)

            if is_expired:
                message = MESSAGE.SESSION_EXPIRED
                self.expired = True
        return (user, token, message,self.expired)