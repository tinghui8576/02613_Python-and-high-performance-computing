class Student:
    def __init__(self, name, courses):
        self.Name = name
        self.Courses = courses
    def attends(self, cour_name):
        
        return cour_name in self.Courses

    
# s = Student('X', ['01005', '02613'])
# print(s.attends('01005'))
students = [Student('D', []), Student('A', ['01005']), Student('B', ['02613']), Student('C', ['01005', '02613'])]

class Student:
    def __init__(self, name, courses):
        self.Name = name
        self.Courses = courses
    def attends(self, cour_name):
        
        return cour_name in self.Courses
    
def coursestudents(students, cour_name):
    return [s.Name for s in students if s.attends(cour_name)]

print(coursestudents(students, '01005'))

