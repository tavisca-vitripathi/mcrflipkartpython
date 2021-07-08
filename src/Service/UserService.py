from src.modals.user import User


class UserService(object):
    Registered_users = []

    def __init__(self):
        pass

    def register_user(self, name):
        user = User(name)
        self.__class__.Registered_users.append(user)
