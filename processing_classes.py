from data_classes import Employee
import json
from typing import TextIO
from presentation_classes import IO

employees: list = []  # a table of employee data
menu_choice = ''

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    """

    @staticmethod
    def read_employee_data_from_file(file_name: str):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: an reference to the Employee class
        :return: list
        """
        employee_data = list()
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = Employee()
                    employee_object.first_name=employee["FirstName"]        # set firstname as a key in dict
                    employee_object.last_name=employee["LastName"]      # set lastname as a key in dict
                    employee_object.review_date=employee["ReviewDate"]      # set ReviewDate as a key in dict
                    employee_object.review_rating=employee["ReviewRating"]      # set ReviewRating as a key in dict
                    employee_data.append(employee_object)
        except FileNotFoundError:
            raise FileNotFoundError("Text file must exist before running this script!")
        except Exception:
            raise Exception("There was a non-specific error!")
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)        # write dictionary to file
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")




if __name__ == '__main__':
        print('This file is not meant to be run, please run main.py')