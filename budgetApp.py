import math
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
bum.withdraw(10, 'ales')



bim = Category('Clothes')

bim.deposit(50, 'krrr')
bim.deposit(70, 'skk')
bim.withdraw(40, 'ales')
bim.transfer(20, 'Food')


#print(categories[0].ledger)

def create_spend_chart(categories):
    class Expence :
        def __init__(self, how_much, on_what, percent) :
            self.how_much = how_much
            self.on_what = on_what
            self.percent = percent
            expences.append(self)
    expences = []
    for category in categories :
        
        category_name = category.category
        this_category_expences = 0


        i = 0
        for a in category.ledger :
            if category.ledger[i]['amount'] < 0 :
                this_category_expences += category.ledger[i]['amount']
            i += 1

        print(f'we spent {-this_category_expences} on {category_name}')
        expence = Expence(this_category_expences, category_name, 0)

    print(expences[0].how_much, expences[1].how_much)    

    total_spent = 0
    i = 0
    for a in expences :
        total_spent += expences[i].how_much
        i += 1
    print('total spent', total_spent)

    j = 0
    for b in expences :
        percent = math.floor(expences[j].how_much / total_spent * 100)
        expences[j].percent = percent
        j += 1

    print(expences[1].percent, '%' )
    print(expences[0].on_what[0])

    # ------ Printout -----
    
    # ------ Print %%%% Table -----

    start_value = 100
    while start_value >= 0 :
        if expences[1].percent >= start_value :
            print(f'{start_value}| o')
        else :
            print(f'{start_value}|  ')
        start_value -= 10








    # ----- Print categories ------
    a = 0
    b = 0

    while b < len(expences[1].on_what): # find longest category before printing
        try :
            print(expences[a].on_what[b], expences[a+1].on_what[b])
            b += 1
        except IndexError:
            print(' ', expences[a+1].on_what[b])
            b +=1
'''
    print(expences[0].on_what[0], expences[1].on_what[0])
    print()
    print(expences[0].on_what[1], expences[1].on_what[1]) 
    print() 
    print(expences[0].on_what[2], expences[1].on_what[2]) 
    print() 
'''
            






create_spend_chart(categories)