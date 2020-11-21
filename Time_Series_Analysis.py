# Time-Series Analysis of Bitcoin Dataset from Kaggle
####################################################################################

# Dataset from <https://www.kaggle.com/mczielinski/bitcoin-historical-data>


# To my interviewer: You actually took the time to look at this!!

# THANK YOU!!!!!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.metrics import mean_squared_error
from math import sqrt
import statsmodels.api as sm
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt



####################################################################################
# Import and Process Data

bit_Nans = pd.read_csv('bitstamp_Kaggle_2012-01-01_to_2020-09-14.csv', index_col=['Timestamp'], parse_dates=['Timestamp'])

def clean_dataset(df):
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)
    
# Get rid of NaNs
bit=clean_dataset(bit_Nans)

# Convert Unix Time to Timestamp
bit_time=bit
bit_time.reset_index(inplace=True)
bit_time['Timestamp'] = pd.to_datetime(bit['Timestamp'],unit='s')


bit_len=bit.shape[0]
WP=bit.Weighted_Price

# Plot of Weighted Price of Bitcoin
#
# plt.figure(figsize=(15, 7))
# plt.plot(WP)
# plt.title('Weighted Price of Bitcoin (in Unix time)')
# plt.grid(True)
# plt.show()


####################################################################################
# Find Rolling Average and Determine Confidence Intervals

def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
wind=4        # window size
scale=1.96    # scale size

rolling_mean = WP.rolling(window=wind).mean()


# Plot confidence intervals for smoothed values
mae = mean_absolute_error(WP[wind:], rolling_mean[wind:])
deviation = np.std(WP[wind:] - rolling_mean[wind:])
lower_bond = rolling_mean - (mae + scale * deviation)
upper_bond = rolling_mean + (mae + scale * deviation)

# Plot of Weighted Price Moving Average and Confidence Intervals
#
# plt.figure(figsize=(15,5))
# plt.title("Moving average\n window size = {}".format(wind))
# plt.plot(upper_bond, "r:", dashes=(5, 1), linewidth=4, label="Upper Bond / Lower Bond")
# plt.plot(lower_bond, "r:",dashes=(5, 1), linewidth=4)
# plt.plot(rolling_mean, "k", label="Rolling mean trend")
# plt.show()
        


####################################################################################
# Finding and Removing Outliers with the Tukey Method

indexes = []
Q1 = np.percentile(WP, 25)
Q3 = np.percentile(WP,75)
IQR = Q3 - Q1
limit = 1.5 * IQR
list_outliers = WP[(WP < Q1 - limit) | (WP > Q3 + limit )].index
indexes.extend(list_outliers)


WP.drop(list_outliers, axis = 0)
WP_No_Outliers = WP.drop(list_outliers, axis = 0).reset_index(drop=True)

Outliers = WP[list_outliers]
outs_len = list_outliers.shape[0]
wp_len=WP_No_Outliers.shape[0]

# Plot of Weighted Price Outliers Highlighted in Red
#
# plt.plot(WP, "k", label="Weighted Price")
# plt.plot(Outliers, "ro", markersize=5, label="Outliers")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.show()

# Plot of Weighted Price Without Outliers
#
# plt.plot(WP_No_Outliers, "b", label="Weighted Price w/o Outliers")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.show()



####################################################################################
# Split Data into Train and Test, get RMS, and Prediction

train_len=int(bit_len * .8 )
train=bit_time[:train_len]
test=bit_time[train_len:]


# RMS
dd= np.asarray(train.Weighted_Price)
y_hat = test.copy()
y_hat['naive'] = dd[len(dd)-1]
rms = sqrt(mean_squared_error(test['Weighted_Price'], y_hat.naive))
print(rms)



# Plot of Weighted Price Train and Test Set
#
# plt.figure(figsize=(12,8))
# plt.plot(train.index, train['Weighted_Price'], label='Train')
# plt.plot(test.index,test['Weighted_Price'], label='Test')
# plt.legend(loc='best')
# plt.title("Train and Test Set for Weighted Price")
# plt.show()





# Working on it...to be posted soon
# sm.tsa.seasonal_decompose(train.Weighted_Price).plot()
# result = sm.tsa.stattools.adfuller(train.Count)
# plt.show()

# y_hat_avg = test_data.copy()
# fit1 = ExponentialSmoothing(np.asarray(train_data) ,seasonal_periods=7 ,trend='add', seasonal='add',).fit()
# y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))
# plt.figure(figsize=(16,8))
# plt.plot( train['Weighted_Price'], label='Train')
# plt.plot(test['Weighted_Price'], label='Test')
# plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
# plt.legend(loc='best')
# plt.show()
