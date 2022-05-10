#Projekt magazyn
products_names = ['Milk','Sugar','Flour','Coffee']
quantities = [120,1000,12000,25]
units = ['l','kg','kg','kg']
prices = [2.3,3,1.2,40]

tab = zip(products_names,quantities,units,prices)



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
    
    






def sell_item(name): 
    
    if name in products_names:
        quantity_sell = int(input("Quantity to sell: "))
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
    
        
        


direct = input('What would you like to do? ')



#Interface
while direct != 'exit':
#Showing current    
    if direct == 'show':
        get_items()
        direct = input("What would you like to do?")

#Adding items to warehouse
    elif direct == 'add':
        add_item()
        direct = input("What would you like to do?")
        

#Selling items from warehouse   
    elif direct == 'sell':
        sell_item(name = input("Item name: "))
        direct = input("What would you like to do?")
        
        
        
        

        
#Exiting program
else:
    print('Exiting... Bye!')
    exit(1)

