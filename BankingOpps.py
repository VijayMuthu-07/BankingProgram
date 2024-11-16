class Bank():
    def __init__(self,name):
        self.customers = {}
        self.name = name
    def create_account(self,account_number,initial_balance):
        if account_number in self.customers:
            print("Account Number Already Exists")
        else:
            self.customers[account_number] = initial_balance
            print("Account Created Successfully")
    def make_deposit(self,acc_num,damt):
        if acc_num in self.customers:
            self.customers[acc_num] += damt
            print("Deposit Successful")
        else:
            print("Account Number Does Not Exist")
    def make_withdrawal(self,acc_num,wamt):
        if acc_num in self.customers:
            if wamt <= self.customers[acc_num]:
                self.customers[acc_num] -= wamt
                print("Withdrawal Successful")
            else:
                print("Insufficient Funds")
        else:
            print("Account Number Does Not Exist")
    def check_balance(self,acc_num):
        if acc_num in self.customers:
            print(f"Account Number: {acc_num}")
            print(f"Account Balance: {self.customers[acc_num]} Rs")
    @staticmethod
    def is_bank(bankname):
        if bankname in ["HDFC","BOB","AXIS"]:
            return True
        else:
            return False

HDFC = Bank("HDFC")
BOB = Bank("BOB")
AXIS = Bank("AXIS")

def bank_opperation(bank_name):
    is_running=True
    while is_running:
        print("*"*20)
        print(f"{bank_name.name}")
        print("*"*20)
        print("1.Create Account")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Account Balance")
        print("5.Exit")
        print("*"*20)
        choice=input("Enter your option: ")
        match choice:
            case "1":
                acc = input("Enter account number: ")
                try:
                    amt = float(input("Enter initial balance: "))
                except ValueError:
                    print("Please enter a valid intial balance")
                    continue
                except Exception:
                    print("Something went wrong")
                    continue
                finally:
                    pass
                if amt <= 0:
                    print("initial balance must be greater than zero")
                    continue
                bank_name.create_account(acc,amt)
            case "2":
                acc = input("Enter account number: ")
                try:
                    amt = float(input("Enter deposit account: "))
                except ValueError:
                    print("Please enter a valid intial balance")
                    continue
                except Exception:
                    print("Something went wrong")
                    continue
                finally:
                    if amt <= 0:
                        print("deposit amount must be greater than zero")
                        continue
                bank_name.make_deposit(acc,amt)
            case "3":
                acc = input("Enter account number: ")
                try:
                    amt = float(input("Enter withdrawal amount: "))
                except ValueError:
                    print("Please enter a valid intial balance")
                    continue
                except Exception:
                    print("Something went wrong")
                    continue
                finally:
                    if amt <= 0:
                        print("withdrawal amount must be greater than zero")
                        continue
                bank_name.make_withdrawal(acc,amt)
            case "4":
                acc = input("Enter account number: ")
                bank_name.check_balance(acc)
            case "5":
                is_running=False
            case _:
                print("Error: That is not a valid choice")

def main():
    bank = input("Enter your bank name: ").upper()
    if Bank.is_bank(bank):
        match bank:
            case "HDFC":
                bank_opperation(HDFC)
            case "BOB":
                bank_opperation(BOB)
            case "AXIS":
                bank_opperation(AXIS)
    else:
        print("Bank does not exist")

if __name__ == '__main__':
    main()