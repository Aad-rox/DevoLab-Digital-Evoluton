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
        
        
        
        


grouped = df_truncation.groupby(["Mutation Rate", "Population Size", "Number of Generations", "Valley Width", "Genome Length", "Truncation Size"])

# Calculating mean, median, and standard deviation of the 'Average Fitness Achieved' column
result = grouped["Average Fitness Achieved"].agg(['mean', 'median', 'std'])
count = grouped.size()
result['std_error'] = result['std'] / (count ** 0.5)

excel_file_path = "aggregated_truncation_data.xlsx"

# Write the DataFrame to an Excel file
result.to_excel(excel_file_path)

print("Data has been successfully saved to", excel_file_path)