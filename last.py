from openpyxl import  Workbook


class BankAccount:
    acc_num = 10000
    no_of_cust = 0

    def __init__(self, name, mobile, money, pin):
        self.name = name
        self.mobile = mobile
        self.money = money
        self.pin = pin
        BankAccount.acc_num += 1
        BankAccount.no_of_cust += 1
        self.account_number = BankAccount.acc_num
        self.data = {
            'name': self.name,
            'mobile': self.mobile,
            'money': self.money,
            'pin': self.pin,
            'account_number': BankAccount.acc_num,

        }
        

    def show_acc_data(self):
        print(
            f"User :{self.name}\tAccount No:{self.account_number}\tBalance:${self.money} ")

    def deposit(self):
        amount = int(input("Enter the deposit amount : "))
        if amount > 0:
            self.money = self.money + amount
            print(f"tranaction completed. Current money : ${self.money}")
        else:
            print("invalid amount")

    def with_drawl(self):
        amount = int(input("Enter the deposit amount : "))
        if amount <= self.money and amount > 0:
            self.money = self.money - amount
            print(f"tranaction completed. Current money : ${self.money}")
        else:
            print("invalid amount")

    def payment(self, other):
        amount = int(input("Enter the payment :"))
        if amount <= self.money and amount > 0:
            self.money = self.money - amount
            other.money = other.money + amount
            print(f"tranaction completed. Current money : ${self.money}")
        else:
            print("invalid amount")

    def save_data(self):
        work_book = Workbook()
        work_sheet = work_book.active
        acc_keys = list(self.data.keys())
        heading = list(acc_keys)
        work_sheet.append(heading)
        acc_name = list(self.data.values())
        work_sheet.append(acc_name)

        work_book.save(f'{acc_name[0]}.xlsx')
