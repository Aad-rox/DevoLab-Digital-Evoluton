import os
import csv
import pandas as pd


#gathering the tournament data in a data base
column_names = ["Mutation Rate", "Population Size", "Number of Generations", "is_tournament", "Tournament Size", "Max Fitness Achieved", "Valley Width", "Genome Length"]
df_tournament = pd.DataFrame(columns=column_names)


folder_path = r"/Users/aadityamoudgil/Documents/data_collection/tournament_data"
target_extension = '.csv'





# Iterate through all files with the target extension in the folder
for filename in os.listdir(folder_path):
    # Check if the item is a file (not a subdirectory) and has the target extension
    if os.path.isfile(os.path.join(folder_path, filename)) and filename.endswith(target_extension):
        
        new_df=pd.read_csv(filename)
        df_tournament.append(new_df)


print(df_tournament)

