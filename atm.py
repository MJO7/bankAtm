class AtmUser(object):
    def __init__(self, CashWithDrawl , BalanceEnquiry , depositedCheck = None):
        self.CashWithDrawl: CashWithDrawl
        self.BalanceEquiry: BalanceEnquiry
        self.depositedCheck: depositedCheck

    def CashWithDrawl(self , amount , withdrawedAmount):
        self.CashWithDrawl[amount] = withdrawedAmount
    def BalanceEnquiry(self , type , status):
        self.BalanceEnquiry[type] = status
    def depositedCheck(self , amount , TotalAmount):
        self.CashWithDrawl[amount] = TotalAmount
    def ProvideBankStatement(self):
        return sum(self.CashWithDrawl , self.depositedCheck)
#defining some people who used atm
harry = AtmUser("Harry" , 10000 , "none" , 10500)
lucy = AtmUser("Lucy" , 5000 , "none" , 29500)
