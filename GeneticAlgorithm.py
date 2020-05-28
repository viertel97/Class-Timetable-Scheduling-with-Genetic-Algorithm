import random as rnd

from Population import Population
from Schedule import Schedule

NUMBER_OF_ELITE_LECTURES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.2
POPULATION_SIZE = 10


class GeneticAlgorithm:
    def __init__(self, data):
        self._data = data

    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, population):
        crossover_population = Population(0, self._data)
        for i in range(NUMBER_OF_ELITE_LECTURES):
            crossover_population.get_schedules().append(population.get_schedules()[i])
        i = NUMBER_OF_ELITE_LECTURES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(population).get_schedules()[0]
            schedule2 = self._select_tournament_population(population).get_schedules()[0]
            crossover_population.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_population

    def _crossover_schedule(self, schedule1, schedule2):
        crossover_schedule = Schedule(self._data).initialize()
        for i in range(0, len(crossover_schedule.get_lectures())):
            if rnd.random() > 0.5:
                crossover_schedule.get_lectures()[i] = schedule1.get_lectures()[i]
            else:
                crossover_schedule.get_lectures()[i] = schedule2.get_lectures()[i]
        return crossover_schedule

    def _mutate_population(self, population):
        for i in range(NUMBER_OF_ELITE_LECTURES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _mutate_schedule(self, mutate_schedule):
        schedule = Schedule(self._data).initialize()
        for i in range(0, len(mutate_schedule.get_lectures())):
            if MUTATION_RATE > rnd.random():
                mutate_schedule.get_lectures()[i] = schedule.get_lectures()[i]
        return mutate_schedule

    def _select_tournament_population(self, pop):
        tournament_population = Population(0, self._data)
        for i in range(TOURNAMENT_SELECTION_SIZE):
            tournament_population.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
        tournament_population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_population
