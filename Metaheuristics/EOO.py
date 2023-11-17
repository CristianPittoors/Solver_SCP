import random
import numpy as np

def initialize_population(population_size):
    return [random.uniform(-10, 10) for _ in range(population_size)]

def calculate_fitness(solution):
    # Aquí debes definir tu función de fitness basada en tu problema específico

    return abs(solution)

def update_position(solution, t, e, c, x_best, l):
    #print(x_best)
    #print("#################################################")
    #print(solution)
    y = t + e + l * random.uniform(0, 1) * (np.array(x_best) - np.array(solution))
    #y = [t + e + l * random.uniform(0, 1) * x for x in (np.array(x_best) - np.array(solution))]
    #print(c)
    new_solution = [x * c for x in solution]
    #print("#################################################")
    #print(new_solution)
    #print("#################################################")
    return new_solution + y
    

def iterarEOO(maxIter, iter, dimension, poblacion, fitness):
    #population = initialize_population(population_size)
    #x_best = min(population, key=calculate_fitness)
    iter = maxIter - iter + 1
    #for i in list(range(max_iter + 1))[::-1]:
    new = []
    for EO in poblacion:
        l = random.uniform(3, 5)
        t = ((l - 5) / (5 - 3)) * 10 - 5
        e = ((iter - 1) / (len(poblacion) - 1)) - 0.5 if iter > 1 else (1 / (len(poblacion) - 1)) - 0.5
        c = ((l - 3) / (5 - 3)) * 2 + 0.6

        new.append(update_position(EO, t, e, c, fitness, l))
        
        #x_best = min(population, key=calculate_fitness)

    return np.array(new)

# Ejemplo de uso
#population_size = 40
#iterations = 40000
#best_solution = eo_algorithm(population_size, iterations)

#print("Mejor solución encontrada:", best_solution)
#print("Valor de fitness:", calculate_fitness(best_solution))