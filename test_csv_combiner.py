import unittest
# import main function from csv_combiner.py
from csv_combiner import main

#create a class called Combiner_Tests
class Combiner_Tests(unittest.TestCase): 
    def setUp(self):
        print("Initializing")
        self.argv_list = ['./testfile/clothing.csv','./testfile/accessories.csv']

    def tearDown(self):
        print("Resetting Enviroment")
        self.argv_list=[]

    def test_main(self):
        print('Combining multiple csv to one')
        self.assertEqual(main(self.argv_list), "success","wrong")

if __name__ == "__main__":
    unittest.main()
