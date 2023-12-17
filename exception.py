from random import randint

class BaseError(Exception):
    pass 
class HighValueError(BaseError):
    pass 
class LowValueError(BaseError):
    pass 

value = randint(0, 100) 
count = 0
while True: 
    try: 
        n = int(input("Enter a number: ")) 
        if n > value: 
            count += 1
            raise HighValueError 
        elif n < value: 
            count += 1
            raise LowValueError 
    except LowValueError:
        print("Very low value, give i/p again.") 
        print() 
    except HighValueError: 
        print("Very high value, give i/p again.") 
        print() 
    else:      
        print("Nice! You got the correct answer in",count,"tries!") 
        break