
import csv





file_trunc=open("data_truncation.csv","w+")
file_tournament=open("data_torunament.csv","w+")



heading_row=["Mutation Rate","Population Size","Numer of Generations", "is_tournament","Tournament Size", "Max Fitness Achieved","Valley Wdith", "Genome Length"]

csv_trunc=csv.writer(file_trunc)
csv_tournament=csv.writer(file_tournament)


csv_trunc.writerow(heading_row)
csv_tournament.writerow(heading_row)


file_trunc.close()
file_tournament.close()