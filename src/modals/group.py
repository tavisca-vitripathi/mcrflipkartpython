from src.modals.user import User


class Group(object):
    def __init__(self, name, group_id=None):
        self.users = []
        self.bills = []
        self.id = group_id
        self.name = name

    def get_users(self):
        return self.users

    def set_users(self, users):
        self.users = users

    def add_user(self, new_user: User):
        self.users.append(new_user)

    def get_bills(self):
        return self.bills

    def set_bill(self, bill):
        self.bills.append(bill)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
