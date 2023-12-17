# #list
# l = ['apple', 'banana', 'mango']
# l.append('orange')
# print(l)

# x = l.copy()
# print(x)

# print(l.count('apple'))

# l2 = ['bmw', 'mercedes', 'ford']
# l.extend(l2)
# print(l)

# print(l.index('ford'))
# l.insert(3, 'peach')
# print(l)

# l.pop(2)
# print(l)

# l.remove('apple')
# print(l)

# l.reverse()
# print(l)

# l.sort()
# print(l)

# l.clear()
# print(l)

# # set
# s = {"apple", "banana", "cherry"}
# print(s)
# s.add('orange')
# print(s)
# x = s.copy()
# print(x)
# y = {"google", "microsoft", "apple"}
# z = x.difference(y)
# print('difference',z)
# s.discard('banana')
# print(s)
# z = x.intersection(y)
# print(z)
# z = x.union(y)
# print(z)
# s.pop()
# print(s)
# s.clear()
# print(s)

# #Dictionary
# d = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = d.copy()
# print(x)

# x = d.keys()
# print(x)

# d.pop('model')
# print(d)

# x = d.get('brand')
# print(x)

# x = d.values()
# print(x)

# x = d.items()
# print(x)

# d.clear()
# print(d)


def histogram(l):
    count = 0
    x = []
    k = []
    for i in range(len(l)):
        count = 0
        for j in range(i, len(l)):
            if l[i] == l[j] and l[i] not in k:
                count += 1
        k = k + [l[i]]
        if count != 0:
            x = x + [(l[i], count)]
    
    x.sort()
    x = sorted(x, key = lambda x: x[1])
    return x

print("Enter the numbers:")
print(histogram(list(map(int, input().split()))))

# # Implement lambda function to find greater of the 2 input numbers
# a = int(input("Enter number a : "))
# b = int(input("Enter number b : "))
# maximum = lambda a,b : a if a > b else b
# print(f"Maximum : {maximum(a,b)}")

# # Using map function perform element wise addition of elements of two lists.
# list1 = []
# list2 = []

# n1 = int(input("Enter the number of elements in list 1"))
# print("Enter the elements")
# list1 = list(map(int, input().split()))[:n1]

# n2 = int(input("Enter the number of elements in list 2"))
# print("Enter the elements")
# list2 = list(map(int, input().split()))[:n2]

# result = list(map(lambda a, b: a+b, list1,list2))
# print("The list of element-wise sum of the two lists is: ", str(result))
