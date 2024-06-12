import unittest  # Library that automates unit tests
from data_classes import Person
from data_classes import Employee

class TestPerson(unittest.TestCase):        # anything in the person class is in a unit test
    def test_person_innit(self):        # test initialization on person class
        person=Person('David', 'Goldberg')
        self.assertEqual('David', person.first_name)      # automation that is from test case, check if first name is correct
        self.assertEqual('Goldberg', person.last_name)

    def test_person_invalid_name(self):
        with self.assertRaises(ValueError):     # expecting to see a failure here
            person=Person('123', 'Goldberg')
        with self.assertRaises(ValueError):     # expecting to see a failure here
            person=Person('David', '123') 

    def test_person_str(self):      # test __str__ function in person class 
        person=Person('David', 'Goldberg')
        self.assertEqual('David,Goldberg', str(person))

class TestEmployee(unittest.TestCase):
    def test_employee_innit(self):
        employee=Employee('David', 'Goldberg', '2024-02-26', 4)
        self.assertEqual('David', employee.first_name)      # automation that is from test case, check if first name is correct
        self.assertEqual('Goldberg', employee.last_name)
        self.assertEqual('2024-02-26', employee.review_date)
        self.assertEqual(4, employee.review_rating)

    def test_employee_invalid_review_data(self):
        with self.assertRaises(ValueError):
            employee=Employee(first_name='David', last_name='Goldberg', review_date='2001/04/26', review_rating= 4)
    
    def test_employee_rating_out_of_range(self):
        with self.assertRaises(ValueError):
            employee=Employee(first_name='David', last_name='Goldberg', review_date='2024-02-26', review_rating= 6)




if __name__ == '__main__':
    unittest.main()     # when running the test, run all tests in the file