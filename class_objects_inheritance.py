# class MyClass:
#     a = 10

# p1 = MyClass()
# print(p1.a)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("John",10)

# print(p1)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
    
#     def printname(self):
#         print(self.fname,self.lname)

# p1 = Person("John","Jain",34)
# p1.printname()

# p1.fname = "Hiena"
# p1.printname()

# del p1.age
# del p1


# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(self.fname,self.lname)
    
# class Student(Person):
#     def __init__(self,fname,lname):
#         super().__init__(fname,lname)

# s1 = Student("Yui","Jain")
# s1.printname()



class Employee:
    emp_list = {}
    manager = {}

    def __init__(self,fname,lname,eid,type):
        self.fname = fname
        self.lname = lname
        self.eid = eid
        self.type = type
        self.emp_list[eid] = self

    def info(self):
        return(self.fname,self.lname,self.eid,self.type)

class Manager(Employee):
    def __init__(self,fname,lname,eid):
        super().__init__(fname,lname,eid,"Manager")
        super().manager[eid] = self
        self.dev = {}
        self.test = {}
        self.man_emp = {}

    def add(self,obj):
        Employee.emp_list[obj.eid] = obj

        if obj.type == "Developer":
            self.dev[obj.eid] = obj
        else:
            self.test[obj.eid] = obj

        self.man_emp[obj.eid] = obj

    def remove(self, eid, type):
        del super().emp_list[eid]

        if (type == 'Developer'):
            del self.dev[eid]
        else:
            del self.test[eid]

        del self.man_emp[eid]

    def display(self):
        for i in self.man_emp:
            print(i,":",str(self.man_emp[i].info()))
        
    def manager_list(self):
        return(super().manager)


class Developer(Employee):
    def __init__(self,fname,lname,eid):
        super().__init__(fname,lname,eid,"Developer")
    
class Tester(Employee):
    def __init__(self,fname,lname,eid):
        super().__init__(fname,lname,eid,"Tester")

manager1 = Manager("Vijay","Harkare", 10)
# print(manager1.info())

# print(manager1.display())

manager1.add(Developer("Anaida","Lewis",20))
manager1.add(Tester("Ayush","Jaon",11))

manager1.display()

