import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns = 10

#gathering the tournament data in a data base
column_names = ["Mutation Rate", "Population Size", "Number of Generations", "is_tournament", "Tournament Size", "Max Fitness Achieved", "Valley Width", "Genome Length", "Average Fitness Achieved"]
df_tournament = pd.DataFrame(columns=column_names)


folder_path = r"/Users/aadityamoudgil/Desktop/data_collection/tournament_data"
target_extension = '.csv'




# Iterate through all files with the target extension in the folder
for filename in os.listdir(folder_path):
  
    # Check if the item is a file (not a subdirectory) and has the target extension
    if os.path.isfile(os.path.join(folder_path, filename)) and filename.endswith(target_extension):
        file_path = os.path.join(folder_path, filename)
            
        if os.path.getsize(file_path) == 0:
               print(f"Skipping empty file: {filename}")
               continue
        
        new_df=pd.read_csv(r"/Users/aadityamoudgil/Desktop/data_collection/tournament_data/"+filename,header=None)
        new_df.columns = column_names
        
        df_tournament = pd.concat([df_tournament,new_df], ignore_index=True)



tournament_size_list = df_tournament['Tournament Size'].tolist()


# Group by the specified columns and calculate the mean for 'Max Fitness Achieved'



Max_df = df_tournament.groupby(['Tournament Size', 'Mutation Rate', 'Population Size'])['Max Fitness Achieved'].mean().reset_index()
Avg_df = df_tournament.groupby(['Tournament Size', 'Mutation Rate', 'Population Size'])['Average Fitness Achieved'].mean().reset_index()


pop_list=[10,100,1000]
mutation_list=[0.001,0.01,0.1]
#plotting the tournament data

fig, axes = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax = axes[pop_list.index(population_size),mutation_list.index(mutation_rate)]
        
        
        condition_max = (Max_df['Mutation Rate'] == mutation_rate) & \
                    (Max_df['Population Size'] == population_size) 
                    
                    
        selected_data_max = Max_df.loc[condition_max, ['Tournament Size', 'Max Fitness Achieved']]
    



        


        x_val_max=(list(selected_data_max["Tournament Size"]))
        y_val_max=(list(selected_data_max["Max Fitness Achieved"]))
        
        ax.set_xlabel('Torunament Size')
        ax.set_ylabel('Max Fitness Achieved')
        ax.set_title('Max ' + str(mutation_rate) + " " + str(population_size))

       
        
        
        
        
        
        
        coordinates_max = list(zip(x_val_max, y_val_max))
        
        # Sort the coordinates based on x-values
        sorted_coordinates_max = sorted(coordinates_max, key=lambda x: x[0])
        
        # Unpack the sorted coordinates into separate x and y lists
        sorted_x_values_max, sorted_y_values_max = zip(*sorted_coordinates_max)
        
        # Plot the graph
        ax.plot(sorted_x_values_max, sorted_y_values_max, marker='o')
        
        #plotting average trendlines
        
        
        condition_avg = (Avg_df['Mutation Rate'] == mutation_rate) & \
                    (Avg_df['Population Size'] == population_size) 
        
        
        selected_data_avg = Avg_df.loc[condition_avg, ['Tournament Size', 'Average Fitness Achieved']]
        x_val_avg=(list(selected_data_avg["Tournament Size"]))
        y_val_avg=(list(selected_data_avg["Average Fitness Achieved"]))
        
        
        ax.set_xlabel('Tournament Size')
        ax.set_ylabel('Average Fitness Achieved')
        ax.set_title('Average ' + str(mutation_rate) + " " + str(population_size))


         # Plot the max boxplot
        # ax.boxplot(y_val_max)

        # Plot the average boxplot
        
   
        
        
        
        
        
        coordinates_avg = list(zip(x_val_avg, y_val_avg))
        sorted_coordinates_avg = sorted(coordinates_avg, key=lambda x: x[0])
        
        sorted_x_values_avg, sorted_y_values_avg = zip(*sorted_coordinates_avg)
        
        ax.plot(sorted_x_values_avg, sorted_y_values_avg, marker='x')
        #print(x_val_avg)
        #ax.boxplot(y_val_avg, positions=sorted_x_values_avg)

        
        ax.set_title(str(population_size)+"  "+str(mutation_rate))
       
   
        ax.set_xlabel("tournament size")
        ax.set_ylabel("fitness achieved")
            
plt.savefig('tournament_figure.png')





# Create box plots for Average Fitness Achieved Used ChatGPT for this
fig_box, axes_box = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax_box_avg = axes_box[pop_list.index(population_size), mutation_list.index(mutation_rate)]
        boxplot_list=[]
        
        
        for T_size in set(tournament_size_list):
            
            filtered_rows = df_tournament[(df_tournament['Population Size'] == population_size) &
                              (df_tournament['Mutation Rate'] == mutation_rate) &
                              (df_tournament['Tournament Size'] == T_size)]

            
            boxplot_list.append(filtered_rows['Average Fitness Achieved'].tolist())
            
        ax_box_avg.boxplot(boxplot_list)

        ax_box_avg.set_xlabel('Tournament Size')
        ax_box_avg.set_ylabel('Max Fitness Achieved')
        ax_box_avg.set_title(f'Box Plot - Max {mutation_rate} {population_size}')
            

        
      
       



# Create box plots for Max Fitness Achieved
fig_box_max, axes_box_max = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax_box_max = axes_box_max[pop_list.index(population_size), mutation_list.index(mutation_rate)]

        boxplot_list=[]
        
        
        for T_size in set(tournament_size_list):
            
            filtered_rows = df_tournament[(df_tournament['Population Size'] == population_size) &
                              (df_tournament['Mutation Rate'] == mutation_rate) &
                              (df_tournament['Tournament Size'] == T_size)]

            
            boxplot_list.append(filtered_rows['Max Fitness Achieved'].tolist())
        #print(boxplot_list)    
        ax_box_max.boxplot(boxplot_list)

        
        ax_box_max.set_xlabel('Tournament Size')
        ax_box_max.set_ylabel('Max Fitness Achieved')
        ax_box_max.set_title(f'Box Plot - Max {mutation_rate} {population_size}')

plt.savefig('max_fitness_boxplot.png')
plt.show()







plt.show()



       