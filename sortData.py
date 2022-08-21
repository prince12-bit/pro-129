import pandas as pd 

file = pd.read_csv("Project 129/dwarfStars.csv")

file = file.dropna()

file["Radius"] = 0.102763 *  file["Radius"]

file['Mass'] = file['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

file['Mass'] = 0.000954588 * file['Mass']

file.to_csv("Project 129/sortedData.csv")






