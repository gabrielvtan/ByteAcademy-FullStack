Age Calculator
===============
##### DESCRIPTION
---
Create a program that will take user input and tell them their age in months, days, hours, and minutes.

###### Part 1
Your first function, ```age_to_time```, should take the persons age in years and return it in months, days, hours, and minutes.

##### PUBLIC INTERFACE
```
age_to_time(<age>)
    @param age - integer representing the age in years
```
##### TEST CASES
---
```
How old are you? 18
months : 216, days : 6480, hours : 155520, and minutes : 388800
```

###### Part 2
Add a function to your program that takes the user's birthday as input in `YYYY-MM-DD` format and tells them their age in months, days, hours and minutes in the same fashion.

##### PUBLIC INTERFACE
```
birthday_to_time(<birthday>)
    @param date_of_birth - string representation of the date
```
##### TEST CASES
---
```
When were you born? 05-06-1985
EDIT
months : 216, days : 6480, hours : 155520, and minutes : 388800
```
##### RESOURCES
---
_Hint: Take a look at Python's [`datetime`][datetime] library._

[datetime]:https://docs.python.org/3.5/library/datetime.html