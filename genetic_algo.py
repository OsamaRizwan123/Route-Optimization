import math
import random
from math import sin, cos, sqrt, atan2, radians

# City class to represent each city
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        dlon = self.x - city.x
        dlat = self.y - city.y
        a = sin(dlat / 2)**2 + cos(self.x) * cos(city.x) * sin(dlon / 2)**2
        dist = 2 * atan2(sqrt(a), sqrt(1 - a))
        if dist < 1:
            return 2 * atan2(sqrt(a), sqrt(1 - a))
        else:
            return round(2 * atan2(sqrt(a), sqrt(1 - a)), 2)

    def __repr__(self):
        return f"({self.x}, {self.y})"

# Function to read cities from a file
def read_cities(size):
    cities = []
    with open(f'test_data/cities_{size}.data', 'r') as handle:
        lines = handle.readlines()
        for line in lines:
            x, y = map(float, line.split())
            cities.append(City(x, y))
    return cities

# Fitness class to calculate the path cost and fitness of a route
class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def path_cost(self):
        if self.distance == 0:
            distance = 0
            for index, city in enumerate(self.route):
                distance += city.distance(self.route[(index + 1) % len(self.route)])
            self.distance = distance
        return self.distance

    def path_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.path_cost())
        return self.fitness

# Genetic Algorithm implementation
class GeneticAlgorithm:
    def __init__(self, iterations, population_size, cities, elites_num, mutation_rate, 
                 greedy_seed=0, roulette_selection=True, plot_progress=True):
        self.progress = []
        self.mutation_rate = mutation_rate
        self.cities = cities
        self.elites_num = elites_num
        self.iterations = iterations
        self.population_size = population_size
        self.greedy_seed = greedy_seed
        self.population = self.initial_population()
        self.average_path_cost = 1
        self.ranked_population = None

    def best_chromosome(self):
        return self.ranked_population[0][0]

    def best_distance(self):
        return 1 / self.ranked_population[0][1]

    def random_route(self):
        return random.sample(self.cities, len(self.cities))

    def initial_population(self):
        p1 = [self.random_route() for _ in range(self.population_size - self.greedy_seed)]
        greedy_population = [self.greedy_route(start_index=1, cities=self.cities) 
                             for start_index in range(self.greedy_seed)]
        return p1 + greedy_population

    @staticmethod
    def produce_child(parent1, parent2):
        gene_1 = random.randint(0, len(parent1))
        gene_2 = random.randint(0, len(parent1))
        start_gene = min(gene_1, gene_2)
        end_gene = max(gene_1, gene_2)
        child = [parent1[i] for i in range(start_gene, end_gene)]
        child += [gene for gene in parent2 if gene not in child]
        return child

    def generate_population(self):
        length = len(self.population) - self.elites_num
        children = []
        for i in range(length):
            child = self.produce_child(self.population[i], 
                                       self.population[(i + random.randint(1, self.elites_num)) % length])
            children.append(child)
        return children

    def mutate(self, individual):
        for index, city in enumerate(individual):
            if random.random() < max(0, self.mutation_rate):
                sample_size = min(max(3, self.population_size // 5), len(individual))
                random_sample = random.sample(range(len(individual)), sample_size)
                sorted_sample = sorted(random_sample)
                random_close_index = random.choice(sorted_sample[:max(sample_size // 3, 2)])
                individual[index], individual[random_close_index] = individual[random_close_index], individual[index]
        return individual

    def next_generation(self):
        self.rank_population()
        self.selection()
        self.population = self.generate_population()
        self.population[:self.elites_num] = [self.mutate(chromosome) 
                                             for chromosome in self.population[self.elites_num:]]
        return self.population
