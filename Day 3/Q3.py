import pandas as pd
import pdfkit

covid_data= pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-16-2020.csv')
data = covid_data.groupby(['Country/Region', 'Province/State'])['Confirmed', 'Deaths', 'Recovered'].max()
pd.set_option('display.max_rows', None)

file = open('data.html', 'w')
data_html = data.to_html()
file.write(data_html)
file.close()

pdfkit.from_file('data.html','datapdf')

