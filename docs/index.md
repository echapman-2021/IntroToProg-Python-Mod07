Elisabeth Chapman
2/28/2021
Foundations of Programming Python
GitHub [https://github.com/echapman-2021/IntroToProg-Python-Mod07](url)
Assignment 07
###Saving data to a Pickled file
In this project, the process of writing data to a file was further explored and a new mechanism for writing and storing data was deployed. This method—called file pickling—was explored as a mechanism for storing information. Just as in the previous project, we again saved user inputted data into a separate file—only this time it was with the addition of a few key differences such as reduced file size which altogether gave the program a greater ability to serialize data. Another concept explored within this project was the concept of error handling—the idea that is better to build a program with built in fail points rather than one with no ability to fail. Because the user-failures are anticipated by the programmer, they can be more easily remedied even by an inexperienced user.
Pickling
 Figure 1: Pickled file
As seen above, the file is ‘pickled’— meaning that rather than saving the file to a human readable format, we save the file in a way that “is Python-specific, and […] can be read only by another Python program”( Mastromatteo). Although this data scrambling and unscrambling provides a slight sense  of security in that obscures the data from human eyes, it unfortunately cannot be relied on because it does not encrypt the file within—thus it should not be relied on in this manner. Where the use of binary files does excel is as a way “way to serialize and deserialize objects in Python”(Mastromatteo). Because “pickle stores the object once and ensures that all other references point to the master copy”(Pathak), it is ideal for information sharing because it renders the sets stored within more easily sharable. Moreover, it can be said that  “If you don’t need a human-readable format […] or if you need to serialize custom objects, then go with pickle.” ”(Mastromatteo)
##Try/Except
 
Moreover, this project was the first foray into the concept of error Handling. As seen above, one of the simplest ways of handling errors is with a simple Try Statement with an Except Clause. The try statement executes first with the attempted task, but if that task fails for whatever reason, the except clause will kick in with the programmed response. This is helpful for users because it signifies where the program went wrong and gives them a pre-written hint on how to fix the bug. In this case, the very simple try statement requests only that the user enters a number of some type, and if the user enters something else, they will receive a statement clarifying that the program needed a number to successfully execute the rest of the script. 


##Conclusion
In conclusion, this data-saving script differed from the previous, insomuch as that although the data is saved and retrieved with no visible changes on the user end, the file on the computer has been both scrambled and unscrambled behind the scenes in the form of a binary file—rather than .txt file. However, it must be said that although the file is scrambled, it is not completely secure. The main value of pickling data is in the serialization of the data, whereas a .txt file can store simple data such as strings but can’t handle lists and dictionaries—a binary file can store a wider variety of data types. 

  In PyCharm
  in Command prompt
References
*	Dawson, Michael, Python Programming, Third Edition, Course Technology, a part of Congage Learning, 2010
* Omkar Pathak. Understanding Python Pickling with example, geeksforgeeks.com, 13 Nov 2018 [https://www.geeksforgeeks.org/understanding-python-pickling-example/.](url) Accessed Feb 26 2021
*	Davide Mastromatteo. The Python pickle Module: How to Persist Objects in Python, realpython.com, Apr 27, 2020,  [https://realpython.com/python-pickle-module/.](url) Accessed Feb 26 2021
