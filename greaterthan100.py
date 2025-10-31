numbers=[int(x)for x in input("enter integers separated by  spaces: ").split()]
result = ['over' if num >100 else num for num in numbers]
print("modified list:",result)
