Remove The Dupes!
==================
##### DESCRIPTION
---
You have a string "aabbccddeded". We want to remove all the _consecutive_ duplicates and put them in a separate string, which yields two separate instances of the string "abcdeded".

##### PUBLIC INTERFACE
---
```
remove_duplicate(<string>)
    @params string to remove duplicates from
```
##### TEST CASES
---
```python
>>> remove_duplicate("balloons")
("balons", "lo")
>>> remove_duplicate("aabbccddeded")
("abcdeded", "abcd")
>>> remove_duplicate("flabby aapples")
("flaby aples", "bap")
```

[Returning Multiple Values(Did Not Read)]:https://www.safaribooksonline.com/library/view/python-cookbook-3rd/9781449357337/ch07s04.html
[Learn Python The Hard Way(Did Not Read)]:http://learnpythonthehardway.org/book/ex21.html
[Tutorials Point(Did Not Read)]:http://www.tutorialspoint.com/python/python_functions.htm
[High Order Functions(Did Not Read)]:http://effbot.org/pyfaq/how-do-you-make-a-higher-order-function-in-python.htm