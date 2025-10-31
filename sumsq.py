n=int(input("enter how many numbers: "))
sum_sq=0
for i in range(n):
    num=int(input(f"enter number {i+1}: "))
    sum_sq+=num**2
print("sum of squares =",sum_sq)
