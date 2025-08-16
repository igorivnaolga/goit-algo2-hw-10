class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


def create_schedule(subjects, teachers):
    schedule: [] = []
    uncovered_subjects = subjects.copy()

    while uncovered_subjects:
        best_teacher = max(
            teachers,
            key=lambda teacher: (
                len(teacher.can_teach_subjects & uncovered_subjects),
                -teacher.age,
            ),
        )
        best_teacher.assigned_subjects.update(
            best_teacher.can_teach_subjects & uncovered_subjects
        )
        uncovered_subjects -= best_teacher.can_teach_subjects & uncovered_subjects
        schedule.append(best_teacher)

    return schedule


if __name__ == "__main__":
    # Set of subjects
    subjects = {"Mathematics", "Physics", "Chemistry", "Informatics", "Biology"}
    # Creating a list of teachers
    teachers = [
        Teacher(
            "Oleksandr",
            "Ivanenko",
            45,
            "o.ivanenko@example.com",
            {"Mathematics", "Physics"},
        ),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Chemistry"}),
        Teacher(
            "Serhii",
            "Kovalenko",
            50,
            "s.kovalenko@example.com",
            {"Informatics", "Mathematics"},
        ),
        Teacher(
            "Nataliia",
            "Shevchenko",
            29,
            "n.shevchenko@example.com",
            {"Biology", "Chemistry"},
        ),
        Teacher(
            "Dmytro",
            "Bondarenko",
            35,
            "d.bondarenko@example.com",
            {"Physics", "Informatics"},
        ),
        Teacher("Olena", "Hrytsenko", 42, "o.grytsenko@example.com", {"Biology"}),
    ]

    # Calling the schedule creation function
    schedule = create_schedule(subjects, teachers)

    # Displaying the schedule
    if schedule:
        print("Class Schedule:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} years old, email: {teacher.email}"
            )
            print(f"   Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is not possible to cover all subjects with the available teachers.")
