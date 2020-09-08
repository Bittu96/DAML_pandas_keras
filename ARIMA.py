from numpy import *
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA

random.seed(1)

series = random.randint(5,20,100)
print series

df = pd.DataFrame({'series':series})
df.index +=1
print df
#df.plot.line()

df_log = log(df) 
#df_log.plot.line(label='series_log')
#plt.ylim([0,10])

rm = df['series'].rolling(10).mean()
#rm.plot.line(label='rolling mean')

rv = df['series'].rolling(10).std()
#rv.plot.line(label='rolling std')

rm_log = df_log['series'].rolling(10).mean()
#rm_log.plot.line(label='rolling log mean')

rv_log = df_log['series'].rolling(10).std()
#rv_log.plot.line(label='rolling log std')

dftest = adfuller(df['series'],autolag='AIC')
print dftest
dfoutput = pd.Series(dftest[0:4], index=['test statistic', 'p-value', '#lags used', 'no. of observations used'])
print dfoutput

'''
lag_acf = acf(df_log, nlags=20)
lag_pacf = pacf(df_log, nlags=20, method='ols')
#Plot ACF: 
plt.subplot(121) 
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(df_log)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(df_log)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')

#Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(df_log)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(df_log)),linestyle='--',color='gray')
plt.title('Partial Autocorrelation Function')
plt.tight_layout()
'''

df_log_diff = df_log - df_log.shift()
#plt.plot(df_log_diff,label='df_log_diff')

model = ARIMA(df_log, order=(2, 1, 0))  
results_AR = model.fit(disp=-1)  
#plt.plot(results_AR.fittedvalues, label='AR fit')
df_log_diff.dropna(inplace=True)
#plt.title('RSS: %.4f'% sum((results_AR.fittedvalues-df_log_diff)**2))


model = ARIMA(df_log, order=(0, 1, 2))  
results_MA = model.fit(disp=-1)
#plt.plot(results_MA.fittedvalues, label='MA fit')
#plt.title('RSS: %.4f'% sum((results_MA.fittedvalues-df_log_diff)**2))

'''
model = ARIMA(df_log, order=(2, 1, 2))  
results_ARIMA = model.fit(disp=-1)  
plt.plot(results_ARIMA.fittedvalues, color='red')
plt.title('RSS: %.4f'% sum((results_ARIMA.fittedvalues-df_log_diff)**2))
'''

predictions_AR_diff = pd.Series(results_AR.fittedvalues, copy=True)
print predictions_AR_diff.head()
predictions_AR_diff_cumsum = predictions_AR_diff.cumsum()
print predictions_AR_diff_cumsum.head()

predictions_AR_log = pd.Series(df_log.index[0], index=df_log.index)
predictions_AR_log = predictions_AR_log.add(predictions_AR_diff_cumsum,fill_value=0)
predictions_AR_log.head()

predictions_AR = np.exp(predictions_AR_log)
#plt.plot(df,label='series')
#plt.plot(predictions_AR,label='predictions_AR')
#plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_AR-df)**2)/len(df)))

results_AR.plot_predict(1,150)
print results_AR.forecast(steps=2)
plt.ylim([-5,10])

######///////////////////////////////////////////////////////////////////
'''
predictions_MA_diff = pd.Series(results_MA.fittedvalues, copy=True)
print predictions_MA_diff.head()
predictions_MA_diff_cumsum = predictions_MA_diff.cumsum()
print predictions_MA_diff_cumsum.head()

predictions_MA_log = pd.Series(df_log.index[0], index=df_log.index)
predictions_MA_log = predictions_MA_log.add(predictions_MA_diff_cumsum,fill_value=0)
predictions_MA_log.head()

predictions_MA = np.exp(predictions_MA_log)
#plt.plot(df)
#plt.plot(predictions_MA)
#plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_AR-df)**2)/len(df)))

results_MA.plot_predict(1,150)
results_MA.forecast(steps=100)
'''
######///////////////////////////////////////////////////////////////////

plt.legend()
plt.show(block=True)