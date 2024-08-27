import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
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
    
    #print(filename)
    # Check if the item is a file (not a subdirectory) and has the target extension
    if os.path.isfile(os.path.join(folder_path, filename)) and filename.endswith(target_extension):
        
        new_df=pd.read_csv(r"/Users/aadityamoudgil/Desktop/data_collection/tournament_data/"+filename,header=None)
        new_df.columns = column_names
        
        df_tournament = pd.concat([df_tournament,new_df], ignore_index=True)
        
        


grouped = df_tournament.groupby(["Mutation Rate", "Population Size", "Number of Generations", "Valley Width", "Genome Length", "Tournament Size"])

# Calculating mean, median, and standard deviation of the 'Average Fitness Achieved' column
result = grouped["Average Fitness Achieved"].agg(['mean', 'median', 'std'])
result = result.reset_index()


X = result[['Mutation Rate', 'Population Size', 'Tournament Size']]
print (X)# Features
y = result['mean']  # Target variable

#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) #got this form Chat GPT

model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print("Mean Squared Error:", mse)

Avg_df = df_tournament.groupby(['Tournament Size', 'Mutation Rate', 'Population Size'])[
    'Average Fitness Achieved'].mean().reset_index()

pop_list = [10, 100, 1000]
mutation_list = [0.001, 0.01, 0.1]
# plotting the tournament data

fig, axes = plt.subplots(3, 3, figsize=(20, 16))

for population_size in pop_list:
    for mutation_rate in mutation_list:
        ax = axes[pop_list.index(population_size), mutation_list.index(mutation_rate)]









        # plotting average trendlines

        condition_avg = (Avg_df['Mutation Rate'] == mutation_rate) & \
                        (Avg_df['Population Size'] == population_size)

        selected_data_avg = Avg_df.loc[condition_avg, ['Tournament Size', 'Average Fitness Achieved']]
        x_val_avg = (list(selected_data_avg["Tournament Size"]))
        y_val_avg = (list(selected_data_avg["Average Fitness Achieved"]))

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
        # print(x_val_avg)
        # ax.boxplot(y_val_avg, positions=sorted_x_values_avg)

        # Adding comparison with y_pred
        X_subset = X[(X['Mutation Rate'] == mutation_rate) & (X['Population Size'] == population_size)]
        y_pred_subset = model.predict(X_subset)
        ax.plot(X_subset['Tournament Size'], y_pred_subset, marker='o', linestyle='-', color='r', label='Predicted')

        ax.set_xlabel('Tournament Size')
        ax.set_ylabel('Fitness Achieved')
        ax.set_title('Mutation Rate: {} Population Size: {}'.format(mutation_rate, population_size))
        ax.legend()  # Add legend to the plot



plt.tight_layout()
plt.show()








