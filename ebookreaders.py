#Give three examples of life-critical applications.

    # checking blood sugar levels in someone's body
    # robot assisted surgeries
    # checking oxygen levels while sleeping

#Suppose you are on the design team for a new e-book reader. What are the primary classes and methods that the Python software for your reader will need?
#You must include a class diagram for this code, but you do not need to write any actual code. Your software architecture should at least include ways for
#customers to buy new books, view their list of purchased books, and read their purchased books. Numerous examples of class diagrams can be found by doing
#a search for "class diagram" in your favorite search engine.  At a minimum you must include 3+ classes and those classes must have attributes and methods.
#You should have more than just setter/getter methods.
    
    #

#In addition to these tasks, you must post an explanation of your class diagram from question #2.
#This allows you to demonstrate what would theoretically be occurring and how it is organized.  

class EBookReaderSystem:
    def __init__(self, pages)
    
class LibraryItem:
    
class newBooks(EBookReaderSystem):
    def __init__()
    
class listOfBooks(EBookReaderSystem):
    def __init__()
    
class readBooks(EBookReaderSystem):
    def __init__()


class SchoolMember:
'''Represents any school member.'''
def __init__(self, name, age):
self.name = name
self.age = age
print('(Initialized SchoolMember: {})'.format(self.name))

def tell(self):
'''Tell my details.'''
print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
'''Represents a teacher.'''
def __init__(self, name, age, salary):
SchoolMember.__init__(self, name, age)
self.salary = salary
print('(Initialized Teacher: {})'.format(self.name))

def tell(self):
SchoolMember.tell(self)
print('Salary: "{:d}"'.format(self.salary))


class Student(SchoolMember):
'''Represents a student.'''
def __init__(self, name, age, marks):
SchoolMember.__init__(self, name, age)
self.marks = marks
print('(Initialized Student: {})'.format(self.name))

def tell(self):
SchoolMember.tell(self)
print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

# prints a blank line
print()

members = [t, s]
for member in members:
# Works for both Teachers and Students
member.tell()