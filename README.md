# CSV and Python

This repository gives a short introduce into python to work with `csv` files.
The guide is only for windows.

## Dependencies

 * Visual C++ Redistributable for Visual Studio 2015

## Install

Download the last [embeddable python](https://www.python.org/downloads/windows/) for `32` or `64` bit depending on the system requirements.
Extract the downloaded `zip`-File into an directory.
However, the current embeddable python has the [issue](https://bugs.python.org/issue34841) with import modules from the same directory.
For fixing the issue the file `pythonXX._pth` (next to the `python.exe`) in the extracted directory needs to be removed.
The `XX` stands for the embeddable python version.

## Execute python


The next step is to execute the `python.exe` from a command line.
Let's open the `cmd` or `PowerShell` and execute the python interactive console.

```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python"
Python 3.7.1rc2 (v3.7.1rc2:6c06ef7dc3, Oct 13 2018, 15:44:37) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The interactive console allows to execute python commands and can be exited with `exit()`.
Let's start with same simple examples:

```python
>>> 5 * 5
25
>>> 5 + 5 == 10
True
>>> "Hello World"
'Hello World'
>>> x = 10
>>> x * 5
50
>>> exit()
```

On the other hand, the python executable allows to run script files. 
Script files are simple `txt` files with the ending `*.py`
However, let's create the file `test.py` with the following content.

```python
# text.py
print("Hello World")
```

The script file can be executed with the python executable by adding the file name as a start-parameter.

```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python" test.py
Hello World
C:\Users\user>
```

This executes the file and prints `Hello World` to the console.

## Python Tutorial

Let's get started with the basics of python.

### Types

To get closer with python, let's start with the dynamic type system.
The dynamic system of python allows that a variable can be of any type.
For detailed information checkout the python [Built-in Types](https://docs.python.org/3/library/stdtypes.htm).
The following types are the common used types in python.

* [integer](https://docs.python.org/3/library/functions.html#int) - a positive or negative numbers 1, 2, 3, etc., or zero. 
* [float](https://docs.python.org/3/library/functions.html#float) - a floating-point number like `3.14`
* [string](https://docs.python.org/3/library/stdtypes.html#textseq) - textual data like `Hello World`
* [list](https://docs.python.org/3/library/stdtypes.html#lists) - a list with other python types like `[1, 2, 3]`
* [dictionary](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) - a map with `key => value` like `{'a':1, 'b':2, 'c':3}`

The following shows the usage of the types.
```python
# integer
x = 42
# float
x = 3.14
# string
x = "Hello World"
# list
x = [ 1, 2, 3, 4 ]
x = [ "a", "b", "c" ]
# dict
x = {'a':1,'b':2,'c':3}
```

Python allows to convert between the different types.
```python
# string to integer
x = int("42")
# string to float
x = int("3.14")
# integer to string
x = str(42)
# float to string
x = str(3.14)
# list to string
x = str([1,2,3])
```

### Python & Math

Let's have a deeper look into the mathematics operations and the [In-Build math](https://docs.python.org/3/library/math.html) module.
Starting with same simple math stuff:
```python
# add
x = 1 + 1 # x = 2
# subtract
x = 1 - 1 # x = 0
# multiply
x = 2 * 2 # x = 4
# divide
x = 4 / 2 # x = 2
x = 2 / 3 # x = 0.6666666666666666
# double pi
pi2 = 3.14 * 2 # pi2 = 6.28
# negated
x = -pi2 # x = -6.28
```

Let's use the [In-Build math](https://docs.python.org/3/library/math.html) module for more complex math functions.
```python
import math
# abs
x = abs(-1) # x = 1
# sqrt
x = math.sqrt(9) # x = 3.0
# pow
x = pow(2, 4) # x = 16
# pi
x = math.pi # x = 3.141592653589793
# sin
x = math.sin(math.radians(90)) # x = 1.0
# infinity
x = math.inf # x = inf
# negative infinity
x = -math.inf # x = -inf
```

For more information checkout the python documentation on [Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex).

### Comparisons

Python has a standard [comparisons](https://docs.python.org/3/library/stdtypes.html#comparisons) for numeric types `integer` and `float`.
The comparisons always return `True` or `Flase`.
Let's check some comparisons.
```python
# strictly less than
x < y
# less than or equal
x <= y
# strictly greater than
x > y
# greater than or equal
x >= y
# equal
x == y
# not equal
x != y
```

The comparisons can be combined with the [Boolean Operations](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not) from python to write complex evaluates.
```python
x or y	# if x is false, then y, else x
x and y # if x is false, then x, else y
not x # if x is false, then True, else False
# and
x = True and False # x = False
x = True and True # x = True
x = False and True # x = False
x = False and False # x = False
# or
x = True or False # x = True
x = False or False # x = False
x = True or True # x = True
x = False or True # x = True
# not
x = not True # x = False
x = not False # x = True
```

### Flow controls

Python has the usual control flow statements known from other languages.
A advanced information can be found in the python documentation at [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html).

#### `if`-Statements

The `if`-statements is the best known flow control and allows to evaluate comparisons and boolean operations.
Let's dive deeper into the `if`-statements:
```python
x = 42
if x < 42:
    print("x less 42")
elif x > 42:
    print("x greater 42")
else:
    print("x is 42")
```

#### `for`-Statements

The `for`-Statements allows to loop over a list in python.
```python
words = ["cat", "world", "hello"]
for w in words:
    print(w)
```

### List

The list is a important and inbuild type in python.
However, the easiest way is to get familiar with `list`, checkout the following usages:
```python
# define list
l = [1, 2, 3]
l = ['a', 'b', 'c']
l = ["cat", "world", "hello"]
# length of a list
l = [1, 2, 3, 4]
length = len(l) # length = 4
# access at index
l = [1, 2, 3] # or use range(3)
a1 = l[0] # a1 = 1
a2 = l[1] # a1 = 2
a3 = l[2] # a1 = 3
# overwrite at index
l[1] = 0 # l = [1, 0, 3]
# append to list
l = [1, 2, 3] 
l.append(4) # l = [1, 2, 3, 4]
# remove element from list
l = [1, 2, 3] 
l.remove(2) # l = [1, 3]
# check if value in list
l = range(3) # l = [1, 2, 3,]
x = 2 in l # x = True
x = 4 in l # x = False
# use for
l = [1, 2, 3]
for n in l:
    print(n)
# usage range and for
length = 10
for i in range(length):
    print(i)
```

More information can be found in the documentation at [More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

### Dictionary

TODO

## Usage `scsv`

The `scsv`-module wraps the `csv`-module from python standard library and simplify the usage.
The `scsv`-module can be downloaded from [scsv.py](./scsv.py) and placed in the directory next to the script.

For illustration the usage of the `scsv` the example `test.csv` with the following content:
```csv
key1;value1;2;value3;4
key2;value5;6;value7;8
key3;value9;10;value11;12
key4;value13;14;value15;16
```

Let's create the script `scsv-test.py` with the content:
```python
# import the scsv
import scsv

# read the csv line by line
for line in scsv.read('test.csv', delimiter=';'):
    # prints the line to the console
    print(line)
```

To execute the `scsv-test.py` like the following:
```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python" test.py
['key1', 'value1', '2', 'value3', '4']
['key2', 'value5', '6', 'value7', '8']
['key3', 'value9', '10', 'value11', '12']
['key4', 'value13', '14', 'value15', '16']
```

Let's get a little more complex and multiply the third value by two and print the result.
```python
# import the scsv
import scsv

# read the csv line by line
for line in scsv.read('test.csv', delimiter=';'):
    # gets the third value, make it to int and multiply it with two
    print(int(line[2]) * 2)
```

Remember `line` is a list where the first value is added with index `0`.
The execution of the script looks like the following:
```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python.exe" ./test.py
4
12
20
28
```

The next example tries to find duplicated keys in the `csv`-File.
```python
import scsv

# define a new dict to store found keys
map = {}
# read the csv line by line
for line in scsv.read('test.csv', delimiter=';'):
    # check if the key already in the dict
    if line[0] in map:
        # print the duplicated key
        print ('Found duplicated', line[0])
    else:
        # store the found key in dict
        map[line[0]] = True
```

To check if the code works the `test.csv` requires a duplicated key, for the next execute the `key1` line is duplicated.
```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python.exe" ./test.py
Found duplicated key1
```