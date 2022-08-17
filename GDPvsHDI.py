from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Human development Index data

HDI = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",
    index_col=1,
    header=1
)

hdi = HDI[0]

hdi.set_index("Nation", inplace=True)
hdi.rename(
    columns = {
        '2019 data (2020 report)​[2].1':'data', 
        'Average annual growth (2010–2019)​[19]':'Average annual growth'
        }, inplace = True
    )

del hdi["2019 data (2020 report)​[2]"]


# GDP Data

GDP = pd.read_html(
    "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)",
    index_col=0,
    header=1
)

gdp = GDP[0]
gdp.rename(columns={"Estimate.2	": "Estimate", "Year.2":"year"}, inplace=True)
gdp.rename(index={"Country/Territory	":"Country"}, inplace=True)

gdp = gdp[["Estimate", "year"]]

# Scatter plot

Interesting_Countries = [
    "China", "United States", "Japan", "France", "Iran", "Germany", "Canada",
    "Russia", "Brazil", "Argentina", "Mexico", "Algeria", "Tunisia", "Egypt",
    "Guinea-Bissau", "Grenada", "Cuba", "India", "Iceland", "Central African Republic",
    "Pakistan", "Turkey", "Poland", "Bulgaria", "Serbia", "Malta", "Bahrain", "Andorra", "Luxembourg",
    "Ireland", "Mauritius", "Seychelles", "Morocco", "Niger", "Nigeria", "Nepal", "Laos",
    "Iraq", "Guatemala", "Uzbekistan", "Libya", "Comoros", "Palau", "Marshall Islands"
    "Tonga", "Dominica", "Samoa", "Saint Luca", "Eritrea", "Bhutan", "Rwanda", "Madagascar", "Armenia",
    "Angola", "Slovakia", "Mongolia"
]

H = []
G = []
countries = []

for c in gdp.index:
    if c in hdi.index:
        try:
            if float(gdp.Estimate[c]) < 1e10:
                G.append(float(gdp.Estimate[c]))
                H.append(float(hdi.data[c]))
                countries.append(c)
            else:
                continue
        except Exception:
            continue

data = pd.DataFrame(data={"GDP": G, "HDI": H}, index = countries)

plt.scatter(G, H, c="b", s=1.7)
plt.xscale("log")
plt.xlabel("GDP of country (Millions of dollars)")
plt.ylabel("Human development index of country")

for i, name in enumerate(countries):
    if name in Interesting_Countries:
        plt.text(G[i], H[i], name)

plt.show()
