class StudentDetails:
    def __init__(self,name,marks,course):
        self.name=name
        self.marks=marks
        self.course=course
    
    def printObj(self):
        print(f'{self.name} is a {self.course} student.His marks is {self.marks}')

kabil=StudentDetails("Kabil",78,"Computer Science")
dhanu=StudentDetails("Dhanu",87,"Software Engineering")

kabil.printObj()
dhanu.printObj()