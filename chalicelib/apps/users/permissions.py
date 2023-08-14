class IsObjectOrAdmin:
    message = "User is not object being updated or admin"

    def has_permission(self, view):
        user = view.authenticator.user
        return user and (user.is_superuser or user.id == str(view.object.id))
