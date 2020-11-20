# Time-Series Analysis Example with Bitcoin Kaggle Dataset
####################################################################################
# Dataset from <https://www.kaggle.com/mczielinski/bitcoin-historical-data>

# To my interviewer: You actually took the time to look at this!!

# THANK YOU!!!!!


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



####################################################################################
# Import dataset and remove Nans

bit_Nans = pd.read_csv('bitstamp_Kaggle_2012-01-01_to_2020-09-14.csv', index_col=['Timestamp'], parse_dates=['Timestamp'])

def clean_dataset(df):
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)

bit=clean_dataset(bit_Nans)

len_bit=bit.size
WP=bit.Weighted_Price

# Plot of Weighted Price of Bitcoin with NaNs Removed
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
outs_len = Outs.size
wp_len=WP_No_Outliers.size

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




