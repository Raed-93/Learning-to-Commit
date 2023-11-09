class user:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def make_withdrawal(self, amount):
        if amount > 0 and amount >= self.balance:
         self.balacne -= amount

    def display_user_balance(self):
       print("User: %s, Balance:%d" % (self.name, self.balance))


    def transfer_money(self,amount,antheruser):
       if amount > 0 and amount >= self.balance:
         self.balacne -= amount
         antheruser.balance += amount
         print("transfer: %d, name: %s" % (amount,self.name))
       else:
          print("none")

          user1 = user("name","balance")
        
    
          


        