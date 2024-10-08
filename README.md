# Into to Object Oriented Programming

You will notice that this task is slightly different

Rather than writing functions into a single Python file, you have a number of empty Python files

For each task you will be required to create Classes to fit the brief given - the classes will go into the corresponding Python file

Ensure you follow any instructions about class names etc, as these are important for the test file

## Task 1 - Circle
For this task you must create a class called `Circle`, with a constructor which reads in a numeric value for the circles radius and sets it as an attribute

The Circle class should have two additional methods which are named `get_area` and `get_perimeter`

Note, the formulas for circles are:

* Area: $$ \pi r^2 $$
* Perimeter: $$ 2\pi r $$

Where r is the radius

You can take the value of pi to be 3.141

Round the answers to the nearest whole integer

Example:
```
circy = Circle(11)
circy.getArea()

# Should return 380.132711084365 -> rounds down to 380

circy = Circle(4.44)
circy.getPerimeter()

# Should return 27.897342763877365 -> rounds up to 28
```

## Task 2 - Name Class

Write a class called Name and create the following attributes given a first name and last name (as fname and lname):
* An attribute called `fullname` which returns the first and last names
* An attribute called `initials` which returns the first letters of the first and last name, put a `.` between the two letters

Example:

```
a1 = Name("john", "SMITH")
a1.fname ➞ "John"
a1.lname ➞ "Smith"
a1.fullname ➞ "John Smith"
a1.initials ➞ "J.S"
```

Notes:
* Make sure only the first letter of each name is capitalised.
* Check the Resources tab for some helpful tutorials on Python classes.