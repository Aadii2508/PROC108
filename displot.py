import pandas as pd
import csv
import plotly_express as px
import plotly.figure_factory as ff

file= pd.read_csv("data.csv")
rateList= file["Avg Rating"].to_list()

figure= ff.create_distplot([rateList], ["Average ratings"])
figure.show()