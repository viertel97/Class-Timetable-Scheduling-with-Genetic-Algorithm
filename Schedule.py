import random as rnd

from Lecture import Lecture


class Schedule:
    def __init__(self, data):
        self._data = data
        self._lectures = []
        self._number_of_conflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._is_fitness_changed = True

    def get_lectures(self):
        self._is_fitness_changed = True
        return self._lectures

    def get_number_of_conflicts(self):
        return self._number_of_conflicts

    def get_fitness(self):
        if self._is_fitness_changed:
            self._fitness = self.calculate_fitness()
            self._is_fitness_changed = False
        return self._fitness

    def initialize(self):
        courses = self._data.get_courses()
        for i in range(0, len(courses)):
            modules = courses[i].get_modules()
            for j in range(0, len(modules)):
                new_meeting_time = self._data.get_meeting_times()[rnd.randrange(0, len(self._data.get_meeting_times()))]
                new_lecture = Lecture(self._classNumb, courses[i], modules[j], new_meeting_time)
                self._classNumb += 1

                new_lecture.set_room(self._data.get_rooms()[rnd.randrange(0, len(self._data.get_rooms()))])

                new_lecture.set_docent(
                    modules[j].get_docents()[rnd.randrange(0, len(modules[j].get_docents()))])
                self._lectures.append(new_lecture)
        return self

    def calculate_fitness(self):
        self._number_of_conflicts = 0
        classes = self.get_lectures()
        for i in range(0, len(classes)):
            seating_capacity = classes[i].get_room().get_seating_capacity()
            number_of_students = classes[i].get_course().get_number_of_students()
            if seating_capacity < number_of_students:
                self._number_of_conflicts += 1
            for j in range(0, len(classes)):
                if j >= i:
                    if (classes[i].get_meeting_time() == classes[j].get_meeting_time() and
                            classes[i].get_id() != classes[j].get_id()):
                        if classes[i].get_room() == classes[j].get_room():
                            self._number_of_conflicts += 1
                        if classes[i].get_docent() == classes[j].get_docent():
                            self._number_of_conflicts += 1
                        if classes[i].get_course() == classes[j].get_course():
                            self._number_of_conflicts += 1
        return 1 / (1.0 * self._number_of_conflicts + 1)

    def __str__(self):
        return_value = ""
        for i in range(0, len(self._lectures) - 1):
            return_value += str(self._lectures[i]) + " | "
        return_value += str(self._lectures[len(self._lectures) - 1])
        return return_value
