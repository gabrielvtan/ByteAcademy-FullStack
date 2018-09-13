# REPL Expressions

## Calculator

* There is nothing to turn in for this exercise.

* Start the python REPL by typing ``` python ``` into VSCode's terminal. ``(Remember Ctrl+` or Command+`)`` opens & closes the terminal.

* REPL stands for Read-Evaluate-Print-Loop and that's what the python interpreter in interactive mode does. It reads python commands you type in, evaluates (interprets) them, prints the result, and then starts over again.

* Try using the interpreter as a calculator

* Add with +, multiply with ``*``, divide with /, and subtract with -

* Try storing the results of your calculations to variables and then printing them back out.

* Do a calculation and then print the special variable _ (the underscore). What do you think _ does? (This only works in the REPL, don't use it in real programs).

* What happens when you work with integers (like 0, 1, 2, 3) and floats (like 1.7, 8.1234, 3.14) together? What if the float is a whole number like 3.0?

* Store the results of your calculation in variables. Do more calculations with those variables.

* try this:

```
a = 0
a = a+1
```

* then press the up key to repeat a=a+1. Do it again. Do it a few times. Then print a.

* now enger a + 1. Pres the up key and hit enter a few times to do it more than once. What happens? What do you think the difference is?

* Try the ** (exponent) and // (floor division) and % (remainder or 'modulus') operators. Do you have a sense of what they do? 

## The help() function

* Type in help(print) what do you see?

* You can use help on most python commands, functions, and modules (we'll cover modules later).

* Note, if a help message is long you can move up and down with the arrow keys. Pressing 'q' gets you out.

## Exiting

* The quit() command exits the REPL.

## Extra investigation, the math module

* Type ``import math``

* Type math.sqrt(16)

* Type help(math) to see what's available.

* Use the up and down arrows to navigate a long help article. Press 'q' to exit a help view.

* Type help(math.cosh)

* Spend some time exploring this. Try the different functions on different inputs. Notice that some of them need more than one number. We'll talk about functions in a couple of days.

* Type ``from math import sqrt``

* Now type sqrt(16)

* Can you use the other functions without preceding them with math. ? Do you think you have an idea of what `` import `` and `` from import `` do?