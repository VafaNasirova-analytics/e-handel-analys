import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

dat = pd.read_csv("data/ecommerce_sales.csv")
print(dat.head())

aov_by_category = dat.groupby("category")["revenue"].mean().round(2)
aov_total = dat["revenue"].mean().round(2)
aov_sd = dat["revenue"].std().round(2)

print(aov_by_category)
print(aov_total)
print(aov_sd)

plt.hist(dat["revenue"], bins=70, color='steelblue', edgecolor='white')
plt.title("Distribution of Order Values")
plt.xlabel("Order Value (kr)")
plt.ylabel("Frequency")
plt.axvline(aov_total, color='black', linestyle='dashed', linewidth=2, label=f'AOV: {aov_total}kr')
plt.axvline(dat["revenue"].quantile(0.25), color='darkred', linestyle='dashed', linewidth=2, label=f'25th Percentile: {dat["revenue"].quantile(0.25)}kr')
plt.axvline(dat["revenue"].quantile(0.75), color='darkgreen', linestyle='dashed', linewidth=2, label=f'75th Percentile: {dat["revenue"].quantile(0.75)}kr')
plt.legend()
plt.show()

dat.groupby("category")["revenue"].mean().plot(kind='bar', color='steelblue')
plt.title("Average Order Value by Category")
plt.xlabel("Category")
plt.ylabel("Average Order Value (kr)")
plt.show()

#sns.kdeplot(dat["revenue"], color='steelblue', fill=True)
#plt.show()

#dat["revenue"].plot(kind='hist', bins=70, color='steelblue')
#plt.show()