from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(get_user_model().USERNAME_FIELD, kwargs.get(get_user_model().EMAIL_FIELD))
        if username is None or password is None:
            return
        try:
            user = get_user_model()._default_manager.get(
                #Q(username__exact=username) | (Q(email__iexact=username) & Q(email_verified=True))
                Q(email__iexact=username) & Q(email_verified=True)
            )
        except get_user_model().DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            get_user_model()().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user