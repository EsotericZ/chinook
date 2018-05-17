from country import results
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

res_t = results[:(len(results)-1)]
# print(res_t)

ax = res_t[['Avg Value/Sale']].plot(kind='bar', title='NAME', figsize=(5,5))
ax.set_xlabel('Country')
ax.set_ylabel('Average Value Per Sale')
ax.set_xticklabels(res_t.Country)
plt.show()

# RESULTS
# In the Czech Republic, the average value per sale is much higher than anywhere else in the world
# This is a country with very few customers, looking into expansion could be benificial
