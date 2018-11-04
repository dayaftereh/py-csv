# CSV and Python

This repository gives a short introudce into python to work with `csv` files.
The guide is only for windows.

## Install

Download the [embeddable python](https://www.python.org/downloads/windows/) for `32` or `64` bit depending on the system requirements.
Extract the downloaded `zip`-File into any directory.
However, currently the extracted directory contains a file like `pythonXX._pth`, where `XX` stands for the pythin version and the file is normaly next to the executable `python.exe`.
Because of same embeddable version the file needs to be removed to fix the import issue.

## Execute python

The next step is to execute the `python.exe` from a command line.
Let's open the `cmd` or `PowerShell` and execute the python interavtive console.

```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python"
Python 3.7.1rc2 (v3.7.1rc2:6c06ef7dc3, Oct 13 2018, 15:44:37) [MSC v.1914 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The interavtive console allows to execute python commands and can be exited with `exit()`.
Let's start with same exampels:

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
The python executable allows to execute `python`-File like scripts. 
The next shows the content of the file `test.py`.

```python
# text.py
print("Hello World")
```

The file can be executed with the python executable like the followring:
```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python" test.py
Hello World
C:\Users\user>
```

## Usage scsv

The `scsv`-module wrappes the `csv`-module from python standard library and simplify the usage.
The `scsv`-module can be downloaded from [scsv.py](./scsv.py) and placed in the directory next to the script.

For illustration the usage of the `scsv` the example `test.csv` with the folloring content:
```csv
key1;value1;2;value3;4
key2;value5;6;value7;8
key3;value9;10;value11;12
key4;value13;14;value15;16
```

Let's create the script `scsv-test.py` with the followring lines:
```python
# import the scsv
import scsv

# read the csv line by line
for line in scsv.read('test.csv', delimiter=';'):
    # prints the line to the console
    print(line)
```

To execute the `scsv-test.py` use the followring command:
```batch
C:\Users\user> "C:\Users\user\Downloads\python-3.7.1rc2-embed-amd64\python" test.py
['key1', 'value1', '2', 'value3', '4']
['key2', 'value5', '6', 'value7', '8']
['key3', 'value9', '10', 'value11', '12']
['key4', 'value13', '14', 'value15', '16']
```

