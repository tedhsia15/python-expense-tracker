'''
File for the Expense class
'''
from datetime import datetime
class Expense:
    def __init__(self, name, amount, category, date):
        self.name = name
        self.amount = float(amount)
        self.category = category
        self.date = date
        
    #returns name of expense
    def getName(self):
        return self.name
        
    #sets name if name exists
    def setName(self):
        if len(name) > 0:
            self.name = name
    
    #returns amount of expense
    def getAmount(self):
        return self.amount
    
    #sets amount if amount exists
    def setAmount(self):
        if amount != none:
            self.amount = amount
        
    #returns category of expense
    def getCategory(self):
        return self.category
        
    #sets category if category exists
    def setCategory(self):
        if len(category) > 0:
            self.category = category
        
    #returns date of expense
    def getDate(self):
        return self.date
        
    #sets date if date exists
    def setDate(self):
        if date != none:
            self.date = date
            
def convertStringToDateTime(dateTimeString):
    format = '%m-%d-%Y'
    dateTime = datetime.strptime(dateTimeString, format)
    
    return dateTime
        
    