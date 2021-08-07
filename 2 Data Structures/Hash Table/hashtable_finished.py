# Hash Tables : Form of an associative array! Data structure that maps keys to its associated values using a hash function. This function uses the key to compute an index into the slots that are in the hash table and map the key to the value. Ideally, a hash function will assign each key to a unique slot in the table where the values are stored. Key to value mappings are unique. Hash tables are typically fast. For small datasets, arrays or linked list are usually more efficient as there wont be any collisions to resolve. Hash tables dont order entries in a predictable way. 

# A hash table is an associative array where a hash function uses a key to compute an index value and to map to the data value.

# demonstrate hashtable usage

# create a hashtable all at once
items1 = dict({"key1": 1, "key2": 2, "key3": "three"})
print(items1)


# create a hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# try to access a nonexistent key
#print(items1["key6"])

# replace an item
items2['key2'] = "two"
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.items():
    print("key: ", key, " value: ", value)
