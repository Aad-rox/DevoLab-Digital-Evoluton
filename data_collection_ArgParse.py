import pickle
import csv
import random
import argparse
import numpy as np

def fitnessScore(organism_list,w=3):
    if sum(organism_list)%w==0:
        return(sum(organism_list))
    else:
       n=(sum(organism_list)%w)+1
       return(sum(organism_list)-n)





file_trunc=open("data_truncation.csv","a+")
file_torunament=open("data_torunament.csv","a+")
csv_trunc_writer=csv.writer(file_trunc)
csv_tournament_writer=csv.writer(file_torunament)



parser= argparse.ArgumentParser(description="Data collection arguments")



parser.add_argument("--mutation_rate_", type=float, default=0.01, help="Mutation rate (e.g., 0.01 for 1%)")
parser.add_argument("--population_size_", type=int, default=100, help="Number of organisms in each generation")






args = parser.parse_args()


mutation_rate=args.mutation_rate_
population_size=args.population_size_ 
number_of_generations=10
truncation_size=10
tournament_size=5
genome_length=100
valley_width=3

list_of_data=[]




max_lists=[]
avg_lists=[]








mu=mutation_rate
    
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
csv_tournament_writer.writerow(data_dict.values())
#print(list_of_data)
#print("---------------")
#print(max_lists)









file_torunament.close()
file_trunc.close()


    
    
    
    
    