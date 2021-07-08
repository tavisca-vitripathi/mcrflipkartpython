import snoop
from src.modals.group import Group


class GroupService(object):
    Registerd_Groups = {}
    BillService = None

    def __init__(self, billservice: BillService):
        self.__class__.BillService = billservice

    def CreateGroup(self, name):
        group = Group(name)
        self.__class__.Registerd_Groups[name] = group

    def Add_users_To_group(self, users, group_name):
        if self.__class__.Registerd_Groups.get(group_name) is None:
            raise Exception("no such group exists")
        else:
            group = self.__class__.Registerd_Groups.get(group_name)
            group.set_users(users)

    def Add_Bill(self, amount, contributions: dict, group_name, registerd_by, split_share=None):
        if self.__class__.Registerd_Groups.get(group_name) is None:
            raise Exception("no such group exists")
        else:
            group = self.__class__.Registerd_Groups.get(group_name)
            bill = self.__class__.BillService.Add_Bill(amount, contributions, registerd_by, split_share)
            group.set_bill(bill)
            self.__class__.Registerd_Groups[group_name] = group
    @snoop
    def Display_Balance(self, user, group_name=None):
        amount = 0
        if group_name is not None:
            if self.__class__.Registerd_Groups.get(group_name) is None:
                raise Exception("no such group exists")
            else:
                group = self.__class__.Registerd_Groups.get(group_name)
                bills = group.get_bills()
                for bill in bills:
                    if bill.get_indiviual_user_amount(user) is not None:
                        amount += bill.get_indiviual_user_amount(user)
        else:
            for key in self.__class__.Registerd_Groups.keys():
                group = self.__class__.Registerd_Groups.get(key)
                bills = group.get_bills()
                for bill in bills:
                    if bill.get_indiviual_user_amount(user) is not None:
                        amount += bill.get_indiviual_user_amount(user)
        return amount
