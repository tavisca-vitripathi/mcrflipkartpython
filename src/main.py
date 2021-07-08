from src.Service.BillService import BillService
from src.Service.UserService import UserService
from src.Service.groupService import GroupService

if __name__ == "__main__":
    billservice = BillService()
    userservice = UserService()
    groupService = GroupService(billservice)

    userservice.register_user("mohit")
    userservice.register_user("ayush")
    userservice.register_user("saloni")
    userservice.register_user("sourav")

    groupService.CreateGroup("group1")
    groupService.CreateGroup("group2")

    groupService.Add_users_To_group(["mohit", "ayush", "saloni", "sourav"], "group1")
    groupService.Add_users_To_group(["mohit", "saloni"], "group2")

    groupService.Add_Bill(300, {'mohit': 250, 'ayush': 50, "sourav": 0}, "group1", "ayush")
    groupService.Add_Bill(100, {'mohit': 50, 'saloni': 50, }, "group2", "ayush")

    amount1 = groupService.Display_Balance('mohit', "group1")
    print(amount1)

    amount2 = groupService.Display_Balance('ayush','group1')
    print(amount2)

    amount3 = groupService.Display_Balance("sourav", 'group1')
    print(amount3)

    amount4 = groupService.Display_Balance('sourav','group2')
    print(amount4)





