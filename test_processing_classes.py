import unittest, tempfile, json
from processing_classes import FileProcessor
from data_classes import Employee



# this works with json, don't want python to mess with main json file in the test
# when testing the file, use a different file
class TestFileProcessor(unittest.TestCase):
    '''
    setUp: called before every test is run. Create new file to run for the tests 
    teardown: run after the test is done. Closes the temp file
    '''
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)      # creating a temp file, going to read and write from this file
        self.temp_file_name = self.temp_file.name       # getting name of the file

    def tearDown(self):
        self.temp_file.close()

    def test_read_data_from_file(self):     # creating sample data in the temp fiile
        sample_data= [
            {"FirstName": "David", "LastName": "Goldberg", "ReviewDate": "2024-04-26", "ReviewRating": 4},
            {"FirstName": "John", "LastName": "Peter", "ReviewDate": "2024-04-26", "ReviewRating": 3}
            ]
        
        with open(self.temp_file_name, 'w') as file:  # open temporary file      
            json.dump(sample_data, file)

        employees = FileProcessor.read_employee_data_from_file(self.temp_file_name)     # read in temp file
        self.assertEqual(len(sample_data), len(employees))      # validation: length of sample data is equal to length of data
        
        self.assertEqual(sample_data[0]['FirstName'], employees[0].first_name)
        self.assertEqual(sample_data[0]['LastName'], employees[0].last_name)
        self.assertEqual(sample_data[0]['ReviewDate'], employees[0].review_date)
        self.assertEqual(sample_data[0]['ReviewRating'], employees[0].review_rating)

        self.assertEqual(sample_data[1]['FirstName'], employees[1].first_name)
        self.assertEqual(sample_data[1]['LastName'], employees[1].last_name)
        self.assertEqual(sample_data[1]['ReviewDate'], employees[1].review_date)
        self.assertEqual(sample_data[1]['ReviewRating'], employees[1].review_rating)

    def test_write_data_to_file(self):      # testing writing to file 
        sample_data= [
            Employee('David','Goldberg','2024-04-26',4),
            Employee('John','Peter','2024-04-26',3)
        ]

        FileProcessor.write_employee_data_to_file(self.temp_file_name, sample_data)     # calling write to file method using sample data and sample file

        with open(self.temp_file_name, 'r') as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))      # validation: length of sample is equal to the length of actual inputted data

        self.assertEqual(sample_data[0].first_name, file_data[0]['FirstName'])
        self.assertEqual(sample_data[0].last_name, file_data[0]['LastName'])
        self.assertEqual(sample_data[0].review_date, file_data[0]['ReviewDate'])
        self.assertEqual(sample_data[0].review_rating, file_data[0]['ReviewRating'])

        self.assertEqual(sample_data[1].first_name, file_data[1]['FirstName'])
        self.assertEqual(sample_data[1].last_name, file_data[1]['LastName'])
        self.assertEqual(sample_data[1].review_date, file_data[1]['ReviewDate'])
        self.assertEqual(sample_data[1].review_rating, file_data[1]['ReviewRating'])

if __name__ == '__main__':
    unittest.main()     # when running the test, run all tests in the file