#Projekt magazyn
import csv

products_names = ["Milk","Sugar","Flour","Coffee"]
quantities = [120,1000,12000,25]
units = ["l","kg","kg","kg"]
prices = [2.3,3,1.2,40]

sold_products = []
sold_quantities = []
sold_units = []
sold_prices = []

sold_items = [sold_products,sold_quantities,sold_units,sold_prices]


items = {'Name': products_names, 'Quantity': quantities, 'Unit': units, 'UnitPrice (PLN)': prices}

def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t----\t\t----\t----------")
    for name,quantity,unit,price in zip(products_names,quantities,units,prices):
        print(f'{name}\t{quantity}\t\t{unit}\t{price}')

def add_item():
    print("Adding to warehouse...")
    name = str(input('Item name: '))
    products_names.append(name)
    quantity = int(input('Item quantity: '))
    quantities.append(quantity)
    unit_name = str(input('Item unit of measure Eg. l,kg,pcs: '))
    units.append(unit_name)
    unit_price = float(input('Item price in (PLN): '))
    prices.append(unit_price)
    print("Successfully added to warehouse. Current status:")
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t----\t\t----\t----------")
    for name,quantity,unit,price in zip(products_names,quantities,units,prices):
        print(f'{name}\t{quantity}\t\t{unit}\t{price}')

def get_costs():
    with open('magazyn_items.csv', 'r')as itemsfile:
        itemsfile = csv.reader(itemsfile)
        headers = next(itemsfile)
        item_quantities = []
        item_prices = []
        
        
        for wiersz in itemsfile:
            item_quantities.append(wiersz[1])
            item_prices.append(wiersz[3])       
        for i in range(len(item_quantities)):
            item_quantities[i] = float(item_quantities[i])
        for i in range(len(item_prices)):
            item_prices[i] = float(item_prices[i])
        print(item_quantities)  
        print(item_prices)
        costs = 0      
        for i in range(len(item_prices)):   
            count = 0
            count = item_quantities[i]*item_prices[i]
            costs = costs + count         
        print("Total count :", costs)
        #print(costs)

def get_income():
    with open('magazyn_sales.csv', 'r')as salefile:
        salefile = csv.reader(salefile)
        headers = next(salefile)
        sale_quantity = []
        sale_price = []
        income = 0
        for wiersz in salefile:
            sale_quantity.append(wiersz[1])
            sale_price.append(wiersz[3])
        for i in range(len(sale_quantity)):
            sale_quantity[i] = int(sale_quantity[i])
        for i in range(len(sale_price)):
            sale_price[i] = float(sale_price[i])
        for i in range(len(sale_quantity)):
            count = 0
            count = float(sale_quantity[i]*sale_price[i])
            income += count
        print(income)

def show_revenue():
    with open('magazyn_items.csv', 'r')as itemsfile:
        itemsfile = csv.reader(itemsfile)
        headers = next(itemsfile)
        item_quantities = []
        item_prices = []
        
        
        for wiersz in itemsfile:
            item_quantities.append(wiersz[1])
            item_prices.append(wiersz[3])       
        for i in range(len(item_quantities)):
            item_quantities[i] = float(item_quantities[i])
        for i in range(len(item_prices)):
            item_prices[i] = float(item_prices[i])
        print(item_quantities)  
        print(item_prices)
        costs = 0      
        for i in range(len(item_prices)):   
            count = 0
            count = item_quantities[i]*item_prices[i]
            costs = costs + count         
        
        
    with open('magazyn_sales.csv', 'r')as salefile:
        salefile = csv.reader(salefile)
        headers = next(salefile)
        sale_quantity = []
        sale_price = []
        income = 0
        for wiersz in salefile:
            sale_quantity.append(wiersz[1])
            sale_price.append(wiersz[3])
        for i in range(len(sale_quantity)):
            sale_quantity[i] = int(sale_quantity[i])
        for i in range(len(sale_price)):
            sale_price[i] = float(sale_price[i])
        for i in range(len(sale_quantity)):
            count = 0
            count = float(sale_quantity[i]*sale_price[i])
            income += count
        
    print("Revenue breakdown (PLN)")
    print("Income :",round(income,2))
    print("Costs: ",round(costs,2))
    print("----------\nRevenue: ", round(income - costs,2))


def sell_item(name): 
    
    if name in products_names:
        sold_items[0].append(name)
        quantity_sell = int(input("Quantity to sell: "))
        sold_items[1].append(quantity_sell)
        sold_items[2].append(units[products_names.index(name)])
        sold_items[3].append(prices[products_names.index(name)])
        value = int(quantities[products_names.index(name)])
        value -= quantity_sell
        quantities[products_names.index(name)] = value
        print(f"Successfully sold {quantity_sell} {units[products_names.index(name)]} of {name}")
        print("Name\tQuantity\tUnit\tUnit Price (PLN)")
        print("----\t----\t\t----\t----------")
        for name,quantity,unit,price in zip(products_names,quantities,units,prices):
            print(f'{name}\t{quantity}\t\t{unit}\t{price}')
      
    else:
        print("Element is not in stock")
    
def export_items_to_csv():
    with open('magazyn_items.csv', 'w', newline='')as csvfile:
        items = ['Name','Quantity','Unit','UnitPrice (PLN)']
        writer = csv.DictWriter(csvfile, fieldnames = items)
        writer.writeheader()
        for name,quantity,unit,price in zip(products_names,quantities,units,prices):
            writer.writerow({'Name': name, 'Quantity': quantity, 'Unit': unit, 'UnitPrice (PLN)': price})

def export_sales_to_csv():
    with open('magazyn_sales.csv', 'w', newline='') as csvfile:
        sold_items = ['Name','Quantity','Unit','UnitPrice (PLN)']
        writer = csv.DictWriter(csvfile, fieldnames = sold_items)
        writer.writeheader()
        for name,quantity,unit,price in zip(sold_products,sold_quantities,sold_units,sold_prices):
            writer.writerow({'Name': name, 'Quantity': quantity, 'Unit': unit, 'UnitPrice (PLN)': price})

def load_items_from_csv(fname):
    
    with open(fname, 'r')as przedmiotyCSV:
        products_names.clear()
        quantities.clear()
        units.clear()
        prices.clear()
        przedmiotyCSV = csv.reader(przedmiotyCSV)
        headers = next(przedmiotyCSV)
        for wiersz in przedmiotyCSV:               
            products_names.append(wiersz[0])
            quantities.append(wiersz[1])
            units.append(wiersz[2])
            prices.append(wiersz[3])
        print("Successfully loaded data from magazyn_items.csv.")
        
def interface(load_items_from_csv):   
    direct = input('What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit): ')
    
#Interface
    while direct != 'exit':
        
#Showing current    
        if direct == 'show':
            get_items()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")

#Adding items to warehouse
        elif direct == 'add':
            add_item()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")
        

#Selling items from warehouse   
        elif direct == 'sell':
            sell_item(name = input("Item name: "))
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")
        

#Profit monitoring
        elif direct == 'show_revenue':
            show_revenue()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")             

#Income
        elif direct == 'income':
            get_income()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")

#Costs
        elif direct == 'costs':
            get_costs()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")

#Saving
        elif direct == 'save':
            export_items_to_csv()
            export_sales_to_csv()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):") 


#Loading items
        elif direct == 'load':
            load_items_from_csv()
            direct = input("What would you like to do? (add,sell,show,show_revenue,income,costs,save,load,exit):")


#Exiting program
    else:
        print('Exiting... Bye!')
        exit(1)

if __name__ == "__main__":
    interface(load_items_from_csv(fname=input("File name: ")))


            




