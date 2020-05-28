class Course:
    def __init__(self, name, modules, number_of_students):
        self._name = name
        self._modules = modules
        self._number_of_students = number_of_students

    def get_name(self): return self._name

    def get_modules(self): return self._modules

    def get_number_of_students(self): return self._number_of_students
