# GeneticAlgorithm_MinimumWeightedVertexCoverProblem
	
Implementation of genetic algorithm for Minimum Weighted Vertex Cover Problem (MWVCP). In MWVCP, required to find the vertex cover of a given graph such that the sum of the weights of the nodes is the minimum. A vertex cover of a graph is “a set of vertices such that each edge of the graph is incident to at least one vertex of the set”. 

The format of the graph files is as follows: 

-Number of nodes 

-Number of edges 

-List of node weights (format: X W where W is the weight of node X) 

-List of edges (format: X Y which indicates an edge from node X to node Y) 

The program gest five inputs as command-line arguments:

a.	Name of the graph file 

b.	Number of generations 

c.	Population size 

d.	Crossover probability 

e.	Mutation probability 

For each of the given three graphs, the program generates 100 and 400 generations with a population of size 100 and 200. For selection of parents, required to implement the binary tournament selection method. For crossover, use 1-point crossover operator with a probability of 0.5 or 0.9. Finally, for the mutation, bitwise mutation operator should be used with a probability of 1/n (n:number of nodes in the graph) and 0.05. 

 
