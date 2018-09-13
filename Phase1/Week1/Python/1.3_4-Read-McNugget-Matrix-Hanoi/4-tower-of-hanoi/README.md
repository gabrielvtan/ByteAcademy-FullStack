# The Tower of Hanoi
---

#####  Description

* [The Tower of Hanoi](http://en.wikipedia.org/wiki/Tower_of_Hanoi) is a mathematical game or puzzle. 
* It consists of three rods, and a number of disks of different sizes which can slide onto any rod. 

![Balh](https://upload.wikimedia.org/wikipedia/commons/0/07/Tower_of_Hanoi.jpeg)


* The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top
* The objective of the puzzle is to move all the disk from the first rod to the last rod following a few rules

##### Rules

* Only one disk can be moved at a time.
* You can only grab the top disk from one of the stacks to place it on another stack
* No larger disk can be placed on top of a smaller disk

##### Challenge

* Write a function that solves the Tower of Hanoi no matter how many disks are passed in.
* It should take in four parameters, as shown in the example below. 
```
def tower_move(disks, start, finish, middle)
```

* Your function should perform the moves necessary to rearrange the tower, and it should return the total number of steps required to solve the puzzle.
* With three disk, the puzzle can be solved in seven moves. 
* Hint: this exercise will involve `recursion`
    * (Think about invoking a function in itself)
