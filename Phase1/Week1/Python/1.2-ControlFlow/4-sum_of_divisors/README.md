WTF - Write Totatives Finder
=================

##### DESCRIPTION
---
The divisors of a number are those numbers that divide it evenly; for example, the divisors of 60 are `1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60`. The sum of the divisors of 60 is 168, and the number of divisors of 60 is 12.

The totatives of a number are those numbers less than the given number and coprime to it. Two numbers are coprime if they have no common factors other than 1. 

For example, the totatives of 30 are `1, 7, 11, 13, 17, 19, 23, and 29`.

The number of totatives of a given number is called its totient. As you can see above, the totient of 30 is 8. 

Your task is to write a small library of five functions that compute the divisors of a number, the sum and number of its divisors, the totatives of a number, and its totient.

##### PUBLIC INTERFACE
---
```
divisors(<num>)
    @params num - integer

sum_of_divisors(<num>)
    @params num - integer

num_of_divisors(<num>)
    @params num - integer

totatives(<num>)
    @params num - integer

totient(<num>)
    @params num - integer
```

##### TEST CASES
---
```python
>>> divisors(30)
[1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30]

>>> sum_of_divisors(30)
108

>>> num_of_divisors(30)
11

>>> totatives(30)
[1, 7, 11, 13, 17, 19, 23, 29]

>>> totient(30)
8
```

##### RESOURCES
---
_Hint_: The functions can call each other!

[High Order Functions(Did Not Read)]:http://effbot.org/pyfaq/how-do-you-make-a-higher-order-function-in-python.htm
