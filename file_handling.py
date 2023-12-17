n = int(input("Enter the count of numbers: "))

print("Enter", n, "numbers:")

with open("T1.txt", "w") as f:
    for i in range(n):
        f.write(str(input()) + "\n")
    

with open("T1.txt", "r") as f1, open("T2.txt", "w") as f2:
    l = list()
    for i in f1:
        l.append(int(i))
    
    l.sort()

    for i in range(n):
        f2.write(str(l[i]) + "\n")
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        