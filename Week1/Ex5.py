class StudentTranscript:
    unniversity_name = "Al-Khwarizmi University"
    max_course = 6
    grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
    gpa = None
    avg_gpa = None
    def __init__(self, name, id, major, courses = None):
        self.student_name = name
        self.id = id
        self.major = major
        self.courses = []
        for course in courses:
            if self.valid_course(course):
                self.courses.append(course)

    def valid_course(self):
        if isinstance(self.courses["name"], str):
            return True
        if 1 <= self.courses["credits"] <= 4:
            return True
        if self.courses["grade"] in StudentTranscript.grades:
            return True
        return False
    def add_course(self, course_name, credits, grade):
        temp_dict = {}
        temp_dict["name"] = course_name
        temp_dict["credits"] = credits
        temp_dict["grade"] = grade
        if self.valid_course(temp_dict):
            self.courses.append(temp_dict)
    def calculate_gpa(self):
        total_credits = 0
        total = 0
        for course in self.courses:
            total_credits += course["credits"]
            total += course["grade"] * StudentTranscript.grades[course["credits"]]
        avg_gpa = total/total_credits
        StudentTranscript.avg_gpa = avg_gpa
        print(avg_gpa)
    def get_standing(self, gpa=None):
        if gpa == None:
            self.gpa = gpa
            StudentTranscript.gpa = gpa
        if self.gpa >= 3.5:
            print("Excellent")
        if self.gpa >= 3.0:
            print("Good")
        if self.gpa >= 2.0:
            print("Satisfactory")
        if self.gpa >= 1.0:
            print("Poor")
        else:
            print("Failing")
    def get_honors_status(self):
        if self.gpa < 4:
            return "No honors"
        elif self.gpa >= 3.8:
            return "Highest honors"
        elif self.gpa >= 3.5:
            return "High honors"
        elif self.gpa >= 3.0:
            return "Honors"
        else:
            return "No hours"
    def generate_transcript(self):
        print(StudentTranscript.unniversity_name)
        print(f"Student: {self.student_name} | ID: {self.id} | Major: {self.major}")
        print(40*"-")
        for course in self.courses:
            print(f"  {course["name"]} {course["credits"]:>20} cr  Grade: {course["grade"]}")
        print(40*"-")
        print(f"GPA {StudentTranscript.gpa}/4.0")
        print(f"Average GPA: {StudentTranscript.avg_gpa}")
        print(f"Standing: {self.get_standing}")
        print(f"Honors status: {self.get_honors_status}")




