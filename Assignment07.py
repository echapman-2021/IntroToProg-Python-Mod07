# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
#EChapman, 2.25.2021, opened and created script
#EChapman, 2.26.2021 completed script
# ------------------------------------------------- #
import pickle
# Data -------------------------------------------- #
file_name ="C:\_PythonClass\Assignment07\AppData.dat"    #'AppData.dat'
lstCustomer = []
list_of_data = []
# Processing -------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        """Writes data to a binary file"""
        file = open(file_name, "wb")
        b = pickle.dump(list_of_data,file)
        file.close()

    @staticmethod
    def read_data_from_file(file_name):
        """Reads data from the binary file"""
        f  = open(file_name, "rb")
        freshly_pickled = pickle.load(f)
        print(freshly_pickled)
        f.close()

    @staticmethod
    def add_to_list(lstCustomer):
        """Adds data to list of Customer data"""
        list_of_data.append(lstCustomer)
        return list_of_data
#IO---------------------------------------
class IO:
    """ Performs Input and Output tasks """
    @staticmethod
    def input_grab_id():
        try:
            float_id = float(input("Enter your ID number: "))
        except:
            print("That's not an ID number! ...Try again!")
        user_id = str(float_id)
        lstCustomer.append(user_id + ",")
        return user_id, lstCustomer
    @staticmethod
    def input_grab_name():
        try:
            user_name = input("Enter your name: ").strip()
        except:
            print("ERROR! Something went wrong, restart and try again")
        lstCustomer.append(user_name)
        return user_name, lstCustomer
# Presentation ------------------------------------ #

print("-----Welcome----")
"""Getting  ID and name from user"""
IO.input_grab_id()
IO.input_grab_name()

"""Storing it in a list object"""
print("Data has been added to a list!")
Processor.add_to_list(lstCustomer)


"""Storing the list object into a binary file"""
print("Storing data...")
Processor.save_data_to_file(file_name, lstCustomer)
"""Reading the data from the file"""
print("reading data...")
print("The data read from file is...")
Processor.read_data_from_file(file_name)
input("Press ENTER to exit")