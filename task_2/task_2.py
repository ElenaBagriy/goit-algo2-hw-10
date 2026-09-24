# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()
    
    def assign_subjects(self, subjects):
        self.assigned_subjects.update(subjects)
    

def create_schedule(subjects, teachers):
   # Зберігатиме обраних викладачів
    schedule = []
    # Непокриті предмети
    uncovered_subjects = subjects.copy()
    # Поки є непокриті предмети
    while uncovered_subjects:
        # Знайдемо підмножину, яка покриває найбільшу кількість непокритих предметів
        best_subset = max(teachers, key=lambda teacher: (len(teacher.can_teach_subjects & uncovered_subjects), -teacher.age))
        if not (best_subset.can_teach_subjects & uncovered_subjects):
            return None
        # Додаємо цю підмножину до розкладу
        schedule.append(best_subset)
        best_subset.assign_subjects(best_subset.can_teach_subjects & uncovered_subjects)
        # Видаляємо покриті предмети з множини непокритих
        uncovered_subjects -= best_subset.can_teach_subjects & uncovered_subjects
    return schedule

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher(first_name = "Олександр", last_name = "Іваненко", age = 45, email = "o.ivanenko@example.com", can_teach_subjects = {'Математика', 'Фізика'}),
        Teacher(first_name = "Марія", last_name = "Петренко", age = 38, email = "m.petrenko@example.com", can_teach_subjects = {'Хімія'}),
        Teacher(first_name = "Сергій", last_name = "Коваленко", age = 50, email = "s.kovalenko@example.com", can_teach_subjects = {'Інформатика', 'Математика'}),
        Teacher(first_name = "Наталія", last_name = "Шевченко", age = 29, email = "n.shevchenko@example.com", can_teach_subjects = {'Біологія', 'Хімія'}),
        Teacher(first_name = "Дмитро", last_name = "Бондаренко", age = 35, email = "d.bondarenko@example.com", can_teach_subjects = {'Фізика', 'Інформатика'}),
        Teacher(first_name = "Олена", last_name = "Гриценко", age = 42, email = "o.grytsenko@example.com", can_teach_subjects = {'Біологія'})
        ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
