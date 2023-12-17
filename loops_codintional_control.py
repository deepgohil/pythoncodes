# Print the given triangle pattern using for loop.

# for i in range(0,6):
#     for j in range(i):
#         print(i, end=" ")
#     print()
    
    
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print('')

# h=int(input('Enter height: '))   
# for x in range(h):
#     print(" " * (h - x), "*" * (2*x + 1))
# for x in range(h - 2, -1, -1):
#     print(" " * (h - x), "*" * (2*x + 1))

# # Find the factorial of a number using for loop.
# n = int(input("Enter the number"))

# result = 1

# for i in range(1, n+1):
#     result *= i

# print(result)

# # Print the Fibonacci sequence up to given 'n' value using for loop.
n = int(input("Enter the number of terms : "))

a = 0
b = 1

if n == 1:
    print(a)
elif n >= 2:
    print(a)
    print(b)
    for _ in range(n - 2):
        c = a + b
        a = b 
        b = c
        print(c)

