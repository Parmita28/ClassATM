class atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber
    def withdrawal(self):
        print("CashWithDrawal")
    def enquiry(self):
        print("BalanceEnquiry")
ATM=atm("cardnumber","pinnumber")
print("Enter Your ATM Card Number")
print("Enter Your Pin Number")