class Teacher:
    def init(self, id, name):
        self.id = id
        self.name = name

    def str(self):
        return f"Teacher(id={self.id}, name={self.name})"


class Student:
    def init(self, id, name):
        self.id = id
        self.name = name

    def str(self):
        return f"Student(id={self.id}, name={self.name})"


class StudyGroup:
    def init(self, teacher, students):
        self.teacher = teacher
        self.students = students

    def str(self):
        student_list = ", ".join(str(student) for student in self.students)
        return f"StudyGroup(teacher={self.teacher}, students=[{student_list}])"


class StudyGroupService:
    def create_study_group(self, teacher, students):
        return StudyGroup(teacher, students)


class StudyGroupController:
    def init(self):
        self.study_group_service = StudyGroupService()

    def create_study_group(self, teacher_id, student_ids):
        teacher = self.get_teacher_by_id(teacher_id)
        students = self.get_students_by_ids(student_ids)
        return self.study_group_service.create_study_group(teacher, students)

    def get_teacher_by_id(self, id):
        # Здесь должна быть логика получения преподавателя из БД или другого источника
        # Пример: возвращаем временного преподавателя
        return Teacher(id, f"Teacher {id}")

    def get_students_by_ids(self, ids):
        # Здесь должна быть логика получения студентов из БД или другого источника
        # Пример: возвращаем временных студентов
        students = [Student(id, f"Student {id}") for id in ids]
        return students


# Пример использования:
if __name__ == "main":
    controller = StudyGroupController()
    teacher_id = 1
    student_ids = [101, 102, 103]
    study_group = controller.create_study_group(teacher_id, student_ids)
    print(study_group)