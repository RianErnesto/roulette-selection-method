import random

def orderFitnesses(fitnesses, population):
    for i in range(len(fitnesses)):
        for j in range(len(fitnesses)):
            if fitnesses[i] < fitnesses[j]:
                fitnesses[i], fitnesses[j] = fitnesses[j], fitnesses[i]
                population[i], population[j] = population[j], population[i]
    return population, fitnesses

def fitnessesSummation(fitnesses):
    summation = 0
    for i in range(len(fitnesses)):
        summation += fitnesses[i]
    return summation


def returnProbabilities(fitnesses, summation):
    probabilities = []
    for i in range(len(fitnesses)):
        probabilities.append(fitnesses[i]/summation)
    return probabilities


def returnFraction(number, fitnesses):
    return number/fitnessesSummation(fitnesses)


def returnPortions(fitnesses, summation):
    portions = []
    step = 0
    for i in range(len(fitnesses)):
        portions.append((step, step + fitnesses[i]/summation))
        step += fitnesses[i]/summation
    return portions


def spinRoulette(portions, random=True, value = 0):
    if random:
        r = random.random()
        for i in range(len(portions)):
            if r >= portions[i][0] and r < portions[i][1]:
                return i
    else:
        for i in range(len(portions)):
            if value >= portions[i][0] and value < portions[i][1]:
                return i