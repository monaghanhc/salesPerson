# Name: Hunter Monaghan

# hw5.py

# Problem: SalesPerson and his Sales

# Certification of Authenticity:

# <include one of the following>

# I certify that this lab is entirely my own work.

# I certify that this lab is my own work, but I

# discussed it with: 

class SalesPerson:
    #Constructor
    def __init__(self, name, listSales):
        self.name = name
        self.listSales = listSales
    #Getter 
    def getName(self):
        return self.name 

    def getListSales(self):
        return self.listSales 
    #Setter
    def setName(self, name):
        if name == str:
            self.name = name

    def setListSales(self, listSales):
        if listSales == float:
            self.listSales = listSales
    #Enter the parameter value into the list of sales
    def enterSale(value):
        listSales += value
        return listSales
        
    #total of sales
    def totalSales():
        total = sum(listSales)
        return total

    def highestSale():
        Sales = listSales.sort()
        answer = max(listSales)
        return answer
        
    def metQuote(quota):
        quota = 2221
        if listSales > quota:
            return True
        else:
            return False
        
    def sortSales():
        for minVal in range(len(listSales)):
            minIndex = minVal
            for val in range(minVal + 1, len(listSales)):
                if listSales[minIndex] > listSales[sales]:
                    minIndex = sales

            listSales[minVal], listSales[minIndex] = listSales[minIndex], listSales[minVal]

    def findSale(value):
        for i in range(len(listSale)):
            if listSale[i] == value:
                return True
            return False
    
    
        
        
        
        
        
            
        

   
        


        
