import pandas as pd
import pdfkit

#fetching the dataset
data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv', usecols=['Last Update', 'Country/Region', 'Confirmed','Deaths', 'Recovered'])
top_20 = data.groupby('Country/Region').max().sort_values(by='Confirmed', ascending=False)[:20]

#converting the above data into html
file = open('data.html', 'w')
top_20_html = top_20.to_html()
file.write(top_20_html)
file.close()

#converting the html to pdf
pdfkit.from_file('data.html','covid19_top_20_countries.pdf')
