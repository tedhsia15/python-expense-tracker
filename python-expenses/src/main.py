'''

This program takes all expenses and summarizes spending by month.
Developed by Teddy Hsia in onlineGDB.

'''
import sys
import csv
from ExpenseHelper import Expense
from ExpenseHelper import convertStringToDateTime
from datetime import datetime
    
#Function processInputCSV()    
def processInputCSV(expenseList):
    #Import CSV and check if CSV has lines
    try:
        with open('../../../Downloads/PythonProjectImport.csv') as csvFile:
            firstChar = csvFile.read(1)
            if not firstChar:
                print("The CSV file is empty")
                sys.exit()
            
            #create reader to read csv
            reader = csv.reader(csvFile, delimiter = ',')
            #skip the first row since they are column headers
            next(reader)
            
            #For every line in CSV
            for row in reader:
                #Create expense object
                #    On expense object
                #        Check if null and Set attributes for each expense
    
                name = row[0]
                category = row[1]
                amount = row[2]
                date = row[3]
            
                expense = Expense(name, amount, category, date)
                
                #Save expense to list of expenses
                expenseList.append(expense)
                
            #return List of Expenses
            return expenseList
            
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit("File not found")
        
    except ValueError as e:
        print("Error parsing data: " + e)
        sys.exit("Error parsing data")

#Expense List = []
expenseList = []

processInputCSV(expenseList)

#Total Expenses = 0
totalExpenses = 0

#Category and Expense Dictionary = {}
catExpenseDictionary = {}

#Set variable for today’s date
todayDateTime = datetime.now()

#Set variable for earliest date as a blank date
earliestDate = todayDateTime

#For each expense in the list
for expense in expenseList:
#    Check the expense date
#          if earliest expense date is not blank or the current expense date is earlier
#              set earliest expense date to current expense date
    date = expense.getDate()
    date = convertStringToDateTime(date)
    if earliestDate != None and date < earliestDate:
        earliestDate = date 
        
#   category = expense category
    category = expense.getCategory()
    
#   expenseAmount = expense cost
    amount = expense.getAmount()
    
    #If list category does not already exist in 
    if category in catExpenseDictionary:
        #Access dictionary value at category key
        #Add the expense amount to the existing value in the dictionary
        currentAmount = catExpenseDictionary[category]
        catExpenseDictionary[category] = amount + currentAmount
        
    #Else 
    #Add Dictionary key as category and value as expense   
    else:
        catExpenseDictionary.update({category:amount})

#For each dictionary entry in the category and expense dictionary
for key in catExpenseDictionary:
#    Print “total expense for category as of “ and add today’s date
    print("Total Expenses for " + key + " as of " + todayDateTime.strftime("%m-%d-%Y") + ":")
#    Print Dictionary value with “: ” and print dictionary value
    print(catExpenseDictionary[key])