my_list = [1, "apple", 4.2, "banana", 5]
print(my_list)

my_iterator = iter(my_list)
for value in my_iterator:
    if value == "apple":
        next_element = next(my_iterator)
        print(next_element)