import pandas as pd
import matplotlib.pyplot as plt



pd.options.display.max_columns = 10







file_tournament=open("data_torunament.csv",'r')
file_truncation=open("data_truncation.csv",'r')


df_tournament=pd.read_csv(file_tournament)
df_truncation=pd.read_csv(file_truncation)



#print(df_tournament)
#print(df_truncation)


#plotting the tournament data

fig, axes = plt.subplots(3, 3, figsize=(10, 8))





#plotting subplot 1

ax = axes[0, 0]
condition = (df_tournament['Mutation Rate'] == 0.001) & \
            (df_tournament['Population Size'] == 10000) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=10000, mu=0.001")



#plotting subplot 2

ax = axes[0, 1]
condition = (df_tournament['Mutation Rate'] == 0.01) & \
            (df_tournament['Population Size'] == 10000) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=10000, mu=0.01")



#plotting subplot 3

ax = axes[0, 2]
condition = (df_tournament['Mutation Rate'] == 0.1) & \
            (df_tournament['Population Size'] == 10000) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=10000, mu=0.1")



#plotting subplot 4

ax = axes[1, 0]
condition = (df_tournament['Mutation Rate'] == 0.001) & \
            (df_tournament['Population Size'] == 1000) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=1000, mu=0.001")


#plotting subplot 5

ax = axes[1, 1]
condition = (df_tournament['Mutation Rate'] == 0.01) & \
            (df_tournament['Population Size'] == 1000) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=1000, mu=0.01")



#plotting subplot 6

ax = axes[1, 2]
condition = (df_tournament['Mutation Rate'] == 0.1) & \
            (df_tournament['Population Size'] == 1000) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=1000, mu=0.1")




#plotting subplot 7

ax = axes[2, 0]
condition = (df_tournament['Mutation Rate'] == 0.001) & \
            (df_tournament['Population Size'] == 100) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=100, mu=0.001")



#plotting subplot 8 

ax = axes[2, 1]
condition = (df_tournament['Mutation Rate'] == 0.01) & \
            (df_tournament['Population Size'] == 100) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=100, mu=0.01")


#plotting subplot 9

ax = axes[2, 2]
condition = (df_tournament['Mutation Rate'] == 0.1) & \
            (df_tournament['Population Size'] == 100) & \
            (df_tournament['Numer of Generations'] == 1000) 
            
            
selected_data = df_tournament.loc[condition, ['Tournament Size', 'Max Fitness Achieved']]





x_val=(list(selected_data["Tournament Size"]))
y_val=(list(selected_data["Max Fitness Achieved"]))

ax.plot(x_val,y_val)
ax.set_title("pop=100, mu=0.1")


plt.show()


