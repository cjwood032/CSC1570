#retail_driver_Wood
#this program creates a class for retail items, and then outputs information for 3 items
#programmer: Christopher Wood
#date: 4/20/18
#program name: retail_driver
class RetailItem(): #define the class
    def __init__(self,Item_Desc,unit_Inv,Price): #run the init method
        self.Item_Desc=Item_Desc #define the item's description
        self.unit_Inv=unit_Inv #define the unit's inventory
        self.Price=Price #define the price
    def __str__(self): #defining the string method
        return self.Item_Desc #return the item 
    def get_Item_Desc(self): #define the get item's name method
        return self.Item_Desc
    def get_unit_Inv(self): #define the get the item's inventory method'
        return self.unit_Inv 
    def get_Price(self): #define the get price
        return self.Price

def main():

    Item_Desc1=RetailItem('Jacket', '12', '$59.95') #set the values for the jackets
    Item_Desc2=RetailItem('Designer \t|\t\t\t\t|\nJeans', '40', '$34.95') #set the values for the jeans
    Item_Desc3=RetailItem('Shirt', '20', '$24.95')#set the values for the shirts

    print('\t\t\t\tUnits in')
    print('Description |   Inventory \t|\t\tPrice')
    print('____________|_______________|________________')
    print(Item_Desc1, Item_Desc1.get_unit_Inv(), Item_Desc1.get_Price(), sep='\t\t|\t\t') #print the information for the jackets
    print('____________|_______________|________________')
    print(Item_Desc2, Item_Desc2.get_unit_Inv(), Item_Desc2.get_Price(), sep='\t\t|\t\t') #print the information for the jean
    print('____________|_______________|________________')
    print(Item_Desc3, Item_Desc3.get_unit_Inv(), Item_Desc3.get_Price(), sep='\t\t|\t\t') # print the information for the shirts
    print('_____________________________________________')
main()
