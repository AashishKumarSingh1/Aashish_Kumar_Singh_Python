class Student:

    def __init__(self,id,name,course=None):
        self.id=id 
        self.name=name
        self.courses=[course] if course is not None else []

    def enroll_in_course(self,course):
        if course in self.courses:
            raise ValueError(f"{self.name} is already enrolled in {course.title}!")
        self.courses.append(course)

    def __str__(self) -> str:
        result = f"Student Name: {self.name}\nEnrolled Courses:\n"
        for course in self.courses:
            result += f"- {course.title}\n"
        return result
    
class Teacher:
    Teacher_List={}
    def __init__(self,id,name,assigned_course=None):
        self.id=id
        self.name=name
        Teacher_List={
            id:name
        }
        # self.info={
        #     'id':id,
        #     'name':name
        #     }
        self.assigned_course=[assigned_course] if assigned_course is not None else []

    def assign_to_course(self, course):
        if course not in self.assigned_course:
            self.assigned_course.append(course)
            course.assign_teacher(self)
        else:
            print(f"{self.name} is already assigned to {course.title}")

    def __str__(self) -> str:
        course=[course for course in self.assigned_course]
        return f"{self.name} : Courses: {course}"

class Course:

    def __init__(self,id ,title,teacher=None) -> None:
        self.id=id 
        self.title=title
        self.teacher = [teacher] if teacher is not None else []

    def assign_teacher(self, teacher):
        if self.teacher is None:
            self.teacher = teacher
            teacher.assign_to_course(self)
        else:
            print(f"{self.title} already has a teacher assigned.")

    # def assign_teacher(self, teacher_id):
    #     if teacher_id not in Teacher.Teacher_List:
    #         raise ValueError(f"Teacher ID {teacher_id} is not assigned to any teacher!")
    
    #     Teacher.Teacher_List[teacher_id].append(self)

    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.enroll_in_course(self)
        else:
            print(f"{student.name} is already enrolled in {self.title}")


    def __str__(self) -> str:
        return f"{self.title} : id:{self.id}"

if __name__=='__main__':
    # Create teachers
    teacher1 = Teacher(1, "Mr. Smith")
    teacher2 = Teacher(2, "Ms. Johnson")

    # Create students
    student1 = Student(101, "Alice")
    student2 = Student(102, "Bob")

    # Create courses
    course1 = Course(201, "Mathematics")
    course2 = Course(202, "Science")

    # Assign teachers to courses
    course1.assign_teacher(teacher1)
    course2.assign_teacher(teacher2)

    # Enroll students in courses
    student1.enroll_in_course(course1)
    student2.enroll_in_course(course1)
    student1.enroll_in_course(course2)

    # Print details
    print(teacher1)
    print(teacher2)
    print(student1)
    print(student2)
    print(course1)
    print(course2)


    

    

