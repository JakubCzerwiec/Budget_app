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
         #   print('not enough founds')
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
          #  print('not enough founds')
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

# ------ PRINTING OBJECT -------
    def __str__(self):
        final_str = ''

        # ----- Category name
        str_name = ''
        cat_name_len = len(self.category)
        str_name = ''
        coef = int((30 - cat_name_len) / 2)
      #  print(coef)
        for x in range(coef) :
            str_name += '*'
        str_name += self.category
        for x in range(coef) :
            str_name += '*'
        if coef % 2 != 0 :
            str_name += '*'
        else :
            str_name += ''
        str_name += '\n'
        final_str += str_name 

        # ------Ledger entries
        for entries in self.ledger :
            amount = entries['amount']
            formated_amount = str("{:.2f}".format(amount))
            cut_amount = formated_amount[:7]
            description = entries['description']
            spaces = ' ' * (23 - len(description) + (7 - len(cut_amount)) )
            final_str += f'{description[:23]}{spaces}{cut_amount}\n'
        
        # ------Balance
        formated_balance = "{:.2f}".format(self.get_balance())
        final_str += f'Total: {formated_balance}'
            
        return final_str

categories = []



# TESTING :D
bum = Category('Food')
'''
bum.deposit(2000, 'alle')
#bum.deposit(20, 'kink')
bum.withdraw(10, 'ales')

bim = Category('Clothes')

bim.deposit(100, 'krrr')
#bim.deposit(70, 'skk')
bim.withdraw(40, 'ales')
bim.transfer(20, 'Food')

funnyStuff = Category('Funny stuff I like')
funnyStuff.deposit(300, 'pocket')
funnyStuff.withdraw(50, 'supid')

brum = Category('sweeeets')
brum.deposit(60, 'mommy')
brum.withdraw(30, 'candies')

testowa = Category('1234567890123456789')
testowa.deposit(200000000000, 'salary')
testowa.withdraw(44.56, 'rent')
testowa.transfer(16.44, 'sweeeets')
#print(categories[0].ledger)
#print(categories[1].ledger)

#print(categories[0].ledger)
'''


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

      #  print(f'we spent {-this_category_expences} on {category_name}')
        expence = Expence(this_category_expences, category_name, 0)

    #print(expences[0].how_much, expences[1].how_much)    

    total_spent = 0
    i = 0
    for a in expences :
        total_spent += expences[i].how_much
        i += 1
 #   print('total spent', total_spent)

    j = 0
    for b in expences :
        percent = math.floor(expences[j].how_much / total_spent * 100)
        expences[j].percent = percent
        j += 1


    # ------ Printout -----
  #  print('Percentage spent by category')
    # ------ Print %%%% Table -----

    start_value = 100
    while start_value >= 0 :
        to_print = ''
        pref = ''
        if 0 < start_value < 100 :
            pref += ' '
        elif start_value == 0 :
            pref += '  '
        for exp in expences :
            if exp.percent >= start_value :
                to_print += ' o '
            else :
                to_print += '   '
        print(f'{pref}{start_value}|{to_print}')
        start_value -= 10



    # ----- Print categories ------
    a = 0
    b = 0
    
    # find longest category before printing
    longest_cat = []
    for exp in expences :
        longest_cat.append(len(exp.on_what))
    print('   ','-' * ((len(categories) * 3) + 1))

    i = 0
    while b < max(longest_cat): 
        
        to_print = '     '

        for exp in expences :
            try :
                to_print += f'{exp.on_what[i]}  '
            except IndexError :
                to_print += '   '
            
        print(to_print)
        i += 1
        b += 1
        
create_spend_chart(categories)
