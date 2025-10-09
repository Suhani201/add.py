n = int(input("Enter how many numbers you want to add:"))
total=0
for i in range(n):
    num = float(input("Enter number(i+1):"))
    total+=num
print("the sum of the numbers is:",total)