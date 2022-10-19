# if-else
if __name__ == '__main__':
    n = int(input().strip())
    
if n % 2 != 0:
    print("Weird")    
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#  Arithmatic Operators
a = int(input())
b = int(input())

sum = a + b
difference = a - b
product = a * b
    
print(sum)
print(difference)
print(product)

# Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    int_div = a // b
    float_div = a / b
    
    print(int_div)
    print(float_div)

# loops
if __name__ == '__main__':
    n = int(input())
   
for i in range(0,n):
    print(i**2)

# leap year
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year == 2100:
        leap = False  
    return leap

# print function
if __name__ == '__main__':
    n = int(input())
for i in range(1, n+1):
  print(i, end = '')

# list comphrehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input()) 

print([[i,j,k]
       for i in range(0,x+1) 
       for j in range(0,y+1)
       for k in range(0,z+1) 
       if i + j + k != n])
