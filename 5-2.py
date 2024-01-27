import re


# class for creat users in system by other classes

class User:

    def __init__(self, user_id, title, key_word):
        self.id = user_id
        self.title = title
        self.key_word = key_word


class Course:

    def __init__(self, course_id, title, valency):
        self.course_id = course_id
        self.title = title
        self.valency = valency
        self.current_students = set()


# ckass for identify the Students in system

class Student(User):

    def __init__(self, user_id, title, key_word):
        super().__init__(user_id, title, key_word)
        self.courses = set()


# ckass for identify the Professors in system

class Professor(User):

    def __init__(self, user_id, title, key_word):
        super().__init__(user_id, title, key_word)
        self.courses_taught = set()


# class for runnimg main program and the error which wanted in program

class MainApp:

    def __init__(self):
        self.users = {}
        self.courses = {}
        self.commands = []
        self.counter = 0

    def sign_up(self, user_type, user_id, title, key_word):
        if user_type != "S" and user_type != "P":
            print("invalid type")
            return
        if user_id.isdigit() != True:
            print("invalid id")
            return
        if " " in title:
            print("invalid name")
            return

        if not (4 <= len(key_word) <= 20 and any(c in "*!@$%^&()" for c in key_word)):
            print("invalid password")
            return
        if user_id in self.users.keys():
            print("id already exists")
            return
        if user_type == "S":
            print("signed up successfully!")
            self.users[user_id] = Student(user_id, title, key_word)
            return
        elif user_type == "P":
            print("signed up successfully!")
            self.users[user_id] = Professor(user_id, title, key_word)
            return

    def log_in(self, user_id, key_word):
        if user_id not in self.users.keys():
            print("incorrect id")
            return
        user = self.users[user_id]

        if user.key_word != key_word:
            print("incorrect password")
            return

        if isinstance(user, Student):
            print("logged in successfully!\nentered student menu")
            self.student_menu(user)
        elif isinstance(user, Professor):
            print("logged in successfully!\nentered professor menu")
            self.professor_menu(user)

    def professor_menu(self, professor):
        while True:
            self.counter += 1
            command = self.commands[self.counter]
            if command == "edu log out edu":
                print("logged out successfully!")
                print("entered log in/sign up menu")
                return
            elif command == "edu show course list edu":
                self.show_course_list()
            elif command.startswith("edu add course -c "):

                pattern = re.compile(r'^edu add course -c (.+?) -i (.+?) -n (.+?) edu$')
                match = pattern.match(command)

                if match:
                    course_title = match.group(1)
                    course_id = match.group(2)
                    valency = match.group(3)

                else:
                    print("Invalid command")
                if " " in course_title:
                    print("invalid course name")
                elif course_id.isdigit() != True:
                    print("invalid course id")
                elif valency.isdigit() != True:
                    print("invalid course capacity")
                else:
                    self.add_course(professor, course_id, course_title, valency)
            elif command == "edu current menu edu":
                print("professor menu")
            else:
                print("invalid command")
        print("entered log in/sign up menu")

    def student_menu(self, student):
        while True:
            self.counter += 1
            command = self.commands[self.counter]
            if command == "edu log out edu":
                print("logged out successfully!")
                print("entered log in/sign up menu")
                return
            elif command == "edu show course list edu":
                self.show_course_list()
            elif command.startswith("edu get course -i "):
                course_id = command.split()[-2]
                self.get_course(student, course_id)
            elif command == "edu current menu edu":
                print("student menu")
            else:
                print("invalid command")

    def show_course_list(self):
        print("course list:")
        for course in self.courses.values():
            print(f"{course.course_id} {course.title} {len(course.current_students)}/{course.valency}")

    def get_course(self, student, course_id):
        if course_id not in self.courses:
            print("incorrect course id")
            return

        course = self.courses[course_id]

        if student in course.current_students:
            print("you already have this course")
        elif len(course.current_students) >= course.valency:
            print("course is full")
        else:
            course.current_students.add(student)
            print("course added successfully!")

    def add_course(self, professor, course_id, course_title, valency):
        if course_id in self.courses:
            print("course id already exists")
            return

        self.courses[course_id] = Course(course_id, course_title, int(valency))
        print("course added successfully!")

    def main(self):
        while True:
            try:
                line = input().strip()
                if line == 'edu exit edu':
                    break
                self.commands.append(line)
            except EOFError:
                break

        while True:
            if self.counter == len(self.commands):
                break
            command = self.commands[self.counter]
            if command == "edu exit edu":
                break
            elif command == "edu current menu edu":
                print("log in/sign up menu")
            elif command.startswith("edu sign up -"):
                pattern = re.compile(r'^edu sign up -(.+?) -i (.+?) -n (.+?) -p (.+?) edu$')
                match = pattern.match(command)
                if match:
                    user_type = match.group(1)
                    user_id = match.group(2)
                    title = match.group(3)
                    key_word = match.group(4)
                else:
                    print("invalid command")
                    self.counter += 1
                    continue
                self.sign_up(user_type, user_id, title, key_word)
            elif command.startswith("edu log in -"):
                pattern = re.compile(r'^edu log in -i (.+?) -p (.+?) edu$')
                match = pattern.match(command)

                if match:
                    user_id = match.group(1)
                    key_word = match.group(2)
                else:
                    print("invalid command")
                    self.counter += 1
                    continue

                self.log_in(user_id, key_word)
            else:
                print("invalid  command")
            self.counter += 1


# run the program

if __name__ == "__main__":
    app = MainApp()
    app.main()