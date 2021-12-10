import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandasgui



population_by_ctr = pd.DataFrame(pd.read_csv("population_by_country_2019_2020.csv", index_col=0))
# pandasgui.show(population_by_ctr, settings={'block': True})

Net_population_change = abs(population_by_ctr.iloc[:,0] - population_by_ctr.iloc[:,1])
Population_change = (Net_population_change/population_by_ctr.iloc[:,0])*100
population_by_ctr["Net population change"] = Net_population_change
population_by_ctr["Population change [%]"] = Population_change

population_by_ctr.sort_values("Population change [%]", axis=0, inplace=True, ascending=False)  # sortowanie wzdłuż osi 0 (po wierszach), w miejscu, malejąco

# most_10_change = population_by_ctr.iloc[0:10,0:2]
# most_10_change.plot(kind='bar')
# plt.show()
# print(most_10_change)

population_by_ctr["Density (2020)"] = "Low"
population_by_ctr.loc[population_by_ctr.iloc[:,0]/population_by_ctr.iloc[:,2] > 500,"Density (2020)"] = "High"
population_output = population_by_ctr.iloc[0::2, :]

population_output.to_csv("population_output.csv")
# pandasgui.show(population_output, settings={'block': True})

