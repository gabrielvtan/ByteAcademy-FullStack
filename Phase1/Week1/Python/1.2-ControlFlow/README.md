## Welcome to Byte Academy!!

Congratulations on taking the very first step towards a career as a technologist. No matter what your career goals and aspirations, you will need fundamental understanding of programming, design and data as a craft.

#### Schedule

Most days will have some periodic lecture or talks, usually not exceeding an hour. The majority of your time should be spent programming. The instructors and coaches are here for any questions you might have during immersion hours, and [reachable on Slack](http://byteacademy.slack.com) in the evenings.

Stay focused and stay on task. If you are venturing far off the course of the assignment at hand, you are no longer on task. Work hard, but make sure you sleep and take care for yourself.

You are welcome and encouraged to stay here and continue to work together after 6pm, and on weekends.

We will be having meetups and workshops on some Tuesdays and Thursdays for outside guests - you are also welcome and encouraged to join us for those and enjoy some free pizza.

####Resources

These resources are here when needed - but Google is your friend!
# Python Fundamentals
The fundamentals of programming translate throughout every language. Like learning any new language we're going to start with the basics and build up. If you wanted to learn English you wouldn't start by reading a novel, but with the alphabet

### Variables

* Variables are a way to store and save data for use
* This is called `assignment`. You are assigning a value to a variable
* Declaring Variables
    * Cannot start with a number
    * Cannot declare with special characters
    * Written in snake case
* Open up Python in the terminal

```python
name = "Jason"
fav_num = 8
turtles = ["Raph", "Leo", "Mickey", "Donny"]
```

### Data Types

* Now you may have noticed that variables can hold different `types` of values
* These are called `Data Types` and python3 has [many built-in types](https://docs.python.org/3/library/stdtypes.htm)
    * [Strings](https://docs.python.org/3/library/stdtypes.html#str)
        * Sequence of 0 or more characters(a-z, A-Z, 0-9, !,@,#, ect).
        * python type `str()` or with the literal `''` or `""`
        * [methods to know](https://docs.python.org/3/library/stdtypes.html#string-methods)
            * `.format()` [https://pyformat.info/](More info)
            * `.isdigit()`, `islower()`, `isupper()`, check to see if the string is a digit and so on. There are many more like these
            * `.lower()`, `.upper()` changed the string to lower and up case
            * `.split()` changes the string to a list based around the character[s] given
    * [Numbers](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
        * [Floats](https://docs.python.org/3/library/functions.html#float)
            * decimals
            * python type `float()` or with the literal `23.3`
            * methods to know
                * `is_integer()` Return `True` if the float a whole number, and `False` otherwise
        * [Integers](https://docs.python.org/3/library/functions.html#int)
            * whole number
            * python type `int()` or with the literal '4'
    * [Lists](https://docs.python.org/3/library/stdtypes.html#lists)
        * Ordered sequence of items
        * python type `list()` or the literal `['a', 'b', 'c']`
        * methods to know
            * `.append()` adds a item to a list
            * `.pop()` removes and returns the last item from the list
    * [Dictionary](https://docs.python.org/3/library/stdtypes.html#dict)
        * Collections of key, value pairs
        * python type `dict()` or the literal `{'key':'value'}`
        * methods to know
            * `.get()` return the value of a give key, or a default value if its not found
            * `.values()` returns a `list` of values in the Dictionary
            * `.keys()` returns a `list` of keys in the Dictionary 
    * [Booleans](https://docs.python.org/3/library/stdtypes.html#boolean-values)
        * Represents something that is `True` or `False` 
        * python type `bool()` or the literal `True` or `False`
    * [Range](https://docs.python.org/3/library/stdtypes.html#range)
        * `Range()` is a special type that represents range of numbers
    * [None](https://docs.python.org/3/library/stdtypes.html#the-null-object)
        * nothing, nothing at all
        * python type ... there is one way, the literal way `None`

### Notable built in functions
* `len()` return the length of the given *sequence*
* `help()` shows help documentation of the given object
* `dir()` show the available methods of the give object

#### Math Operators
All math operators can be done on both floats and ints
Python comes with the following symbols for mathematical operators.

* `+` add
* `-` subtract
* `*` multiplication
* `\` division
* `\\` floor divided, always returns a whole number
* `%` modulo: finds the remainder after division
* The language also supports PEMDAS
    * `5+(50+5)`

#### Comparison Operators

* `==` equality
* `!=` not equal
* `<` less then
* `<=` less then or equal to
* `>` greater then
* `>=` greater then or equal to


#### Control Flow

* Now we have reached `if/else` statements
* If an expression you passed in is `True` do something
* `else` do something `else`

```python
if expression == true:
    run code
    
if name == "Jason":
    print("That is an awesome name")
else: 
    print("You should get a different name")
    
if number > 100:
    print("That's a big number")
elif number > 50 && number < 100:
    print("That's a medium number")
else:
    print("Your number is puny")
```
* Things to note
    * Put a colon after the expression you want to evaluate to start the `if` body
    * `if` to `elif` to `else`
    * indents show what code is part of the body of the statement and where it ends


#### Lists and Indexing

* What if you wanted to store more data. 
* Can be assigned to variables
* Can hold different data types at once
* The values are indexed for us starting at zero

```python
my_list = ["Jason", "Anna Kendrick", 2015, True]

my_list[0] == "Jason" # True

my_list[2] == 2016 # False
```
* Just a heads up indexing through a list is similar to indexing with strings. 
* the value at index zero will be the first element in the list, or the first letter in a string

#### Functions and Statements

* We declare our functions with the word `def` for define
* Functions follow the same naming principles as declaring variables
    * Snake case
    * Do not start with numbers or special characters
* Remember how we used white space to organize our code with if/else statements. Well that idea holds true everywhere in Python

```python
def my_name():
    return "My name is Jason"
```
* Functions allow us to build code that is reusable
* This follows the concept of **DRY - Don't Repeat Yourself**
* Functions can also take arguments. These allow our functions to be more dynamic

```python
def my_name(name):
    return "My name is " + name
```

* When there is no `return` statement, the function *implicitly* returns `None`

### `for` loops

`for` loops *iterate* over a *sequence*. There are 2 parts to a `for` loop, the *statement* and the *body*. The *statement* tells the loop what to *iterate* over and *assigns* the loop variable. The body tells python what to do in each iteration. Before each iteration the loop variable is assigned to the next value in the *sequence*, in oder from the zero index to the last item.

```python
teachers = ['billy', 'tom', 'jason', 'jeff']
for teacher in teachers:
    print( teacher.capitalize() )
```

In this loop we *iterate* over each teacher in the loop and print there name capitalized.

### `while` loops

Unlike `for` loops, `while` are not bound to a sequence and can continue for ever.
like a `for` loop, `while` loops have 2 parts, an *statement* and a body.

```python
num = input('Please enter a whole number: ')
while not num.isdigit():
    print('Not a whole number!')
    num = input('Please enter a whole number: ')
```


### loop control
There are 2 ways can control what loops. They both with `for` and `while` loops in the same way.

* [`break`](https://docs.python.org/3/reference/simple_stmts.html#break)
    The `break` *statement* stops loop and allows python to move on to the rest of the script. If you are using a `while` loop, you should have a break *statement* to stop the loop.
```python
count = 1
while True:
    count *= count
    if count > 100: break
```
* [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue)
    The `continue` *statement* skips to the next iteration of the loop. Generally, `continue` statement are at the top of the loop body.
```python
for num in range(100):
    if num%10 != 0: continue
    print(num)
```


[Python Cheatsheet](http://overapi.com/python/)

[Python Convention](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html)
