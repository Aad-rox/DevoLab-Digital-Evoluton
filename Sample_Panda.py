

import pandas as pd

my_str="Pop,mu,result\n"
my_str+="100,0.1,50\n"
my_str+="200,0.1,59\n"
my_str+="300,0.2,70\n"
my_str+="1000,0.1,90\n"


file=open("data_test.csv","w")

file.write(my_str)
file.close()

df=pd.read_csv("data_test.csv")
print(df)
print(list(df[df["mu"]==0.1]["result"]))