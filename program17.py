my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)
sorted_dict = dict(sorted(my_dict.items(), reverse=True))
print(sorted_dict)
