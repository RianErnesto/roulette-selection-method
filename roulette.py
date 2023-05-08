from utils import fitnessesSummation
from utils import returnProbabilities
from utils import returnPortions
from utils import orderFitnesses
from utils import spinRoulette
from utils import returnFraction

population = ["A", "B", "C", "D", "E", "F"]
fitness = [30, 22, 45, 53, 21, 109]
population, fitness = orderFitnesses(fitness, population)
probabilities = []
portions = []
summation = 0
values = [1, 61, 82, 21, 279, 6, 11]

summation = fitnessesSummation(fitness)
probabilities = returnProbabilities(fitness, summation)
portions = returnPortions(fitness, summation)

for i in values:
    print("Value: ", i, "Individual: ", population[spinRoulette(portions, False, returnFraction(i, fitness))])
