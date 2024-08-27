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


def get_decimal_part(number):
    if isinstance(number, (int, float)):
        return number % 1
    else:
        raise ValueError("Input must be a float or an integer")



#file_trunc=open(r"/Users/aadityamoudgil/Desktop/data_collection/data_truncation.csv","a+")
#file_torunament=open(r"/Users/aadityamoudgil/Desktop/data_collection/data_torunament.csv","a+")
#csv_trunc_writer=csv.writer(file_trunc)
#csv_tournament_writer=csv.writer(file_torunament)



parser= argparse.ArgumentParser(description="Data collection arguments")



parser.add_argument("--mutation_rate_", type=float, default=0.01, help="Mutation rate (e.g., 0.01 for 1%)")
parser.add_argument("--population_size_", type=int, default=100, help="Number of organisms in each generation")
parser.add_argument("--tournament_size_", type=float, default=5, help="Number of organisms truncated in each generation")





#passsing all the arguements through argparse

args = parser.parse_args()

for replic in range(1,11):
    mutation_rate=args.mutation_rate_
    population_size=args.population_size_ 
    number_of_generations=1000
    truncation_size=10
    tournament_size=args.tournament_size_
    genome_length=1
    valley_width=3
    num_replicates=replic
    random.seed(num_replicates)
    
    
    if population_size>=tournament_size:
        
        #making and writing the individual file for each condition
        file_name=str(mutation_rate)+","+str(population_size)+","+str(tournament_size)+","+str(num_replicates)+".csv"
        condition_file=open(file_name,"a+")
        writer=csv.writer(condition_file)
        heading_row=["Mutation Rate","Population Size","Numer of Generations", "is_tournament","Tournament Size", "Max Fitness Achieved","Valley Wdith", "Genome Length"]
      
        
        
        
        list_of_data=[]
        
        
        
        
        max_lists=[]
        avg_lists=[]
        
        
        
        
        
        
        
        
        mu=mutation_rate
            
        y=[]
        y_max=[]
        x=[]
        mutation_counter=0
        #print("Run Started \n")
        organism = 0
        
        population=[]
        
        for i in range(population_size):
            
          #creating the original population
          population.append(organism)
        next_gen_population=[]
        next_gen_population=list(population)
        fitness_list=[]
        
        for o in next_gen_population:
         fitness_list.append(o)
        avg_fitness=sum(fitness_list)/len(fitness_list)
        max_fitness=max(fitness_list)
        
        y_max=[max_fitness]
        y=[avg_fitness]
        
        for gen in range(number_of_generations): #runs for each generation
          #print(next_gen_population)  
          
              select_population= list(next_gen_population) #selecting the population used to create offssprings
              next_gen_population=[]
              
              for i in range(population_size): #using the function to figure out the tournament size from the partial torunament size
                tournament=[]
                decimal_part=get_decimal_part(tournament_size)
                if random.random()<decimal_part:
                    tournament_size_mod=int(tournament_size)+1
                else:
                    tournament_size_mod=int(tournament_size)
                    
               #creating tournament without replacement
                tournament=random.sample(select_population, tournament_size_mod) 
                tournament=sorted(tournament, key=lambda x: fitnessScore(x,valley_width))
                #print(tournament)
                next_gen_population.append(tournament[-1]) #selecting organism with the maximum fitness from the given tournament 
                
                num_mutation=np.random.binomial(genome_length, mu)
                for _ in range(num_mutation):
                  result = random.choice([1, -1])
                 
                  next_gen_population[-1]+=result #applying muatations to the selected organism 
              #print("------------")
              #print(next_gen_population)
              fitness_list=[]
              
              for o in next_gen_population:
               fitness_list.append(o)
               
              avg_fitness=sum(fitness_list)/len(fitness_list)
              max_fitness=max(fitness_list)
              
              y_max.append(max_fitness)
              y.append(avg_fitness)
         
        max_lists.append(y_max)
        avg_lists.append(y)
        data_dict={"mutation_rate" :mu, "population_size":population_size, "number_of_generations":number_of_generations,"is_tournament":True,"torunament_size":tournament_size, "max_fitness_achieved":y_max[-1],"valley_width":valley_width,"genome_length":genome_length,"average_fitness_achieved":y[-1] }
        list_of_data.append(data_dict)
        #csv_tournament_writer.writerow(data_dict.values())
        #storing the specific values in the dictionary to be read later
           
        writer.writerow(data_dict.values())
        
                        
        #print(list_of_data)
        #print("---------------")
        #print(max_lists)
        
        
        
        
        
        
        
        
        
        condition_file.close()
    #file_torunament.close()
    #file_trunc.close()
    
    
        
        
        
        
        
