import pickle
import random
import numpy as np

def fitnessScore(organism_list,w=3):
    if sum(organism_list)%w==0:
        return(sum(organism_list))
    else:
       n=(sum(organism_list)%w)+1
       return(sum(organism_list)-n)

mutation_rate=eval(input("Enter the list of mutation rates: "))
population_size=int(input("Enter population size: "))
number_of_generations=int(input("Enter the number of generations: "))
truncation_size=int(input("Enter truncation size: "))
tournament_size=int(input("Enter the tournament size: "))
genome_length=int(input("enter the genome length: "))
valley_width=int(input("Enter Valley width for the fitness function: "))

list_of_data=[]




max_lists=[]
avg_lists=[]
for mu in mutation_rate:
    
    y=[]
    y_max=[]
    x=[]
    mutation_counter=0
    #print("Run Started \n")
    organism = [0]*genome_length
    
    population=[]
    
    for i in range(population_size):
        
      population.append(list(organism))
    next_gen_population=[]
    next_gen_population=list(population)
    fitness_list=[]
    
    for o in next_gen_population:
     fitness_list.append(sum(o))
    avg_fitness=sum(fitness_list)/len(fitness_list)
    max_fitness=max(fitness_list)
    
    y_max=[max_fitness]
    y=[avg_fitness]
    
    
    for gen in range(number_of_generations):
      #print(next_gen_population)  
      
      select_population= list(next_gen_population)
      next_gen_population=[]
      
      for i in range(population_size):
        tournament=[]  
        for t in range(tournament_size):
            random_org_position = random.randint(0, population_size-1)
            #print(random_org_position)
            tournament.append(select_population[random_org_position])
        tournament=sorted(tournament, key=lambda x: fitnessScore(x,valley_width))
        #print(tournament)
        next_gen_population.append(tournament[-1].copy())    
        num_mutation=np.random.binomial(genome_length, mu)
        for _ in range(num_mutation):
          position=random.randint(0,len(next_gen_population[-1])-1)
          if next_gen_population[-1][position]==1:
            next_gen_population[-1][position]=0
          else:
            next_gen_population[-1][position]=1
      #print("------------")
      #print(next_gen_population)
      fitness_list=[]
      
      for o in next_gen_population:
       fitness_list.append(sum(o))
       
      avg_fitness=sum(fitness_list)/len(fitness_list)
      max_fitness=max(fitness_list)
      
      y_max.append(max_fitness)
      y.append(avg_fitness)
     
    max_lists.append(y_max)
    avg_lists.append(y)
    data_dict={"mutation_rate" :mu, "population_size":population_size, "number_of_generations":number_of_generations,"is_tournament":True,"torunament_size":tournament_size, "max_fitness_achieved":y_max[-1],"valley_width":valley_width,"genome_length":genome_length, }
    list_of_data.append(data_dict)
    #print(list_of_data)
    #print("---------------")
    #print(max_lists)




for mu in mutation_rate:
    
    y=[]
    y_max=[]
    x=[]
    mutation_counter=0
    print("Run Started \n")
    organism = [0]*genome_length

    population=[]
    
    for i in range(population_size):
      population.append(organism)
    next_gen_population=[]
    next_gen_population=list(population)
    
    for gen in range(number_of_generations):
      next_gen_population = sorted(next_gen_population, key=lambda x: fitnessScore(x,valley_width))
      select_population=list(next_gen_population[-1*truncation_size:])
      next_gen_population=[]
      
      for i in range(population_size):
        next_gen_population.append(select_population[random.randint(0,len(select_population)-1)].copy())
        num_mutation=np.random.binomial(genome_length, mu)
        for _ in range(num_mutation):
          position=random.randint(0,len(next_gen_population[-1])-1)
          if next_gen_population[-1][position]==1:
            next_gen_population[-1][position]=0
          else:
            next_gen_population[-1][position]=1
      
      fitness_list=[]
      
      for o in next_gen_population:
       fitness_list.append(sum(o))
       
      avg_fitness=sum(fitness_list)/len(fitness_list)
      max_fitness=max(fitness_list)
      
      y_max.append(max_fitness)
      y.append(avg_fitness)
     
    max_lists.append(y_max)
    avg_lists.append(y)
    data_dict={"mutation_rate" :mu, "population_size":population_size, "number_of_generations":number_of_generations,"is_tournament":False,"truncation_size":truncation_size, "max_fitness_achieved":y_max[-1],"valley_width":valley_width,"genome_length":genome_length, }
    list_of_data.append(data_dict)



with open("data", 'wb') as file:
    data = list_of_data
    pickle.dump(data, file)



    
    
    
    
    