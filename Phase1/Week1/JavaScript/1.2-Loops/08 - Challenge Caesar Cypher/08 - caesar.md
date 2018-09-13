## Day 2 - Challenge Exercise - Caesar

* Julius Caesar used a simple code to send messages to his subordinates. He would shift each letter in a message a certain number of letters forward in the alphabet. For instance if that number was 2, then "VINCE" (the command form of to conquer in latin) would be "XKPEG." If a letter would go past the end of the alphabet, it loops back around, so Y would be come A with a shift of 2.

* Write a program that asks the user for a message and an integer shift value.

* Print out the encoded message. Keep characters other than letters the same.

* You will need to look up documentation for how to convert a character to a meaningful number and back again.

* Python3's strings are in the *character set* of Unicode. You may need to convert them to UTF-8.

* Allow negative integer input to decrypt.

#### Historical accuracy

* Lower case letters were not invented until after the fall of the Roman Empire. They were developed by Frankish (Germanic) monks and scribes. To make this problem more accurate, print out the encoded message in all caps.

#### Internet history

* Did you know that forum discussions are older than the World Wide Web? An older internet technology, Usenet goes back to the 1980s and worked much like modern forums did. In old discussions of movies and books, spoilers were encoded in what was called ROT13, which was a Caesar Cypher with a shift of 13.

* What is special about a shift of 13?

* Look up "Eternal September" for a bit of Usenet history.