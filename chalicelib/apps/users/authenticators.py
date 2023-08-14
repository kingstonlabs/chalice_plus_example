import os

from chalice_plus.authenticators import CognitoAuthenticator
from chalicelib.apps.users.models import User


class CustomCognitoAuthenticator(CognitoAuthenticator):
    def get_user(self):
        if self.user_id:
            return self.session.get(User, self.user_id)

    def get_user_id(self):
        if 'AWS_CHALICE_CLI_MODE' in os.environ:
            # Ensure this user id exists in the local database
            return "14c0b40c-c2fa-4a93-bb3d-a7d898d86706"
        return super().get_user_id()
