#Name: Nguyen Vo
#ID: 1673509



import csv                         #working with csv files
from datetime import datetime      #this will allow accessing time for later use

#initialize class for every output
class InventoryReports:
    def __init__(self, item_list):
        self.item_list = item_list      #provide list to create new file


    #Part a
    #Create FullInventory.csv for entire inventory
    #Following order ID, manufacture name, item type, price, service date, damaged
    def fullInventory(self):
        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])              #sorted alphabetically by manufacture
            for item in keys:
                id = item
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                serviceDate = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate, damaged))

    #Part b
    #Create Inventorylist for each item type
    #This will produce 3 seperate cvs files: PhoneInventory, TowerInventory, LaptopInventory
    #Following order ID, manufacture, price, service date, and if damaged
    def inventoryList(self):
        items = self.item_list
        types = []
        keys = sorted(items.keys())                 #the items sorted by ID
        for item in items:
            itemType = items[item]['item_type']
            if itemType not in types:
                types.append(itemType)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open('Inventorylist' + '-' + file_name, 'w') as file:
                for item in keys:
                    id = item
                    manufacture = items[item]['manufacturer']
                    price = items[item]['price']
                    serviceDate = items[item]['service_date']
                    damaged = items[item]['damaged']
                    itemType = items[item]['item_type']
                    if type == itemType:
                        file.write('{},{},{},{},{}\n'.format(id, manufacture, price, serviceDate, damaged))

    #Part c
    #Crate PastServiceDateInventory.csv
    #Following order ID, manufacture, item type, price, service date
    def pastService(self):
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date())        #sorted date from oldest to most recent
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                serviceDate = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(serviceDate, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:                                                      #list if it damaged
                    file.write('{},{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate, damaged))

    #Part d
    #Create DamagedInventory.csv for items that are damaged
    #Following order ID, manfacture, item type, price, service date
    def damagedInventory(self):
        items = self.item_list
        #order to file based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)     #order being reserved so that it sort from expensive to cheap
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manufacture = items[item]['manufacturer']
                itemType = items[item]['item_type']
                price = items[item]['price']
                serviceDate = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:                                      #condition to write for damaged items
                    file.write('{},{},{},{},{}\n'.format(id, manufacture, itemType, price, serviceDate))


if __name__ == '__main__':           #main program
    items = {}
    files = ['ManufacturerList(1).csv', 'PriceList(1).csv', 'ServiceDatesList(1).csv']        #create list of input files and read every files
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufacture = line[1]
                    itemType = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufacture.strip()
                    items[item_id]['item_type'] = itemType.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    serviceDate = line[1]
                    items[item_id]['service_date'] = serviceDate

    inventory = InventoryReports(items)
    # Create all the output files
    inventory.fullInventory()
    inventory.pastService()
    inventory.damagedInventory()
    inventory.inventoryList()
