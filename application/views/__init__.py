from application.views.users_views import api as user_namespace
from application.views.phones_views import api as phone_namespace
from application.views.emails_views import api as email_namespace

__all__ = [
    "user_namespace",
    "phone_namespace",
    "email_namespace",
]
