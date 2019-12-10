# CeasarCipher
Program which encrypts and decrypts messages using the Ceasar Cipher. This project was something I used to teach myself the fundamentals of object oriented programming and tkinter.

10/15/2019: Updated the GUI. I think this is what I actually want it to look like.

10/20/2019:  
Minor changes to gui layout.  
Added log frame and widget to show transcription of users message.  
Added label to scale, shows the value of the key according to scale position.  
Created get_message() and get_scale functions().  
get_message() shows value of users message to the shell.  
get_scale() shows value of scale to the shell.  
Created a bind for return key for get_message() function. 

10/25/2019:
Refactored GUI code to use object oriented model. No other significant changes.

11/20/2019:
Refactored code.
Created function which retreviews values from get_message(), get_selected(), and get_scale(), then uses the ceasar cipher method to translate message. Project is finished besides needing a database.

12/09/2019:
Added brute force method, nothing connected to gui yet.  
Discovered that GUI looks weird as heck in Windows.  

TODO:

~~Map ceasarcipher.py functions to gui.~~  
~~Create class structure for GUI.~~   
Create database of previous queries.    
~~Add brute force message~~
Create another tab within the program for brute force method.
Refactor code to look better on Windows.  
