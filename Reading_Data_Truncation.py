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
        
        
        condition = (df_truncation['Mutation Rate'] == mutation_rate) & \
                    (df_truncation['Population Size'] == population_size) & \
                    (df_truncation['Numer of Generations'] == 1000) 
                    
                    
        selected_data = df_truncation.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





        x_val=(list(selected_data["Tournament Size"]))
        y_val=(list(selected_data["Max Fitness Achieved"]))

        ax.plot(x_val,y_val)
        ax.set_title(str(population_size)+"  "+str(mutation_rate))
        ax.set_ylim(-1,101)
            




plt.show()
file_tournament.close()
file_truncation.close()       