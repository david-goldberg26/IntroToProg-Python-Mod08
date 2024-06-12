import unittest
from unittest.mock import patch
from presentation_classes import IO
class TestIO(unittest.TestCase):
    
    def test_get_input(self):       # want input choice to be automated (patch the function)
        # patch function will overwrite python. override builtins.input
        # return the value 2
        with patch('builtins.input', return_value='2'):
            choice=IO.input_menu_choice()
            self.assertEqual('2', choice)

    def test_input_employee_data(self):
        # Simulate user input for student data
        with patch('builtins.input', side_effect=['David', 'Goldberg', '2024-04-26', 4]):       # simulate user input for employee data
            employees = []
            employees=IO.input_employee_data(employees)     # call input_employee_data function to populate list
            self.assertEqual(1, len(employees))     # check if a record has been inputted into the list
            self.assertEqual( 'David', employees[0].first_name)     # verify the first name
            self.assertEqual('Goldberg', employees[0].last_name )       # verify the last name
            self.assertEqual('2024-04-26', employees[0].review_date)        # verify the review date
            self.assertEqual(4, employees[0].review_rating)     # verify the review rating
        
    
    

if __name__ == '__main__':
    unittest.main()     # when running the test, run all tests in the file