import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('cost_revenue_clean.csv')
#print(data.head())
#print(data.describe())

X = DataFrame(data, columns=['production_budget_usd'])
y = DataFrame(data, columns=['worldwide_gross_usd'])

regression = LinearRegression()
regression.fit(X, y)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

regression.coef_
regression.intercept_

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.3)
plt.plot(X, regression.predict(X), color = 'red', linewidth=4)
plt.title('Film Cost Vs Global Revennue')
plt.xlabel('Production Budget K')
plt.ylabel('Worldwide Revenue K')
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()