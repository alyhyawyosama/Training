

class Person:
    def __init__(self,email,password,name):
        self.__name= name
        self.__email = email
        self.__password = password
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name


class Student(Person):
    student_count = 0 
    def __init__(self,email,password,name):
        super().__init__(email,password,name)
        self.courses = []
        Student.student_count +=1
        self.id = Student.student_count 
        
        
    def check_validaty(self,email,password):
        return self.get_password() == password and self.get_email() == email

    def show_data(self):
        print(f"Email:{self.get_email()} , name:{self.get_name()} ")

class Doctor(Person):
    doctor_count = 0 
    def __init__(self,email,password,name):
        super().__init__(email,password,name)
        self.teached_courses = []
        Doctor.doctor_count +=1
        self.id = Doctor.doctor_count
        
                
    def check_validaty(self,email,password):
        return self.get_password() == password and self.get_email() == email

    def show_data(self):
        print(f"Email:{self.get_email()} , Name:{self.get_name()} ")
    
    def show_my_courses(self):
        print("    Name    -    Code    ")
        i = 1
        if len(self.teached_courses) <1:
            print("You have not added any course yet.")
            return 
        for crs in self.teached_courses:
            print(str(i) + "- "+crs.name,crs.code,sep=("    ") )
            i+=1
    



class Course:
    course_count = 0    
    def __init__(self,doctor,name,code):
        Course.course_count += 1
        self.id =Course.course_count
        self.name =   name
        self.doctor = doctor
        self.assignments = []
        self.code = code
    
    def add_assignment(self,assignment):        
        self.assignments.append(assignment)
    
    def show_assignment(self):
        if len(self.assignments)<1:
            print("There is not any assignment")
            return False
        i = 1
        for assign in self.assignments :
            print(str(i)+"- "+ assign.title )
            i+=1
        return True
            
    
class Assignment:
    assignment_count = 0 
    def __init__(self):
        Assignment.assignment_count +=1
        self.id = Assignment.assignment_count
        self.title = None
        self.course = None
        self.maxGrade = 100
        self.solutions = []
    def set_title(self,title):
        self.title = title
        
    def set_course(self,course):
        self.course = course
    def set_maxGrade(self,grade):
        self.maxGrade = grade
        
    def add_solution(self,solution):
        self.solutions.append(solution)
        
    def show_solution(self):
        if len(self.solutions) < 1:
            print("There is not any solution")
            return False
        
        i = 1
        for sol in self.solutions:
            print(str(i)+"- "+sol.answer+"\t studentName:"+sol.student.name +"*  Grade:"+str(self.grade))
        return True
        
        
        
        
class Helper:
    def print_menu(items):
        count = 1
        print("\n\nchoose One of the following")
        for item in items:
            print(count,"- ",item)
            count+=1

            
    def validate_choice(low,high,msg="Enter Your choice :"):
        print(msg,end=" ")
        num = input()
        while not num.isdigit() :
            print("The intered must be integer ")
            num = input("Enter:")
        number = int(num)
        
        if  number <= high and number >= low :
            return number
        else :
            print(f"The intered choice must be between {low} - {high}")
            return Helper.validate_choice(low,high) 
            
        
class CourseManager:
    courses = []
#    def __init__(self):
    
    
class Solution:
    count = 0
    def __init__(self):
        Solution.count +=1
        self.id = Solution.count 
        self.answer 
        self.student
        self.grade 
    def set_grade(self,grade):
        self.grade = grade 

    
    
    
    
    
    
    
    
     
class DoctorController:
    def __init__(self):
        self.doctors = []
        self.currentUser = None
        
            
    def check_user(self,email,password):
        user = self.get_user(email,password) 
        if user != None :
            self.currentUser = user
            return True
        return False
    
    
    def get_user(self,email,password):
        for user in self.doctors :
            if user.check_validaty(email,password) == True :
                return user
        return None
    
    def login(self):
        email = input("Enter email:")
        password = input("Enter password:")
        while not self.check_user(email,password) :
            print("Your email or password incorrect,try again")
            email = input("Enter email:")
            password = input("Enter password") 
        self.take_control()
            
    def take_control(self):
        control = DoctorFlowController(self.currentUser)
        control.main()

            

class DoctorFlowController :
    def __init__(self,user):
        self.currentUser = user
    
    def main(self):
        items = ("Create new course","List my courses","Show my courses","Log out")
        while True:
            Helper.print_menu(items)
            choice = Helper.validate_choice(1, len(items) )  
            if choice == 1:
               self.create_course()
               
            elif choice == 2:
                self.list_courses()
            elif choice == 3:
                self.show_courses()

            elif choice == 4:
                return 
            else :
                assert False ,"Unexpected error" 
    
    def create_course(self):
        cours_name = input("Enter,Course name:")
        cours_code = input("Enter,Course code:")
        course = Course(self.currentUser, cours_name,cours_code)
        CourseManager.courses.append(course)
        self.currentUser.teached_courses.append(course)
        
        
    def list_courses(self):
        self.currentUser.show_my_courses();
        
    

    def show_courses(self):
        self.list_courses() 
        courses_count = len(self.currentUser.teached_courses)
        print(courses_count)
        choice = Helper.validate_choice(1, courses_count,"Enter course number:") -1
        cours = self.currentUser.teached_courses[choice-1]
        items = ("Add new assignment","Show solution")
        Helper.print_menu(items)
        choice = Helper.validate_choice(1, len(items)) 
        if choice == 1 :
            assignment = Assignment()
            title = input("Enter title:")
            assignment.set_title(title)
            maxGrade = Helper.validate_choice(1, 100,"Enter max grade:")
            assignment.set_maxGrade(maxGrade)
            assignment.course = cours
            cours.assignments.append(assignment)
        elif choice == 2 :
            ass = cours.show_assignment() 
            if ass == False :
                return 
            choice = Helper.validate_choice(1, len(cours.assignments)) -1
            assignment = cours.assignments[choice]
            ass = assignment.show_solution()
            if ass == False :
                return 
            choice = Helper.validate_choice(1, len(cours.assignments) ,"Enter the number of solution :")-1 
            solution = assignment.solutions[choice]
            grade = Helper.validate_choice(1,assignment.max,"Enter grade:")
            solution.set_grade(grade)
            
            
            
            
            
            
            
                

            
            
            

        
        
        
        
        

        
        
    
        
        
        
                
        
        
        
        
        
        

    









            
        