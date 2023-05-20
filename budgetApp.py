class Category:
    def __init__(self, category) :
        self.category = category
        self.ledger = []
        categories.append(self)

    def deposit(self, amount, description = '') :
        self.ledger.append({"amount": amount, "description": description})



    def withdraw(self, amount, description = '') :
        amount = amount
        # calculations for possibility of withdraw (enough money)
        if self.check_funds(amount) == False :
            print('not enough founds')
            return False
        else :
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self) :
        i = 0
        balance = 0
        for cash in self.ledger :
            balance += self.ledger[i]['amount']
            i += 1
        return balance

    def transfer(self, amount, category) :

        if self.check_funds(amount) == False :
            print('not enough founds')
            return False
        else :
            
            self.ledger.append({"amount": -amount, "description": f'Transfer to {category}'})
            i = 0
            for b in categories :
                if categories[i].category == category :
                    categories[i].ledger.append({"amount": amount, "description": f'Transfer from {self.category}'})
                i += 1
            return True



    def check_funds (self, amount) :
        # calculations for possibility of withdraw (enough money)
        if self.get_balance() < amount :
           # print('not enough foundshhh')
            return False
        else :
            return True

    

    



categories = []

# TESTING :D
bum = Category('Food')

bum.deposit(10, 'alle')
bum.deposit(20, 'kink')
#bum.withdraw(40, 'ales')
print(bum.get_balance())

bim = Category('Clothes')

bim.deposit(50, 'krrr')
bim.deposit(70, 'skk')
#bim.withdraw(40, 'ales')
bim.transfer(20, 'Food')
print(bim.get_balance())
print(bim.ledger)
print(bum.ledger)

#print(categories[0].ledger)

#def create_spend_chart(categories):