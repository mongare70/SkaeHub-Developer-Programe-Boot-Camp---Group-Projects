import pandas as pd
import matplotlib.pyplot as plt
import pdfkit

df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-17-2020.csv')

#filter total deaths greater than 200 and group sum of Deaths, confirmed and recovered by country
df2 = df[df['Deaths'] > 200].groupby(['Country/Region'])[['Deaths','Confirmed','Recovered']].sum()

#generate html file from df2
file = open('data2.html', 'w')
df2_html = df2.to_html()
file.write(df2_html)
file.close()

#generate pdf file from html file
pdfkit.from_file('data2.html','df2pdf')

#plot of lines of df2
df2.plot()
plt.show()
