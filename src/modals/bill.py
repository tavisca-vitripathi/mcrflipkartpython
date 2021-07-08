class Bill(object):
    def __init__(self, amount, contributions, id=None, register_by=None , split_share=None):
        self.amount = amount
        self.contributions = contributions
        self.id = id
        self.split_share = split_share
        self.register_by = register_by
        self.indiviual_user_amount = {}

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def set_contribution(self, contributions):
        self.contributions = contributions

    def get_contribution(self):
        return self.contributions

    def get_registerd_by(self):
        return self.register_by

    def set_registered_by(self, register_by):
        self.register_by = register_by

    def set_indiviual_user_amount(self, name, amount):
        self.indiviual_user_amount[name] = amount

    def get_indiviual_user_amount(self, name):
        if self.indiviual_user_amount.get(name) is not None:
            return self.indiviual_user_amount[name]
        return None