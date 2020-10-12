from hw5 import *

def main():
    #Test list number
    HunterSalesGuy = SalesPerson('Hunter', [])
    testSales = HunterSalesGuy.getListSales()
    print("Sales: ", testSales)

    #Test Name
    testName = HunterSalesGuy.getName()
    print("Name: ", testName)

    #Test EnterSale
    testEnterSale = HunterSalesGuy.enterSale()
    print("Entered Sale: ", testEnterSale)

    #Test totalSales
    testTotalSales = HunterSalesGuy.totalSales()
    print("Total Sales: ", testTotalSales)

    print("\nDone")
main()
