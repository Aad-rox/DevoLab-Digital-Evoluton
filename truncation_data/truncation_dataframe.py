import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns = 10

#gathering the truncation data in a data base
column_names = ["Mutation Rate", "Population Size", "Number of Generations", "is_tournament", "Truncation Size", "Max Fitness Achieved", "Valley Width", "Genome Length", "Average Fitness Achieved"]
df_truncation = pd.DataFrame(columns=column_names)


folder_path = r"/Users/aadityamoudgil/Desktop/data_collection/truncation_data"
target_extension = '.csv'





# Iterate through all files with the target extension in the folder
for filename in os.listdir(folder_path):
   
    #print(filename)
    # Check if the item is a file (not a subdirectory) and has the target extension
    if os.path.isfile(os.path.join(folder_path, filename)) and filename.endswith(target_extension):
        
        new_df=pd.read_csv(r"/Users/aadityamoudgil/Desktop/data_collection/truncation_data/"+filename,header=None)
        new_df.columns = column_names
        
        df_truncation = pd.concat([df_truncation,new_df], ignore_index=True)




truncation_size_list = df_truncation['Truncation Size'].tolist()

# Group by the specified columns and calculate the mean for 'Max Fitness Achieved'



Max_df = df_truncation.groupby(['Truncation Size', 'Mutation Rate', 'Population Size'])['Max Fitness Achieved'].mean().reset_index()
Avg_df = df_truncation.groupby(['Truncation Size', 'Mutation Rate', 'Population Size'])['Average Fitness Achieved'].mean().reset_index()

max_rep_list=list(df_truncation.groupby(['Truncation Size', 'Mutation Rate', 'Population Size'])['Max Fitness Achieved'])
#print(list(df_truncation[df_truncation["Mutation Rate"]==0.001]["Average Fitness Achieved"]))
#print(max_rep_list[0])
#print(Average_df)


pop_list=[10,100,1000]
mutation_list=[0.001,0.01,0.1]
#plotting the truncationt data

fig, axes = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax = axes[pop_list.index(population_size),mutation_list.index(mutation_rate)]
        
        
        condition = (Max_df['Mutation Rate'] == mutation_rate) & \
                    (Max_df['Population Size'] == population_size) 
                    
                    
        selected_data = Max_df.loc[condition, ['Truncation Size', 'Max Fitness Achieved']]





        x_val=(list(selected_data["Truncation Size"]))
        y_val=(list(selected_data["Max Fitness Achieved"]))
        
        ax.set_xlabel('Truncation Size')
        ax.set_ylabel('Max Fitness Achieved')
        ax.set_title('Max ' + str(mutation_rate) + " " + str(population_size))

        # Plot the max boxplot
        ax.boxplot(y_val)
        
        
        coordinates = list(zip(x_val, y_val))
        
        
        # Sort the coordinates based on x-values
        sorted_coordinates = sorted(coordinates, key=lambda x: x[0])
        
        # Unpack the sorted coordinates into separate x and y lists
        sorted_x_values, sorted_y_values = zip(*sorted_coordinates)
        
        # Plot the graph
        ax.plot(sorted_x_values, sorted_y_values, marker='o')
        
        
        #plotting average trendlines
        
        
        condition_avg = (Avg_df['Mutation Rate'] == mutation_rate) & \
                    (Avg_df['Population Size'] == population_size) 
        
        
        selected_data_avg = Avg_df.loc[condition_avg, ['Truncation Size', 'Average Fitness Achieved']]
        x_val_avg=(list(selected_data_avg["Truncation Size"]))
        y_val_avg=(list(selected_data_avg["Average Fitness Achieved"]))
        
        ax.set_xlabel('Truncation Size')
        ax.set_ylabel('Average Fitness Achieved')
        ax.set_title('Average ' + str(mutation_rate) + " " + str(population_size))

        # Plot the average boxplot
        ax.boxplot(y_val_avg)
        
        coordinates_avg = list(zip(x_val_avg, y_val_avg))
        sorted_coordinates_avg = sorted(coordinates_avg, key=lambda x: x[0])
        
        sorted_x_values_avg, sorted_y_values_avg = zip(*sorted_coordinates_avg)
        
      
        
        ax.plot(sorted_x_values_avg, sorted_y_values_avg, marker='x')

        
        ax.set_title(str(population_size)+"  "+str(mutation_rate))
    
        ax.set_xlabel("truncation size")
        ax.set_ylabel("fitness achieved")
            
plt.savefig('truncation_figure.png')


# Create box plots for Average Fitness Achieved Used ChatGPT for this
fig_box, axes_box = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax_box_avg = axes_box[pop_list.index(population_size), mutation_list.index(mutation_rate)]
        boxplot_list=[]
        
        
        for T_size in set(truncation_size_list):
            
            filtered_rows = df_truncation[(df_truncation['Population Size'] == population_size) &
                              (df_truncation['Mutation Rate'] == mutation_rate) &
                              (df_truncation['Truncation Size'] == T_size)]

            
            boxplot_list.append(filtered_rows['Average Fitness Achieved'].tolist())
            
        ax_box_avg.boxplot(boxplot_list)

        ax_box_avg.set_xlabel('Truncation Size')
        ax_box_avg.set_ylabel('Max Fitness Achieved')
        ax_box_avg.set_title(f'Box Plot - Max {mutation_rate} {population_size}')
            

        
      
       



# Create box plots for Max Fitness Achieved
fig_box_max, axes_box_max = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax_box_max = axes_box_max[pop_list.index(population_size), mutation_list.index(mutation_rate)]

        boxplot_list=[]
        
        
        for T_size in set(truncation_size_list):
            
            filtered_rows = df_truncation[(df_truncation['Population Size'] == population_size) &
                              (df_truncation['Mutation Rate'] == mutation_rate) &
                              (df_truncation['Truncation Size'] == T_size)]

            
            boxplot_list.append(filtered_rows['Max Fitness Achieved'].tolist())
       # print(boxplot_list)    
        ax_box_max.boxplot(boxplot_list)

        
        ax_box_max.set_xlabel('Truncation Size')
        ax_box_max.set_ylabel('Max Fitness Achieved')
        ax_box_max.set_title(f'Box Plot - Max {mutation_rate} {population_size}')

plt.savefig('max_fitness_boxplot.png')

plt.show()







plt.show()



       

       