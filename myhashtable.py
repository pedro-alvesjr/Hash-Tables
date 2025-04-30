class HashTable:
    def __init__(self, value = 7):
        self.data_map = [None] * value
        

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
# ------------------------
# TESTS
# ------------------------

print("Creating HashTable...")
ht = HashTable()

print("\nSetting items...")
ht.set_item("apple", 100)
ht.set_item("banana", 200)
ht.set_item("grape", 300)
ht.set_item("orange", 400)
ht.set_item("apricot", 500)  # May cause a collision

print("\nGetting items...")
print("apple:", ht.get_item("apple"))     # Expected: 100
print("banana:", ht.get_item("banana"))   # Expected: 200
print("grape:", ht.get_item("grape"))     # Expected: 300
print("orange:", ht.get_item("orange"))   # Expected: 400
print("apricot:", ht.get_item("apricot")) # Expected: 500
print("nonexistent:", ht.get_item("pear"))# Expected: None

print("\nPrinting table...")
ht.print_table()

print("\nKeys in table:")
print(ht.keys())  # Should print all inserted keys