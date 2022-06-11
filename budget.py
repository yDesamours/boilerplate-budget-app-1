from math import ceil

class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = list()
     
        
    def deposit(self, amount, description = ''):
        transaction = {
            "amount" : amount,
            "description" : description
        }
        self.ledger.append(transaction)
     
        
    def withdraw(self, amount, description = ''):
        possible = self.check_funds(amount)
        
        if possible :
            transaction = {
                "amount" : -amount,
                "description" : description
            }
            self.ledger.append(transaction)
            return True
        else:
            return False
     
        
    def get_balance(self):
        funds = 0
        
        for item in self.ledger:
             funds = funds + item['amount']
    
        return funds
        
        
    def check_funds(self, amount):
        funds = 0
        
        for item in self.ledger:
             funds = funds + item['amount']
             
        if funds >= amount:
            return True
        else:
            return False
            
            
    def transfer(self, amount, category):
        possible = self.check_funds(amount)
        
        if not possible:
            return False
            
        to = 'Transfer to ' + category.name
        fro = 'Transfer from ' + self.name
        category.deposit(amount, fro)
        self.withdraw(amount, to)

        return True
        
    
    def total_withdraw(self):
        total = 0
        
        for item in self.ledger:
            if item['amount'] < 0 :
                total += item['amount']
                
        return -total
                
        
    def __str__(self):
        title = self.name.center(30, '*')
        details = ''
        total = 'Total: {:.2f}'.format(self.get_balance())
        
        for item in self.ledger:
            description = item['description'][:23]
            amount = '{:.2f}'.format(item['amount'])[:7]
            
            details = details + '{:<23}'.format(description) + '{:>7}'.format(amount) +'\n'
            
        return title + '\n' + details + total
        

def bar(index, elem):
    if index < elem :
        return 'o'
    else :
        return ' '

def create_spend_chart(categories):
    spent , percents= list(), list()
    total_cat = len(categories)
    title = 'Percentage spent by category'
    
    for cat in categories :
        withdraw = cat.total_withdraw()
        spent.append(withdraw)
        
    total = sum(spent)
    
    for item in spent:
        percents.append(ceil(item/total*10))
    details = ''
    i = 10
    while i > -1:
        details = details + '{:>3}'.format(str(i * 10)) + '| '
        j = 0
        while j < total_cat:
            details = details + '{}  '.format(bar(i, percents[j]))
            j = j+1
        details = details + '\n'
        i = i - 1
    breaks = ' ' * 4 + '-' * (total_cat*3 + 1)
    
    category_names = []
    i = 0
    while i < total_cat:
        category_names.append(len(categories[i].name))
        i = i + 1
        
    maxlen = max(category_names)
    i = 0    
    while i < total_cat:
        category_names[i] = '{}{}'.format(categories[i].name,' '*(maxlen - len(categories[i].name))) 
        i = i + 1
        
    i = 0
    names = ''
    while i < maxlen:
        names = names + ' '*5
        j = 0 
        while j < total_cat:
            names = names + category_names[j][i] + ' ' * 2
            j = j + 1
        i = i + 1
        if i < maxlen:
            names = names + '\n'
        
        
        
    output = title + '\n' + details + breaks + '\n' + names
    return output