tuple1 = (22,23,45,12,25,67,55,32)
tuple2 = ("apple", "banana", "cherry","mango","orange”)
tuple3 = (30,40,50,60,20,45)  # Nested tuple
tuple4 = ()  # Empty tuple
tuple5 = (200,)  # Single-element tuple

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3 (Nested):", tuple3)
print("Tuple 4 (Empty):", tuple4)
print("Tuple 5 (Single element):", tuple5)

# Accessing Elements
print("\nFirst element of tuple1:", tuple1[0])
print("Last element of tuple1:", tuple1[-1])

# Slicing
print("\nSliced tuple1 (index 1 to 3):", tuple1[1:4])

# Concatenation
tuple_concat = tuple1 + tuple2
print("\nConcatenated Tuple:", tuple_concat)

# Repetition
tuple_repeat = tuple2 * 2
print("\nRepeated Tuple:", tuple_repeat)
# Membership Testing
print("\nIs 'apple' in tuple2?", 'apple' in tuple2)
print("Is 6 in tuple1?", 6 in tuple1)
# Iteration
print("\nIterating through tuple1:")
for item in tuple1:
    print(item, end=" ")
# Length of Tuple
print("\nLength of tuple1:", len(tuple1))
# Maximum and Minimum (only works for numeric tuples)
print("Max of tuple1:", max(tuple1))
print("Min of tuple1:", min(tuple1))
# Count and Index
tuple6 = (1, 2, 2, 3, 4, 2, 5)
print("\nCount of 2 in tuple6:", tuple6.count(2))
print("Index of 3 in tuple6:", tuple6.index(3))
# Converting a List to a Tuple
list1 = [10, 20, 30]
tuple_from_list = tuple(list1)
print("\nConverted List to Tuple:", tuple_from_list)
# Deleting a Tuple
del tuple5  # Tuples are immutable; we can only delete the entire tuple
print("\nTuple5 deleted successfully.")
