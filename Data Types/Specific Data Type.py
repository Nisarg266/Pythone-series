# Python Specific Data Types - Examples and Outputs

# String
x = str("Hello World")  # str
print(type(x), x)       # <class 'str'> Hello World

# Integer
x = int(20)             # int
print(type(x), x)       # <class 'int'> 20

# Float
x = float(20.5)         # float
print(type(x), x)       # <class 'float'> 20.5

# Complex Number
x = complex(1j)         # complex
print(type(x), x)       # <class 'complex'> 1j

# List
x = list(("apple", "banana", "cherry"))  # list
print(type(x), x)                        # <class 'list'> ['apple', 'banana', 'cherry']

# Tuple
x = tuple(("apple", "banana", "cherry")) # tuple
print(type(x), x)                        # <class 'tuple'> ('apple', 'banana', 'cherry')

# Range
x = range(6)             # range
print(type(x), list(x))  # <class 'range'> [0, 1, 2, 3, 4, 5]

# Dictionary
x = dict(name="John", age=36)  # dict
print(type(x), x)              # <class 'dict'> {'name': 'John', 'age': 36}

# Set
x = set(("apple", "banana", "cherry"))  # set
print(type(x), x)                       # <class 'set'> {'banana', 'cherry', 'apple'}

# Frozenset
x = frozenset(("apple", "banana", "cherry"))  # frozenset
print(type(x), x)                             # <class 'frozenset'> frozenset({'banana', 'cherry', 'apple'})

# Boolean
x = bool(5)           # bool
print(type(x), x)     # <class 'bool'> True

# Bytes
x = bytes(5)          # bytes
print(type(x), x)     # <class 'bytes'> b'\x00\x00\x00\x00\x00'

# Bytearray
x = bytearray(5)      # bytearray
print(type(x), x)     # <class 'bytearray'> bytearray(b'\x00\x00\x00\x00\x00')

# Memoryview
x = memoryview(bytes(5))  # memoryview
print(type(x), x)         # <class 'memoryview'> <memory at 0x...>