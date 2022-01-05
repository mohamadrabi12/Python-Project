class Person:
     def __init__(self, name, age,id,gender):
        self.name = name
        self.age = age
        self.id=id
        self.gender=gender

     def print(self):
        print(f"Person: name=  {self.name}, id={self.id}, gender={self.gender} age={self.age}")
##################################################################################
class Worker(Person):
     def __init__(self, name, age,id,gender):
        super().__init__(name, age,id,gender)
        self.salary=1000

     def print(self):
        super().print();
        print(f" Salary= {self.salary}")

##################################################################################
class Student(Person):
    def __init__(self, name, age,id,gender):
        super().__init__(name, age,id,gender)
        self.location="Israel"
        self.subject="CS"

    def print(self):
        super().print();
        print(f" Study Location= {self.location}, Subject={self.subject}")
##################################################################################
class Teacher(Person):
    def __init__(self, name, age,id,gender):
        super().__init__(name, age,id,gender)
        self.seniority=10
        self.subject="Math"

    def print(self):
        super().print();
        print(f" Seniority= {self.seniority}, Subject={self.subject}")

##################################################################################
class Cinema:
    def __init__(self, name, price):
        self.name=name
        self.price=price
        self.studentSale=10
        self.teacherSale=20

def getPersons(persons):
    persons.insert(0,Student("aaaaa",20,123456789,True));
    persons.insert(1,Teacher("bbbb",20,123456871,False));
    persons.insert(2, Worker("ccc",20,123456765,True));

def show(persons,cinema):
     studentCounter=teacherCounter=wokerCounter=0
     total=0
     for p in persons:
         if isinstance(p,Student):
             studentCounter=studentCounter+1;
             total=total+ cinema.price-(cinema.price*cinema.studentSale/100)
         if isinstance(p,Teacher):
             total=total+ cinema.price-(cinema.price*cinema.teacherSale/100)
             teacherCounter=teacherCounter+1;
         if isinstance(p, Worker):
             total = total + cinema.price
             wokerCounter = wokerCounter + 1;

     print(f" total pay= {total}, price = {cinema.price}")
     allCounter=teacherCounter+studentCounter+wokerCounter
     print(f"teacherCounter={teacherCounter},studentCounter={studentCounter} , wokerCounter={wokerCounter} , allCounter={allCounter} ")

if __name__ == '__main__':
   c=Cinema("my Cinema",120);
   persons=[]
   getPersons(persons);
   show(persons,c)



