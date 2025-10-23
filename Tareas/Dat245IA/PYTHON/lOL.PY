import random
modelEnd = [1,1,1,1,1,1,1,1,1,1] 
largeIndividual = 10 
num = 10 
pressure = 3 #individual>2
mutation_chance = 0.2 

def individual(min, max):
    return[random.randint(min, max) for i in range(largeIndividual)]

def newPopulation():
    return [individual(1,9) for i in range(num)]

def functionType(individual):
    fitness = 0
    for i in range(len(individual)):
        if individual[i] == modelEnd[i]:
            fitness += 1
    return fitness

def selection_and_reproduction(population):
    evaluating = [ (functionType(i), i) for i in population]
    evaluating = [i[1] for i in sorted(evaluating)]
    population = evaluating
    selected = evaluating[(len(evaluating)-pressure):]
    for i in range(len(population)-pressure):
        pointChange = random.randint(1,largeIndividual-1)
        father = random.sample(selected, 2)
        population[i][:pointChange] = father[0][:pointChange]
        population[i][pointChange:] = father[1][pointChange:]
    return population

def mutation(population):
    for i in range(len(population)-pressure):
        if random.random() <= mutation_chance: 
            pointChange = random.randint(1,largeIndividual-1) 
            new_val = random.randint(1,9) 
            while new_val == population[i][pointChange]:
                new_val = random.randint(1,9)
            population[i][pointChange] = new_val
    return population

 
population = newPopulation()

for i in range(100):
    population = selection_and_reproduction(population)
    population = mutation(population)
    

print("\nEndless Population:\n%s"%(population))

