# Row and Column Sorting
---

Write a program that reads a matrix of numbers separated by newlines and whitespace, like this:

		10 5 4 20
		9 33 27 16
		11 6 55 3

then calculates the sums for each row and column. For our example above:

		Row Sums: 39 85 75
		Column Sums: 30 44 86 39

then prints two new matrices, one where the rows are sorted by their sums (ascending from top to bottom) and one where the columns are sorted by their sums (ascending from left to right). The correct output from the example above:

		10 5 4 20
		11 6 55 3
		9 33 27 16
		
		10 20 5 4
		9 16 33 27
		11 3 6 55


Find the large input matrix to import and test your program on inside `testmatrix.txt`.

For bonus points, format your output matrices nicely (align the columns, draw boxes with - and |...)