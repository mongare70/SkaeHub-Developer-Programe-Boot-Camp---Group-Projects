import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')

df2 = df[df['Deaths'] > 200].groupby(['Country/Region'])[['Deaths','Confirmed','Recovered']].sum()

df2.plot()

plt.show()