import json
import requests
import random

#Parameters
population = 20
generations = 1000

#The selection process is applied to the list of chromosomes with this rate.
selection_rate = 0.2 #MAX 1.0

#The mutation process is applied to each individual gene with this rate.
mutation_rate = 0.1 #MAX 1.0


class Chromosome:

	def __init__(self):
		
		self.fitness = -999999.9
		
		#Genes
		self.phi1 = random.randint(0, 360)
		self.phi2 = random.randint(0, 360)
		self.phi3 = random.randint(0, 360)
		self.theta1 = random.randint(0, 360)
		self.theta2 = random.randint(0, 360)
		self.theta3 = random.randint(0, 360)
		

	def __str__(self):

		return 'Fitness: ' + str(self.fitness) + '\n' + 'phi1: ' + str(self.phi1) + ' | phi2: ' + str(self.phi2) + ' | phi3: ' + str(self.phi3) + '\n' + 'theta1: ' + str(self.theta1) + ' | theta2: ' + str(self.theta2) + ' | theta3: ' + str(self.theta3) + '\n'

def geneticAlgorithm():

	#Initial population.
	chromosomes =  [Chromosome() for _ in range(population)]
	best_chromosome = Chromosome()

	for generation in range(generations):

		print('\nGeneration: ' + str(generation) + '\n')

		#Calculating the fitness for each chromosome of the population.
		chromosomes = fitness(chromosomes)

		#Saving the best result until now.
		if best_chromosome.fitness < chromosomes[0].fitness:
			best_chromosome = chromosomes[0]

		#Selecting the best portion of the population.
		chromosomes = selection(chromosomes)
		chromosomes = crossover(chromosomes)
		chromosomes = mutation(chromosomes)
	
	return best_chromosome

def fitness(chromosomes):

	for chromosome in chromosomes:

		src = "https://aydanomachado.com/mlclass/02_Optimization.php?phi1=" + str(chromosome.phi1) + "&theta1=" + str(chromosome.theta1) + "&phi2=" + str(chromosome.phi2) + "&theta2=" + str(chromosome.theta2) + "&phi3=" + str(chromosome.phi3) + "&theta3=" + str(chromosome.theta3) + "&dev_key=Machine big deep data learning vovozinha science"
		request = json.loads(requests.get(src).text)
		chromosome.fitness = float(request['gain'])
		print(chromosome.fitness)

	return sorted(chromosomes, key=lambda chromosome: chromosome.fitness, reverse=True)

def selection(chromosomes):

	#Once the chromosome list is already ordered at this point, the best part of the population is at the beginning of the list.
	return chromosomes[:int(selection_rate * len(chromosomes))]

def crossover(chromosomes):
	
	selected = chromosomes
	selected_size = len(selected)

	#The loop stops when the population returns to the original size.
	for _ in range(population - selected_size):
		#This process takes 2 random chromosomes of the previously selected list to generate a new chromosome.
		parent1 = random.choice(selected)
		parent2 = random.choice(selected)

		if random.randint(0, 100) < 50:
			chromosomes.append(generateChild(parent1, parent2))
		else: 
			chromosomes.append(generateChild(parent2, parent1))

	return chromosomes

def generateChild(parent1, parent2):

	child = Chromosome()

	child.phi1 = parent1.phi1
	child.phi2 = parent1.phi2
	child.phi3 = parent1.phi3

	child.theta1 = parent2.theta1
	child.theta2 = parent2.theta2
	child.theta3 = parent2.theta3

	return child

def mutation(chromosomes):

	for chromosome in chromosomes:
		
		if random.randint(0, 100) < (100 * mutation_rate):
			chromosome.phi1 = random.randint(0, 360)
		
		if random.randint(0, 100) < (100 * mutation_rate):
			chromosome.phi2 = random.randint(0, 360)
		
		if random.randint(0, 100) < (100 * mutation_rate):
			chromosome.phi3 = random.randint(0, 360)

		if random.randint(0, 100) < (100 * mutation_rate):
			chromosome.theta1 = random.randint(0, 360)

		if random.randint(0, 100) < (100 * mutation_rate):
			chromosome.theta2 = random.randint(0, 360)

		if random.randint(0, 100) < (100 * mutation_rate):
			chromosome.theta3 = random.randint(0, 360)

	return chromosomes			

def main():

	if population <= 0 or (selection_rate <= 0 or selection_rate > 1) or (mutation_rate <= 0 or mutation_rate > 1) or generations <= 0:
		print("Invalid parameters!")
	else:	
		best_chromosome = geneticAlgorithm()		
		print('Best chromosome: ' + str(best_chromosome))

main()		