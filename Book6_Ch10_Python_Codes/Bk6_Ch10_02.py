

###############
# Authored by Weisheng Jiang
# Book 6  |  From Basic Arithmetic to Machine Learning
# Published and copyrighted by Tsinghua University Press
# Beijing, China, 2022
###############


# single variate regression

# initializations and download results 
import pandas as pd
import pandas_datareader as web
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pandas_datareader as web
import statsmodels.api as sm


y_levels_df = web.get_data_yahoo(['AAPL'], start = '2020-01-01', end = '2020-12-31')

y_levels_df.round(2).head()
y_df = y_levels_df['Adj Close'].pct_change()
y_df = y_df.dropna()


x_levels_df = web.get_data_yahoo(['^GSPC'], start = '2020-01-01', end = '2020-12-31')

x_levels_df.round(2).head()
x_df = x_levels_df['Adj Close'].pct_change()
x_df = x_df.dropna()

x_df = x_df.rename(columns={"^GSPC": "SP500"})

#%% OLS Regression

# add a column of ones
X_df = sm.add_constant(x_df)

model = sm.OLS(y_df, X_df)
results = model.fit()
print(results.summary())

#%% Obtain the ANOVA table 

from statsmodels.formula.api import ols

data = pd.DataFrame({'x': x_df['SP500'], 'y': y_df['AAPL']})

# Fit the model
model_V2 = ols("y ~ x", data).fit()

from statsmodels.stats.anova import anova_lm
anova_results = anova_lm(model_V2, typ=1)

print(anova_results)

#%% Analysis of Variance

y_mean = y_df.mean()

# Sum of Squares for Total, SST
SST = ((y_df - y_mean)**2).sum()
n = len(y_df)
# degree of freedom total, DFT
DFT = n - 1
# mean square total, MST
MST = SST/DFT

# predicted
y_hat = results.fittedvalues

y_hat = y_hat.to_frame()
y_hat = y_hat.rename(columns={0: 'AAPL'})
 
# Sum of Squares for Regression, SSR
SSR = ((y_hat - y_mean)**2).sum()
# degrees of freedom for regression model
DFR = 1
# MSR: mean square regression
MSR = SSR/DFR

# Sum of Squares for Error, SSE
SSE = ((y_df - y_hat)**2).sum()
# degrees of freedom for error, DFE
DFE = n - DFR - 1
# mean squared error, MSE
MSE = SSE/DFE


#%% Goodness of fit

# coefficient of determination, R squared

R2 = SSR/SST

R2_adj = 1 - MSE/MST

#%% F-test

F_test = MSR/MSE

N = results.nobs
k = results.df_model+1
dfm, dfe = k-1, N - k
F = results.mse_model / results.mse_resid
import scipy.stats as stats
p = 1.0 - stats.f.cdf(F,dfm,dfe)


alpha = 0.01
# F = 549.7
# n = 252
# D = 1
# p = D + 1

fdistribution = stats.f(p - 1, n - p) 
# build an F-distribution object
f_critical = fdistribution.ppf(1 - alpha)

p_value = 1 - stats.f.cdf(F, p - 1, n - p)

#%% visualization
x_points = x_df.values.T
y_points = y_df.values.T
y_hat_points = y_hat.values.T

p = model.fit().params

# generate x-values for  regression line
x = np.linspace(x_df.min(),x_df.max(),10)

fig, ax = plt.subplots()
plt.plot(x_points,y_points,'.'); 
plt.plot(x_points,y_hat_points,'+k'); 

plt.plot(x, p.const + p.SP500 * x,color = 'r')
plt.plot(np.vstack((x_points,x_points)),
     np.vstack((y_points,y_hat_points)),
     color = [0.7,0.7,0.7]);

plt.axis('scaled')
plt.ylabel('y')
plt.xlabel('x')
plt.xlim([-0.15,0.15])
plt.ylim([-0.15,0.15])
