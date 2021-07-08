import snoop
from src.modals.bill import Bill


class BillService(object):
    def __init__(self):
        pass

    def Add_Bill(self, amount, contributions, registerd_by, split_share=None):
        bill = Bill(amount, contributions, register_by=registerd_by, split_share=split_share)
        if split_share is None:
            user_count = len(contributions)
            if user_count == 0:
                raise Exception("Invalid format")
            indiviual_share = amount / user_count
            for key in contributions.keys():
                amount_paid = indiviual_share - contributions[key]
                bill.indiviual_user_amount[key] = amount_paid
        else:
            user_count = len(contributions)
            if user_count == 1:
                raise Exception("Invalid format")
            for key in contributions.keys():
                indiviual_share = amount * split_share[key]
                amount_paid = indiviual_share - contributions[key]
                bill.indiviual_user_amount[key] = amount_paid
        return bill
