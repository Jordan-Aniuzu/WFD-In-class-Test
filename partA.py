class House: #JORDAN ANIUZU OOP PART A (B00151878) (#REMINDER, PART A1 AND B1 DONE ALREADY) CLASS MAKING AND UODATES ETC


    def __init__(self, house_number, street, area, num_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.num_beds = num_beds   #INSTANTIATING/CALLING ALL ATTRIBUTES FROM THE TOP
        self.price = price     

    def display_info(self): #A3: METHOD TO DISPLAY ALL ATTRIBUTES. CALLS AL VALUES AKA SELF + THE NAME OF ATTRIBUTE
        print(f"House Number: {self.house_number}, Street: {self.street}, Area: {self.area}, Beds: {self.num_beds}, Price: {self.price}")




#A4 METHODS TO UPDATE ALL ATTRIBUTES
    def update_house_number(self, new_number): #METHOD TO UOPDATE THE HOUSE NUMBER
        if isinstance(new_number, int):   #IF THE NUMBER IS AN INT + NEW NUMBE RTHEN THE HOUSE NUMBER WILL BE UPDATED
            self.house_number = new_number
        else:
            print("Invalid house number!") #IF NOT, THE HOUSE NUMBER IS INVALID


    def update_street(self, new_street):   #UODATE STREET METHOD
        if isinstance(new_street, str):
            self.street = new_street  # CHECKS IF ITS A STRING: IF IT IS THEN THE STREET WILL BE UPDATED
        else:
            print("Invalid street name!")

    def update_area(self, new_area): #UPDATE AREA METHOD
        if isinstance(new_area, str): #CHECKS IF ITS A STRING: IF IT IS THEN THE AREA WILL BE UPDATED
            self.area = new_area
        else:
            print("Invalid area name!")

    def update_num_beds(self, new_beds): #UPDATE NUMBER OF BEDS METHOD
        if isinstance(new_beds, int): #CHECKS IF ITS AN INT: IF IT IS THEN THE NUMBER OF BEDS WILL BE UPDATED
            self.num_beds = new_beds
        else:
            print("Invalid number of beds!")

    def update_price(self, new_price): #UPDATE PRICE METHOD
        if isinstance(new_price, (int, float)):
            self.price = new_price #CHECKS IF ITS AN INT OR FLOAT: IF IT IS THEN THE PRICE WILL BE UPDATED
        else:
            print("Invalid price!")




#A5  1 CHILD CLASS
class Mansion(House):
    def __init__(self, house_number, street, area, num_beds, price, pool, garage):
        super().__init__(house_number, street, area, num_beds, price)
        self.pool = pool  #BOOLEAN VALUE  FOR POOL BEING TRUE OR FALSE 
        self.garage = garage  #INSTANTIATING ALL ATTRIBUTES

        ##(GARAGE AND POOL ARE USED TO EXTEND FUNCTIONALITY AS PART OF THE HOSUE METHOD)


#A6
    def display_info(self): 
        super().display_info() #DISPLAYS ALL ATTRIBUTES FROM THE PARENT CLASS
        print(f"Pool: {self.pool}, Garage: {self.garage}")

#A7
    def update_pool(self, has_pool):
        if isinstance(has_pool, bool):
            self.pool = has_pool
        else:
            print("Invalid value for pool!")


    def update_garage(self, has_garage):
        if isinstance(has_garage, bool):
            self.garage = has_garage
        else:
            print("Invalid value for garage!")


#A8
# CREATING INSTANCES OF CLASSES ASKED IN A8
house1 = House(12, "Corduff Grove", "Dubln", 3, 250000)
luxury_house1 = Mansion(25, "Portmarnock Green", "Dublin", 5, 1000000, True, True)

#THE METHOD BELOW RUNS THE DISPLAY INFO METHOD TO DISPLAY ALL ATTRIBUTES AS WELL AS CALLING FROM LUXURURY INFO TOO
house1.display_info()
luxury_house1.display_info()

#THE METHODS BELOW ARE USED TO UPDATE THE ATTRIBUTES OF THE UPDATED HOUSE PRICE AND STREET NAME
house1.update_price(270000)
house1.update_street("Dunboyne Road")

#THE METHODS BELOW ARE USED TO UPDATE THE ATTRIBUTES OF THE LUXURY HOUSE POOL AND GARAGE BOOLEAN VALUES
luxury_house1.update_pool(False)
luxury_house1.update_garage(False)

#FINALLY THE DISPLAY INFO METHOD IS CALLED TO DISPLAY ALL UPDATEDD ATTRIBUTES OF ALL CLASSES GIVEN BELOW



#A9
house1.display_info()
luxury_house1.display_info()

