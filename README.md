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

On the other hand, the python executable allows to script files. 
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
To get closer with python, let's start with the dynamic type system.
The dynamic system of python allows that a variable can be of any type.
The following types are the important types in python.

* `integer` - a positive or negative numbers 1, 2, 3, etc., or zero. 
* `float` - a floating-point number like `3.14`
* `string` - a text like `Hello WOrld`
* `list` - a list with other types

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

