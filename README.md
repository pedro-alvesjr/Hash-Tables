# HashTable Class in Python

## Overview

This is a basic implementation of a **Hash Table** in Python, which provides efficient storage and retrieval of data through hashing. The class allows you to store key-value pairs in an array-like structure where keys are hashed using a custom hash function. The class also includes methods for printing the table's contents.

## Features

- **Customizable table size**: The size of the table can be specified during initialization (default is 7).
- **Custom hash function**: A simple hash function is used to map keys (strings) to indices in the table.
- **Collision handling**: Uses separate chaining (list of key-value pairs) to handle collisions.
- **Print table**: A method to print the entire table with its indices and values.
- **Retrieve values**: Fetch values associated with keys using `get_item`.
- **List all keys**: Retrieve a list of all keys currently stored in the table.

## Methods

### `__init__(self, value = 7)`
Initializes the hash table with a specified size. By default, the size is set to 7.

#### Parameters:
- `value` (int): The size of the hash table (default is 7).

---

### `__hash(self, key)`
Private method that generates a hash value for a given key (string). It calculates a hash by iterating through the letters of the key, using a basic algorithm (ord of each letter * 23) and taking modulo of the table size.

#### Parameters:
- `key` (str): The key to be hashed.

#### Returns:
- An integer that represents the index in the `data_map` array.

---

### `set_item(self, key, value)`
Inserts a key-value pair into the hash table. If a collision occurs, the pair is added to a list at that index.

#### Parameters:
- `key` (str): The key associated with the value.
- `value` (any): The value to store.

---

### `get_item(self, key)`
Retrieves the value associated with a given key.

#### Parameters:
- `key` (str): The key to look up.

#### Returns:
- The value associated with the key, or `None` if the key is not found.

---

### `print_table(self)`
Prints the contents of the hash table. It shows the index and the associated value at that index.

---

### `keys(self)`
Returns a list of all keys stored in the hash table.

#### Returns:
- `list[str]`: A list of all keys in the table.