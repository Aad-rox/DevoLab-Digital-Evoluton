import pickle
import csv
import random
import argparse
import numpy as np

def fitnessScore(organism_,w=3):
    if organism_%w==0: 
        return(organism_)
    else:
       n=(organism_%w)+1
       return(organism_-n)





#file_trunc=open(r"/Users/aadityamoudgil/Desktop/data_collection/data_truncation.csv","a+")
#file_torunament=open(r"/Users/aadityamoudgil/Desktop/data_collection/data_torunament.csv","a+")
#csv_trunc_writer=csv.writer(file_trunc)
#csv_tournament_writer=csv.writer(file_torunament)



parser= argparse.ArgumentParser(description="Data collection arguments")



parser.add_argument("--mutation_rate_", type=float, default=0.01, help="Mutation rate (e.g., 0.01 for 1%)")
parser.add_argument("--population_size_", type=int, default=100, help="Number of organisms in each generation")
parser.add_argument("--truncation_rate_", type=int, default=10, help="Number of organisms truncated in each generation")



#getting all the arguments through argparse



args = parser.parse_args()
for replic in range(1,11):

    mutation_rate=args.mutation_rate_
    population_size=args.population_size_ 
    number_of_generations=1000
    truncation_size=args.truncation_rate_
    tournament_size=5
    genome_length=1
    valley_width=3
    num_replicates=replic
    random.seed(num_replicates)
    
    if (truncation_size<=population_size):
    
    
        #making and writing the individual file for each of the conditions
        file_name=str(mutation_rate)+","+str(population_size)+","+str(truncation_size)+","+str(num_replicates)+".csv"
        condition_file=open(file_name,"a+")
        writer=csv.writer(condition_file)
        heading_row=["Mutation Rate","Population Size","Numer of Generations", "is_tournament","Truncation Size", "Max Fitness Achieved","Valley Wdith", "Genome Length"]
        
        
        list_of_data=[]
        
        
        
        
        max_lists=[]
        avg_lists=[]
        
        
        
        
        
        
        
        
        mu=mutation_rate
            
        
        
        
        
        
        
        
        #run for truncation selection
            
        y=[]
        y_max=[]
        x=[]
        mutation_counter=0
        print("Run Started \n")
        organism = 0
        
        population=[]
        
        for i in range(population_size): #creating the first population
          population.append(organism)
        next_gen_population=[]
        next_gen_population=list(population)
        
        
        
        
        for gen in range(number_of_generations): #runs for the number of generations
          next_gen_population = sorted(next_gen_population, key=lambda x: fitnessScore(x,valley_width))
          select_population=list(next_gen_population[-1*truncation_size:]) #truncating the population
          next_gen_population=[]
          
          for i in range(population_size):
            next_gen_population.append(select_population[random.randint(0,len(select_population)-1)])
            num_mutation=np.random.binomial(genome_length, mu)
            for _ in range(num_mutation):
              result = random.choice([1, -1])
             
              next_gen_population[-1]+=result #mutating the selected  organisms 
              
          
          fitness_list=[]
          
          for o in next_gen_population:
           fitness_list.append(o)
           
          avg_fitness=sum(fitness_list)/len(fitness_list)
          max_fitness=max(fitness_list)
          
          y_max.append(max_fitness)
          y.append(avg_fitness)
         
        max_lists.append(y_max)
        avg_lists.append(y)
        data_dict={"mutation_rate" :mu, "population_size":population_size, "number_of_generations":number_of_generations,"is_tournament":False,"truncation_size":truncation_size, "max_fitness_achieved":y_max[-1],"valley_width":valley_width,"genome_length":genome_length,"average_fitness_achieved":y[-1] }
        list_of_data.append(data_dict)
        #csv_trunc_writer.writerow(data_dict.values())
        writer.writerow(data_dict.values()) #storing the given values in csv value that can be read later 
        
        
        #file_torunament.close()
        #file_trunc.close()
        
        condition_file.close()
        
    
    
