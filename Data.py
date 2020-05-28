from Course import Course
from Docent import Docent
from MeetingTime import MeetingTime
from Module import Module
from Room import Room


class Data:
    def __init__(self):
        rooms = [["2.56CR", 40], ["2.18", 40], ["2.20", 55]]
        meeting_times = [
            ["1. Block", "09:50 – 11:20"],
            ["2. Block", "11:30 – 13:00"],
            ["3. Block", "13:45 – 15:15"],
            ["4. Block", "15:30 – 17:00"]
        ]
        docents = [
            ["HOZ", "Holzheuer, Heiko"],
            ["EWE", "Ewering, Christian"],
            ["NUW", "Nüßer, Wilhelm"],
            ["JAA", "Jäsche, Andreas"],
            ["JAP", "Janacik, Peter"],
            ["PAD", "Padberg, Carsten"]
        ]

        self._rooms = []
        self._meeting_times = []
        self._docents = []
        self.fill_objects(rooms, meeting_times, docents)

        module1 = Module("ISM", "IT-Strategie und -management",
                         [self.get_docent("HOZ")])
        module2 = Module("OR", "Operations Research - Methoden und Anwendungen",
                         [self.get_docent("EWE")])
        module3 = Module("TT", "Technologie-Trends",
                         [self.get_docent("NUW"), self.get_docent("HOZ")])
        module4 = Module("SIC", "Strategieimplementierung und Changemanagement",
                         [self.get_docent("JAA")])
        module5 = Module("CM", "Complexity Management",
                         [self.get_docent("JAP")])
        module6 = Module("MIC", "Methoden und Instrumente des Controlling",
                         [self.get_docent("PAD")])
        self._modules = [module1, module2, module3, module4, module5, module6]

        course1 = Course("PFMI419A", [module1, module3, module4], 20)
        course2 = Course("PFMV419A", [module2, module4, module5], 20)
        course3 = Course("PFMF419A", [module4, module5, module6], 50)
        self._courses = [course1, course2, course3]

    def get_docents(self):
        return self._docents

    def get_rooms(self):
        return self._rooms

    def get_modules(self):
        return self._modules

    def get_courses(self):
        return self._courses

    def get_meeting_times(self):
        return self._meeting_times

    def fill_objects(self, rooms, meeting_times, docents):
        for i in range(0, len(rooms)):
            self._rooms.append(Room(rooms[i][0], rooms[i][1]))
        for i in range(0, len(meeting_times)):
            self._meeting_times.append(MeetingTime(meeting_times[i][0], meeting_times[i][1]))
        for i in range(0, len(docents)):
            self._docents.append(Docent(docents[i][0], docents[i][1]))

    def get_docent(self, name):
        return next((docent for docent in self._docents if docent.get_id() == name), None)
