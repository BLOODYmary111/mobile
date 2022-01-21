import pandas as pd
import csv 
import plotly.figure_factory as ff

df=pd.read_csv("daata.csv")
fig = ff.create_distplot([df["Sr.No"].tolist()],["Mobile Brand"],["Avg Rating"],show_hist=False)
fig.show()