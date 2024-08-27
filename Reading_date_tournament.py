import pandas as pd
import matplotlib.pyplot as plt
 


pd.options.display.max_columns = 10







file_tournament=open("data_torunament.csv",'r')
file_truncation=open("data_truncation.csv",'r')


df_tournament=pd.read_csv(file_tournament)
df_truncation=pd.read_csv(file_truncation)



#print(df_truncation)
#print(df_truncation)

pop_list=[10,100,1000]
mutation_list=[0.001,0.01,0.1]
#plotting the truncationt data

fig, axes = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax = axes[pop_list.index(population_size),mutation_list.index(mutation_rate)]
        
        
        condition = (df_tournament['Mutation Rate'] == mutation_rate) & \
                    (df_tournament['Population Size'] == population_size) & \
                    (df_tournament['Numer of Generations'] == 1000) 
                    
                    
        selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





        x_val=(list(selected_data["Tournament Size"]))
        y_val=(list(selected_data["Max Fitness Achieved"]))
        
        coordinates = list(zip(x_val, y_val))
        
        # Sort the coordinates based on x-values
        sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
        
        # Unpack the sorted coordinates into separate x and y lists
        sorted_x_values, sorted_y_values = zip(*sorted_coordinates)
        
        # Plot the graph
        ax.plot(sorted_x_values, sorted_y_values, marker='o')
        
        
        

        
        ax.set_title(str(population_size)+"  "+str(mutation_rate))
        ax.set_ylim(-1,101)
        ax.set_xscale("log")
            




plt.show()
file_tournament.close()
file_truncation.close()       