original_numbers = list(range(1,11))
print(f'Original numbers: {original_numbers}')

squared = lambda x: x**2
squared_numbers= list(map(squared, original_numbers))
print(f'Squared numbers: {squared_numbers}')

even = lambda x: x % 2 == 0
even_numbers = list(filter(even, original_numbers))
print(f'Even numbers: {even_numbers}')

list_dictionary = [{"name" : "Monitor", "price" : 150},
                   {"name" : "Keyboard", "price" : 25},
                   {"name" : "Mouse", "price" : 30}]

sorted_dict = sorted(list_dictionary, key= lambda x: x["price"])

print("Products sorted by price")
for item in sorted_dict:
    print(f'{item["name"]}- ${item["price"]}')