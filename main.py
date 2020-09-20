from GeneticAlgorithm import GeneticAlgorithm
import sys
import matplotlib.pyplot as plt

file_name = "003.txt"
generations = 100
pop_size = 200
crossover_prob = 0.5
mutation_prob = 0.05

if len(sys.argv) == 6:
    try:
        file_name = sys.argv[1]
        generations = int(sys.argv[2])
        pop_size = int(sys.argv[3])
        crossover_prob = float(sys.argv[4])
        mutation_prob = float(sys.argv[5])
    except ValueError:
        print("Your inputs are invalid. Please correct them. (Use \".\" for floats)")
        exit(0)


def run(file_name, generations, pop_size, crossover_prob, mutation_prob):
    algorithm = GeneticAlgorithm(file_name, generations, pop_size, crossover_prob, mutation_prob)
    algorithm.run()
    print("Result is feasible:", algorithm.check_feasibility_of_best())

    fig = plt.figure()
    plt.plot(algorithm.fitness_data)
    plt.grid()
    plt.xlabel('Generation #')
    plt.ylabel('Avg. Fitness')
    plt.title(file_name + ", Gener: " + str(generations) + ", Pop: " + str(pop_size) + ", Cross: " + str(
        crossover_prob) + ", Mut: " + str(mutation_prob) + "\nBest Fitness: " + str(round(algorithm.best.fitness, 4)))
    fig.savefig(file_name + "_" + str(generations) + "_" + str(pop_size) + "_" + str(crossover_prob) + "_" + str(
        mutation_prob) + ".png")
    plt.clf()
    plt.cla()
    plt.close(fig)


run(file_name, generations, pop_size, crossover_prob, mutation_prob)
