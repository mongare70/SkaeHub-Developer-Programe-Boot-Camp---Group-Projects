import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')

df = df[['Last Update', 'Country/Region', 'Confirmed', 'Deaths', 'Recovered']].head(20)

print(df)