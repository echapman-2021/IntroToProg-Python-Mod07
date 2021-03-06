## Elisabeth Chapman
## 3/2/2021
## Foundations of Programming Python
## [](url)https://github.com/echapman-2021/IntroToProg-Python-Mod07
## Assignment 07
# Saving data to a Pickled file
In this project, the process of writing data to a file was further explored and a new mechanism for writing and storing data was deployed. This method—called file pickling—was explored as a mechanism for storing information. Just as in the previous project, we again saved user inputted data into a separate file—only this time it was with the addition of a few key differences such as reduced file size which altogether gave the program a greater ability to serialize data. Another concept explored within this project was the concept of error handling—the idea that is better to build a program with built in fail points rather than one with no ability to fail. Because the user-failures are anticipated by the programmer, they can be more easily remedied even by an inexperienced user.
# Pickling
 ![image](https://user-images.githubusercontent.com/78879611/110529454-24907f80-80ce-11eb-9c49-44758b8e626e.png)
## Figure 1: The pickled binary file 
As seen above, the file is ‘pickled’— meaning that rather than saving the file to a human readable format, we save the file in a way that “is Python-specific, and […] can be read only by another Python program”( Mastromatteo). Although this data scrambling and unscrambling provides a slight sense  of security in that obscures the data from human eyes, it unfortunately cannot be relied on because it does not encrypt the file within—thus it should not be relied on in this manner. Where the use of binary files does excel is as a way “way to serialize and deserialize objects in Python”(Mastromatteo). Because “pickle stores the object once and ensures that all other references point to the master copy”(Pathak), it is ideal for information sharing because it renders the sets stored within more easily sharable. Moreover, it can be said that  “If you don’t need a human-readable format […] or if you need to serialize custom objects, then go with pickle.” ”(Mastromatteo).

# Try/Except
 ![image](https://user-images.githubusercontent.com/78879611/110529569-45f16b80-80ce-11eb-9c5f-7432fa1bcd7f.png)
###  Figure 2: Try/Except statement within the code
Moreover, this project was also the first foray into the concept of error handling. As seen above, one of the simplest ways of handling errors is with a “try and except block in Python [..] used to catch and handle exceptions”(van de Klundert). Because the try statement is an attempt to run the entire code, it executes first and if no errors are found the code will run as usual. If the specified error in the except clause is present, the except clause will then initialize with the programmed response. These two blocks are helpful for users because they can be used to signify where the program is miscalculating and lead the user to a pre-written hint on how to fix the bug. In this script,  a simple try statement requests only that the user enters a number of some type, and if the user enters something else, they will receive a statement clarifying that the program needed a number to successfully execute the rest of the script. 
# A note on Websites: 
In this project it was suggested that we research online for websites to better clarify on the concepts of error handling and file pickling. The websites primarily used in this assignment were geeksforgeeks.com which proved to be a decent resource for a brief easily understood summaries,  and realpython.com for a much more in-depth explanation on both file pickling and error handling. Medium.com, with some tentative caution can also be a decent resource written by developers within the field, however the qualifications to write for medium.com(or stackoverflow.com) are non-existent.
# Conclusion
![image](https://user-images.githubusercontent.com/78879611/110529662-61f50d00-80ce-11eb-9ea5-4c01884e0b65.png)
### Figure 3: The script running in PyCharm
In conclusion, this data-saving script differed from the previous, insomuch as that although the data is saved and retrieved with no visible changes on the user end, the file on the computer has been both scrambled and unscrambled behind the scenes in the form of a binary file—rather than .txt file. However, it must be said that although the file is scrambled, it is not completely secure. The main value of pickling data is in the serialization of the data, whereas a .txt file can store simple data such as strings but cannot handle lists and dictionaries—a binary file can store a wider variety of data types. 


 ![image](https://user-images.githubusercontent.com/78879611/110529768-7fc27200-80ce-11eb-997f-f53b93fa2ea3.png)
### Figure 4: The script running in Command Prompt


## References
-	Dawson, Michael, Python Programming, Third Edition, Course Technology, a part of Congage Learning, 2010
-	Omkar Pathak. Understanding Python Pickling with example, geeksforgeeks.com, 13 Nov 2018 https://www.geeksforgeeks.org/understanding-python-pickling-example/. Accessed Feb 26, 2021
- Davide Mastromatteo. The Python pickle Module: How to Persist Objects in Python, realpython.com, Apr 27, 2020,  https://realpython.com/python-pickle-module/. Accessed Feb 26, 2021
-	Said van de Klundert. Python Exceptions: An Introduction , realpython.com, No date found, https://realpython.com/python-exceptions/. Accessed Mar 1, 2021



