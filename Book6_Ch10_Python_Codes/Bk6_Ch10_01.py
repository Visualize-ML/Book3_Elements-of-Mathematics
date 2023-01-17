

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
# from datetime import datetime
# startdate = datetime(2022,12,1)
# enddate = datetime(2022,12,15)
x_levels_df = web.get_data_yahoo(['^GSPC'], start = '2020-01-01', end = '2020-12-31')

x_levels_df.round(2).head()
x_df = x_levels_df['Adj Close'].pct_change()
x_df = x_df.dropna()

x_df = x_df.rename(columns={"^GSPC": "SP500"})

y_x_df = pd.concat([y_df, x_df], axis=1, join="inner")

#%% Data analysis

sns.jointplot(data=y_x_df, x="SP500", y="AAPL", kind = 'scatter',
              xlim = [-0.15,0.15],ylim = [-0.15,0.15])


# marginal and joint KDE plots
sns.jointplot(data=y_x_df, x="SP500", y="AAPL",
              kind="kde", cmap = 'Blues', fill = True,
              xlim = [-0.15,0.15],ylim = [-0.15,0.15])

#%% covariance matrix

SIGMA = y_x_df.cov()

fig, axs = plt.subplots()

h = sns.heatmap(SIGMA, annot=True,cmap='RdBu_r')
h.set_aspect("equal")
print(np.sqrt(np.diag(SIGMA)))
#%% correlation matrix

RHO = y_x_df.corr()

fig, axs = plt.subplots()

h = sns.heatmap(RHO, annot=True,cmap='RdBu_r')
h.set_aspect("equal")

#%% Volatility vector space

Angles = np.arccos(RHO)*180/np.pi
fig, axs = plt.subplots()

h = sns.heatmap(Angles, annot=True,cmap='RdBu_r')
h.set_aspect("equal")

def draw_vector(vector,RBG): 
    array = np.array([[0, 0, vector[0], vector[1]]])
    X, Y, U, V = zip(*array)
    plt.quiver(X, Y, U, V,angles='xy', scale_units='xy',scale=1,color = RBG)

angle = Angles['AAPL']['SP500']*np.pi/180

vols = np.sqrt(np.diag(SIGMA))
v_1_x = vols[1]
v_1_y = 0

v_2_x = vols[0]*np.cos(angle)
v_2_y = vols[0]*np.sin(angle)

fig, ax = plt.subplots()

draw_vector([v_1_x,v_1_y],np.array([0,112,192])/255)
draw_vector([v_2_x,v_2_y],np.array([255,0,0])/255)
plt.ylabel('$y, TSLA$')
plt.xlabel('$x, S&P500$')
plt.axis('scaled')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
ax.set_xlim([-0.01, 0.03])
ax.set_ylim([-0.01, 0.03])
ax.grid(linestyle='--', linewidth=0.25, color=[0.5,0.5,0.5])


#%% OLS Regression

# add a column of ones
X_df = sm.add_constant(x_df)

model = sm.OLS(y_df, X_df)
results = model.fit()
print(results.summary())


#%% visualization

p = model.fit().params

# generate x-values for  regression line
x = np.linspace(x_df.min(),x_df.max(),10)

fig, ax = plt.subplots()

# scatter-plot data
plt.scatter(x_df, y_df, alpha = 0.5)

plt.plot(x, p.const + p.SP500 * x,color = 'r')

plt.axhline(y=0, color='k', linestyle='--')
plt.axvline(x=0, color='k', linestyle='--')
plt.axis('scaled')
plt.ylabel('AAPL daily log return')
plt.xlabel('S&P 500 daily log return, market')
plt.xlim([-0.15,0.15])
plt.ylim([-0.15,0.15])

sns.jointplot(x=x_df['SP500'], y=y_df['AAPL'], kind="reg",
              xlim = [-0.15,0.15],ylim = [-0.15,0.15])
