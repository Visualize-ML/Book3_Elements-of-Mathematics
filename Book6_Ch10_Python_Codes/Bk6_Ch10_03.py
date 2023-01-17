

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

#%% linear regression with confidence interval, calculated

# add a column of ones
X_df = sm.add_constant(x_df)

model = sm.OLS(y_df, X_df)
results = model.fit()
print(results.summary())

p = model.fit().params

x_mean = x_df.mean().values
y_mean = y_df.mean().values

n = len(y_df)

# predicted
y_hat = results.fittedvalues

y_hat = y_hat.to_frame()
y_hat = y_hat.rename(columns={0: 'AAPL'})

DFR = 1

# Sum of Squares for Error, SSE
SSE = ((y_df - y_hat)**2).sum()
# degrees of freedom for error, DFE
DFE = n - DFR - 1
# mean squared error, MSE
MSE = SSE/DFE
MSE = MSE.values

#%% t-test

b1 = p.SP500
b0 = p.const

SSD_x = np.sum((x_df.values - x_mean)**2)
SE_b1 = np.sqrt(MSE/SSD_x)

SE_b0 = np.sqrt(MSE*(1/n + x_mean**2/SSD_x))

T_b1 = (b1 - 0)/SE_b1
T_b0 = (b0 - 0)/SE_b0

#%%

from scipy import stats

pval_b1 = stats.t.sf(np.abs(T_b1), n-2)*2
pval_b0 = stats.t.sf(np.abs(T_b0), n-2)*2

alpha = 0.05
t_95 = stats.t.ppf(1 - alpha/2, DFE) 

#%% confidence intervals of coefficients

b1_upper_95 = b1 + t_95*SE_b1
b1_lower_95 = b1 - t_95*SE_b1

b0_upper_95 = b0 + t_95*SE_b0
b0_lower_95 = b0 - t_95*SE_b0

#%% Visualizations

# generate x-values for regression line
x_i = np.linspace(-0.15,0.15,50)

# predicted values
y_i = b0 + b1* x_i

# confidence band
fig, ax = plt.subplots()
plt.plot(x_df,y_df,'.'); 

plt.plot(x_i, y_i,color = 'r')

# plot confidence interval
alpha = 0.05
t_95 = stats.t.ppf(1 - alpha/2, DFE) 

CI_95 = t_95 * np.sqrt(MSE) * np.sqrt(1/n + (x_i - x_mean)**2 / np.sum((x_df.values - x_mean)**2))

CI_upper = y_i + CI_95
CI_lower = y_i - CI_95
ax.fill_between(x_i,CI_lower, CI_upper, color = 'b', alpha = 0.5)

alpha = 0.01
t_99 = stats.t.ppf(1 - alpha/2, DFE) 

CI_99 = t_99 * np.sqrt(MSE) * np.sqrt(1/n + (x_i - x_mean)**2 / np.sum((x_df.values - x_mean)**2))

CI_upper = y_i + CI_99
CI_lower = y_i - CI_99
ax.fill_between(x_i,CI_lower, CI_upper, color = 'b', alpha = 0.25)

plt.axis('scaled')
plt.ylabel('y')
plt.xlabel('x')
plt.xlim([-0.15,0.15])
plt.ylim([-0.15,0.15])

# linear regression with confidence interval, Seaborn

# sns.regplot(x_df,y_df,ci=95)

#%% plot predicting interval

fig, ax = plt.subplots()
plt.plot(x_df,y_df,'.'); 

plt.plot(x_i, y_i,color = 'r')

alpha = 0.05
t_95 = stats.t.ppf(1 - alpha/2, DFE) 

pi_95 = t_95 * np.sqrt(MSE) * np.sqrt(1 + 1/n + (x_i - x_mean)**2 / np.sum((x_df.values - x_mean)**2))

pi_upper = y_i + pi_95
pi_lower = y_i - pi_95
ax.fill_between(x_i,pi_lower, pi_upper, color = 'b', alpha = 0.5)

alpha = 0.01
t_99 = stats.t.ppf(1 - alpha/2, DFE) 

pi_99 = t_99 * np.sqrt(MSE) * np.sqrt(1 + 1/n + (x_i - x_mean)**2 / np.sum((x_df.values - x_mean)**2))

pi_upper = y_i + pi_99
pi_lower = y_i - pi_99
ax.fill_between(x_i,pi_lower, pi_upper, color = 'b', alpha = 0.25)

plt.axis('scaled')
plt.ylabel('y')
plt.xlabel('x')
plt.xlim([-0.15,0.15])
plt.ylim([-0.15,0.15])

#%% Log-Likelihood Function

# SSE = SSE.values
s2 = SSE / n

# maximum likelihood estimator of error variance
# Log Likelihood function
log_L = n*(-np.log(np.sqrt(s2*2*np.pi))) - n/2

#%%

AIC = 2*(DFR + 1) - 2*log_L
BIC = (DFR + 1)*np.log(n) - 2*log_L

#%% Residual analysis
e_df = y_df - y_hat;

# confidence band
fig, ax = plt.subplots()
plt.plot(x_df,e_df,'.'); 
plt.axhline(y=0, color='r', linestyle='--')
plt.axis('scaled')
plt.ylabel('y')
plt.xlabel('x')
plt.xlim([-0.15,0.15])
plt.ylim([-0.15,0.15])

# skewness
S = np.mean(e_df**3)/np.mean(e_df**2)**(3/2)
S_2 = stats.skew(e_df,bias = True)

# kurtosis
K = np.mean(e_df**4)/np.mean(e_df**2)**(4/2)
K_2 = stats.kurtosis(e_df,fisher=False,bias = True)

# Omnibus test for normality
(Omnibus_test, p) = stats.normaltest(e_df)
fig, ax = plt.subplots()
sns.distplot(e_df)

#%% Jarque-Bera test

JB = (n/6.0) * ( S**2.0 + (1.0/4.0)*( K - 3.0 )**2.0 )
p_JB = 1.0 - stats.chi2(2).cdf(JB)

#%% Autocorrelation 

from matplotlib import pyplot
from statsmodels.graphics.tsaplots import plot_acf

# Durbin-Watson test
DW = np.sum(np.diff(e_df['AAPL'].values)**2)/SSE

plot_acf(e_df, lags=20)
pyplot.show()

#%% Condition number, multicollinearity

X = np.matrix(X_df)
eigen_values, V = np.linalg.eig(X.T * X)
print(eigen_values)

condition_number = np.sqrt(eigen_values.max()/eigen_values.min())

# if the condition number > 30, multicollinearity might exist
