class StudentDetails:
    name="Kabil" # class attributes
    course_name="Computer Science"
    age=21
    
    def printObj(self): # method- function in a class
        print(f'{self.name} is a {self.course_name} student and he is {self.age} years old.')


StudentDetails.name="M.Kabileshwaran" # setting class attribute
kabil=StudentDetails()
kabil.printObj()
dhanush=StudentDetails()
dhanush.name="Dhanush" # setting instance attribute
dhanush.age=19
dhanush.course_name="Software Engineering"

dhanush.printObj()