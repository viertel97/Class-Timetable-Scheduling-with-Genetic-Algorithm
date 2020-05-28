from Data import Data
from GeneticAlgorithm import POPULATION_SIZE, GeneticAlgorithm
from Population import Population
from Print import print_available_data, print_current_population, print_stats


def main():
    data = Data()
    print_available_data(data)

    generation_number = 0
    conflicts = []

    population = Population(POPULATION_SIZE, data)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    print_current_population(population, generation_number)

    geneticAlgorithm = GeneticAlgorithm(data)

    while population.get_schedules()[0].get_fitness() != 1.0:
        generation_number += 1
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        print_current_population(population, generation_number)
        conflicts.append(population.get_schedules()[0].get_number_of_conflicts())
    print_stats(generation_number, conflicts, data)


if __name__ == '__main__':
    main()
