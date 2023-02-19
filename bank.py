from last import BankAccount
customer_dict = {}
mobile_acc_link = {}
def new_cust():
    name = input('Enter the name of customer: ')
    mobile = int(input('Enter the mobile number of customer: '))
    money = int(input('Enter the initial deposit amount: '))
    if money <= 500:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = BankAccount(name=name, mobile=mobile, money=money, pin=pin)
    customer_dict[customer.acc_num] = customer
    mobile_acc_link[customer.mobile] = customer.acc_num
    customer_dict[customer.acc_num].save_data()
    print('New User Created!')
    print(
        f'Welcome {customer.name} to Corporate Bank. {customer.acc_num} is your account number')


def login():
    account_no = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin:
        print(f'\n{customer_dict[account_no].name} Logged in')
        customer_dict[account_no].show_acc_data()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        print("Press 1 for deposit:")
        print("Press 2 for withdrawl:")
        print("Press 3 for money transfer:")
        print("Press 4 to log out")
        choose_login_menu = int(input())
        if choose_login_menu == 1:
            customer_dict[account_no].deposit()
        elif choose_login_menu == 2:
            customer_dict[account_no].with_drawl()
        elif choose_login_menu == 3:
            mobile = int(input('Enter the mobile number of recepient: '))
            if mobile in mobile_acc_link.keys():
                other = mobile_acc_link[mobile]
                customer_dict[account_no].payment(customer_dict[other])
            else:
                print(
                    'The mobile number you have enter does not have an account associated with it')
        elif choose_login_menu == 4:
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        customer_dict[account_no].show_acc_data()


while True:
    print("Welcome to the menu!")
    print("press 1 for creating a new customer:")
    print("press 2 for logging in as an existing customer:")
    print("press 3 for displaing number of customer:")
    print("press 4 for Exit")
    choose_menu = int(input())
    if choose_menu == 1:
        print('Create user')
        new_cust()
    elif choose_menu == 2:
        login()
    elif choose_menu == 3:
        print('There currently', BankAccount.no_of_cust,
              'customers in Corporate bank.')
    elif choose_menu == 4:
        print('Exited')
        break
    else:
        print('Invalid input try again')
