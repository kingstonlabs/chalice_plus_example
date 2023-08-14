from chalice_plus.permissions import IsAdmin
from chalice_plus.views import RetrieveUpdateDeleteView, CreateListView

from chalicelib.apps.users.authenticators import CustomCognitoAuthenticator

from .models import User
from .permissions import IsObjectOrAdmin
from .schemas import UserSchema


class UserDetailView(RetrieveUpdateDeleteView):
    model = User
    schema_class = UserSchema
    authenticator_class = CustomCognitoAuthenticator
    permission_classes = {
        "patch": [IsObjectOrAdmin],
        "delete": [IsAdmin],
    }


class UserListView(CreateListView):
    model = User
    schema_class = UserSchema
    authenticator_class = CustomCognitoAuthenticator
