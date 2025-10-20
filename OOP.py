class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []              #Оконченные курсы студента
        self.courses_in_progress = []           #Курсы которые в процессе
        self.grades = {}   #Оценки
    def average_grade(self):
        if not self.grades:
            return 0
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __str__(self):
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grade()}\nКурсы в процессе обучения:{courses_in_progress_str}\nЗавершенные курсы:{finished_courses_str}')


    def rate_lecture(self,lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []   #За каким курсом закпеплён преподаватель

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grade(self):
        if not self.grades:
            return 0

        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades)

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции:{self.average_grade()}\n'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        print(f"Reviewer {self.name} проверяет работу {student.name}")
        result = super().rate_hw(student, course, grade)      # Вызываем родительский метод
        return result
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)

# Задание №1

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

# Задание №2

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}

#Задание №3

some_reviewer = Reviewer('Пётр','Иванов')
some_lecturer = Lecturer('Игнат','Высоцкий')
some_student = Student('Михаил','Раскошный', 'М')

some_lecturer.courses_attached = ['Python', 'Math'] # инициируем лектора для получения оценок
student.courses_in_progress = ['Python', 'Math']     # инициируем студента для выставления оценок
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']

student.rate_lecture(some_lecturer, 'Python', 9)
student.rate_lecture(some_lecturer, 'Python', 8)
student.rate_lecture(some_lecturer, 'Math', 10)
student.rate_lecture(some_lecturer, 'Math', 7)



print(some_reviewer)
print(some_lecturer)
print(some_student)

student1 = Student('Ruoy', 'Eman', 'male')
student1.grades = {'Python': [9, 10, 8], 'Git': [10, 9]}

student2 = Student('Maria', 'Ivanova', 'female')
student2.grades = {'Python': [8, 7, 9], 'Math': [10, 8]}

# сравниваем студентов
print(student1 > student2)   # True (9.2 > 8.4)
print(student1 == student2)  # False
print(student1 <= student2)  # False
print(student1 != student2)  # True

# создаем лекторов
lecturer1 = Lecturer('Ivan', 'Petrov')
lecturer1.grades = {'Python': [9, 8, 10]}  # Средняя: 9.0

lecturer2 = Lecturer('Anna', 'Sidorova')
lecturer2.grades = {'Math': [7, 8, 9]}     # Средняя: 8.0

# сравниваем лекторов
print(lecturer1 > lecturer2)
print(lecturer1 == lecturer2)
print(lecturer1 >= lecturer2)

# сортировка списков
students = [student2, student1]
lecturers = [lecturer2, lecturer1]
