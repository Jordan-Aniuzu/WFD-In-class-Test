import unittest #PARTB OOP JORDAN ANIUZU (B00151878) TESTNG


from partA import House, Mansion

class TestHouse(unittest.TestCase): #IMPLYING A TESTCASE TO BE DONE



  #B1 IS ALREATD DONE BY CREATING THE FILE 
    def setUp(self):



        self.house = House(12, "Corduff Grove", "Dublin", 3, 250000)
        self.luxury_house = Mansion(25, "Portmarnock Green", "Dublin", 5, 1000000, True, True)
        self.same_house = self.house  # REFERERING TO THE SAME OBJECT AS HOUSE

    def test_instance_of_class(self): #B2 THIS TEST IF THE OBJCT IS AN INSTANCE OF A CLASS
       
        self.assertIsInstance(self.house, House)
        self.assertIsInstance(self.luxury_house, Mansion)
        self.assertIsInstance(self.luxury_house, House)  

    def test_not_instance_of_class(self):
    #B3 TEST IF OBJECT IS NOT AN INSTANCE OF A CLASS
        self.assertNotIsInstance(self.house, Mansion)

    def test_objects_are_identical(self):
        """B4: TEST IF 2 OBJECTS ARE IDENTICAL""" #TESTING IF TWO OBJECTS ARE IDENTICAL
        self.assertIs(self.house, self.same_house) 

    def test_update_methods(self):
        """B5: TEST UPDATE METHODS FOR HOUSE""" #TESTING IF THE UPDATE METHODS WORK
        self.house.update_price(300000)
        self.assertEqual(self.house.price, 300000)

        self.house.update_street("Corduff Grove")
        self.assertEqual(self.house.street, "Corduff Grove")



        self.house.update_num_beds(4)
        self.assertEqual(self.house.num_beds, 4) #TESTING IF THE NUMBER OF BEDS IS UPDATED

        self.luxury_house.update_pool(False)
        self.assertFalse(self.luxury_house.pool) #TESTING IF THE POOL IS UPDATED

        self.luxury_house.update_garage(False)
        self.assertFalse(self.luxury_house.garage) #TESTING IF THE GARAGE IS UPDATED

    def test_invalid_updates(self):
        """TEST INVALID UPDATES (SHOULD NOT CHANGE VALUES)"""
        self.house.update_price("Not a number")  #THIS IS AN INVALID UPDATE
        self.assertEqual(self.house.price, 300000)  #REMAINS UNCHANGED

        self.house.update_num_beds("Four")  #THIS IS AN INVALID UPDATE
        self.assertEqual(self.house.num_beds, 4)  #REMIANS UNCHANGED

        self.luxury_house.update_pool("yes")  #THIS IS AN INVALID UPDATE
        self.assertFalse(self.luxury_house.pool)  #REMAIN UNCHANGED




    @staticmethod
    def run_tests(): #CALLING THE RUNTESTS FUCNTION
        """B6: RUN ALL TESTS""" #B6 RUNNING ALL TESTS
        unittest.main()




if __name__ == "__main__":
    TestHouse.run_tests()

