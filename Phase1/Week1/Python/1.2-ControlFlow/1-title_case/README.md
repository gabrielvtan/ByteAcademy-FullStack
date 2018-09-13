Title Transform
===============
##### DESCRIPTION
---
Write a function that transforms a string into [title case].
This mostly means capitalizing only every first letter of every word in the string.
However, there are some non-obvious exceptions to title case which can't easily be hard-coded. Your function must accept, as a second argument, a set or list of words that should not be capitalized. 

Furthermore, the first word of every title should always have a capital leter.
 
##### PUBLIC INTERFACE
---
```
titlecase(<title>,<exceptions>)
    @param title - string to transform
    @param exceptions - list of words to keep lowercase
```
##### TEST CASES
---
```python
>>> exceptions = ['jumps', 'the', 'over']
>>> titlecase('the quick brown fox jumps over the lazy dog', exceptions)
"The Quick Brown Fox jumps over the Lazy Dog"

>>> exceptions = ['are', 'is', 'in', 'your', 'my']
>>> titlecase('THE vitamins ARE IN my fresh CALIFORNIA raisins', exceptions)
"The Vitamins are in my Fresh California Raisins"
```
[comment]:Resources

[title case]:http://en.wikipedia.org/wiki/Letter_case#Headings_and_publication_titles
[LC Hawk]:http://www.secnetix.de/olli/Python/list_comprehensions.hawk
[LC Read The Docs]:http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Comprehensions.html
[Python For Beginners]:http://www.pythonforbeginners.com/basics/list-comprehensions-in-python
[Dive Into Python 3]:http://www.diveintopython3.net/comprehensions.html