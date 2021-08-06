# Note: Dictionaries cannot store duplicate keys. Duplicate values can be stored.

sal_info = {'Boston': 91185, 'Austin': 90171}
print(sal_info)
# Changing values of the key in the dictionary sal_info
sal_info['Boston'] = 95128
print(sal_info)
# Adding new entry
sal_info['Atlanta'] = 105128
print(sal_info)
print(len(sal_info))
# Deleting an entry
del sal_info['Atlanta']
print(sal_info)
print(len(sal_info))
# To clear all the data from the dictionary use clear() method
sal_info.clear()
print(sal_info)
print(len(sal_info))

# Dictionaries, like lists, have both functions and methods - making it very versatile. we give dictionary as a parameter to the len method above and then we can also call a method clear() on it using the dot operator. 

# Iterating through the dictionary
sal_info = dict()
print(sal_info)
sal_info = {'Austin': 911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286}
print(sal_info)

if('Dallas' in sal_info):
    print(sal_info['Dallas'])
else:
    print("Not Found")

# prints values
for location in sal_info:
    print(sal_info[location])

# prints keys
for location in sal_info:
    print(location)

if('Seattle' not in sal_info):
    sal_info['Seattle'] = 110340
else:
    print("Key exists! ")

print(sal_info)
#del sal_info
#print(sal_info)

# .get(key, default message) method
print(sal_info.get('Dallas', "Not Found"))
print(sal_info.get('Portland', "Not Found"))
# .key() method
print(sal_info.keys())
# .value() method
print(sal_info.values())
# .items() method returns both
print(sal_info.items())

print("Key-Value pairs")
for k, v in sal_info.items():
    print("The key is: ", k, ". The value is: ", v)

# max() method
print("City with highest salary: " + max(sal_info, key=sal_info.get))

# min() method
print("City with lowest salary: " + min(sal_info, key=sal_info.get))

# pop() method
print("Value of the key " + str(sal_info.pop('Dallas', "not found")))
print(sal_info)

print(sal_info.popitem())
print(sal_info)

print(sorted(sal_info.keys()))
print(sorted(sal_info.values()))


# Using Python lists within a dictionary! i.e. Dictionary of Lists! 
# A dictionary ket can only be immutable (cannot be changed!) This means a list data structure cannot be a key, but a key can most certainly hold a list of values. Values dont have to immutable. They are mutable (can be changed!)

eng_dic = {}

# Adding lists as value
eng_dic['solitude'] = ['lone', 'lonely', 'alone', 'unaccompanied', 'without someone']
eng_dic['hope'] = ['aspiration', 'desire', 'wish', 'expectation', 'ambition']
print(eng_dic)

# Creating a dictionary with an empty list and then appending the list! 
eng_dic.clear()
eng_dic = {'solitude': []}
eng_words = ['lone', 'lonely', 'alone', 'unaccompanied', 'without someone']
eng_dic['solitude'].append(eng_words[0])
print(eng_dic)

eng_dic['solitude'] = eng_words
print(eng_dic)

if(eng_dic.get('solitude')):
    for list_item in eng_dic['solitude']:
        print(list_item)
else:
    print("Word not in Dictionary!")


# Dictionaries VS. Lists - Both are known as Collections 'coz they group multiple values together. 
# When choosing a collection type, it is useful to understand the properties of that type. 
# Choosing the right type of data structure/dataset could mean retention of meaning and it could mean an increase in efficiency or security. 

# List - It is a collection which is ordered and changeable. Allows duplicate members. It is a collection of index-value pairs as that of an array in C++. Created by placing elements in the square brackets. In a list, the indices are integers starting from zero and the elements are accessed via indices. Order of the elements in a list are maintained. 


# Dictionary - It is a collection which is unordered, changeable, and indexed, no duplicate members. A hashed structure of key-value pairs. Created by placing elements in the curly brackets. When accessing element in dictionary, we use square bracket with the key within the brackets.  Keys of a dictionary can be any data type as long as they are immutable. Elements are accessed via key values. No guarantee for maintaining the order in a dictionary. It is inserted in the order in which it is added. 

sal_info_keys = ["Austin", "Portland", "Dallas"]
sal_info_values = [91185, 110123, 89123]

# Printing original keys-value lists
print("Original Key lists is: " + str(sal_info_keys))
print("Original Value lists is: " + str(sal_info_values))

# to convert lists to dictionary:
sal_info = {}

print("#### Method 1 using for in ")
index = 0
for key in sal_info_keys:
    value = sal_info_values[index]
    sal_info[key] = value
    index = index + 1

# Printing resultant dicitionary
print("Resultant dictionary is: " + str(sal_info))


# Python TUPLES: It is a collection that is ordered and unchangeable, and is indexed. Allows duplicate members. 

# Python SETS: A collection which is unordered and unindexed. No duplicate members. 

# Python DICTIONARIES: A collection that is unordered, changeable, and indexed. No duplicate keys, but values can be duplicated. 

# Dictionaries, lists, and tuples give better control in accessing the data

# Dictionaries and sets havev fast access times compared to lists and tuples. 

# Both sets and dictionaries data structures have very fast access times compared to list and tuples. Just like list and dictionaries, elements in the set has to be immutable. 
# Tuples: 
Cities = ('Austin', 'Portland', 'Dallas')
print(Cities[0])

print(Cities)

# Dicitonaries:
citi_info = {'Austin': 81111, 'Dallas': 91234}
print(citi_info['Dallas'])
print(citi_info)

# Sets: 
city_names_set = {'Austin', 'Portland', 'Dallas', 'Austin'}
print(city_names_set)
# Print order is not predictable. 
for set_value in city_names_set:
    print(set_value)


# Python Dictionary Data Structure : Hash Table 
# Python dictionary is highly optimized. Hashing is a tried and tested Table lookup optimization. 
# A dict-hash table in Python is stored in memory as an array. It is a specialized kind of array called the sparse-table i.e. it always has empty cells. 
# goal of a hash table is to keep the data evenly distributed across the table. Keep at least one-third empty. If its too crowded, then it's copied to a new location with a larger size. Not a good idea to modify the dictionary while iterating through it.
# If you need to scan and add items to a dictionary, do in 2 steps: read the dictionary from start to finish and collect the needed additions in a second dictionary, then update the first one with it. 

# Hashable objects that compare equal - will need to have the same hash value consistently

# Dictionaries keys must be immutable - for ex: str, bytes, numeric.

# Cells in the hash tables are often called buckets

# Consequences of using a hash table : Keys must be immutable. Significant memory overhead (although with Python 3.6, using of spare arrays has solved this issue). Key search is very fast. Key ordering depends on the insertion order. Adding items to the dictionary may change the order of the exisiting keys. 