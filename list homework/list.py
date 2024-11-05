print("1. Creating a List")
ffruits_list = ['apple', 'watermelon', 'blueberry', 'banana', 'peach']
print(ffruits_list)

print("\n2. Accessing Elements")
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(colors[0],colors[2],colors[-1])

print("\n3. Modifying a List")
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

print("\nList Slicing")
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[:3]
print(subset)

print("\n5. Looping through a List")
listnumbers = [1,2,3,4,5,6,7,8,9,10]
for i in listnumbers:
    
    print(i ** 2)

print("\n6. List Methods: Append and Extend")
shopping_cart = []
shopping_cart.append("milk")
shopping_cart.append("bread")
shopping_cart.append("eggs")
extra_items = ["butter", "cheese"]
shopping_cart.extend(extra_items)
print(shopping_cart)

print("\n7. Finding Maximum and Minimum in a List")
ma_mi_numbers = [45, 22, 88, 56, 92, 33]
print("max number is",max(ma_mi_numbers))
print("min number is:",min(ma_mi_numbers))

print("\n8. Counting Occurrences")
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print("Amount of times when 'a' appeard in the list is",letters.count("a"))

print("\n9. List Comprehension")
list_compre = [l ** 2 for l in range(11) if l %2 == 0]
print(list_compre)

print("\n10. Removing Duplicates")
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
print(set(nums))