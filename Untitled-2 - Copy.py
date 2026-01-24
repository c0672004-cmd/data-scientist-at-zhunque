# %%
import pandas_datareader.data as web
import datetime 
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 

# %%
#Define the timeframe
start = datetime.datetime(2019, 1, 1) 
end = datetime.datetime(2025,12,31)

#pull the data from FRED 
#CPIAUCSL = Headline CPI, CPILFESL = Core CPI 
df = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)

# %%
df_yoy = df.pct_change(periods = 12) * 100

df_yoy.columns = ['CPI inflation (YoY, %)', 'Core CPI inflation (YoY, %)']


df_yoy = df_yoy.dropna()

# %%
plt.figure(figsize = (11,6))
plt.plot(df_yoy.index, df_yoy['CPI inflation (YoY, %)'], label = 'CPI inflation (YoY, %)', color = '#1f77b4', linewidth = 2)

plt.plot(df_yoy.index, df_yoy['Core CPI inflation (YoY, %)'], label = 'Core CPI inflation (YoY, %)', color = '#d62728', linewidth = 2)



plt.axvline(pd.to_datetime('2020-03-01'), color = 'gray', linestyle = '--')
plt.text(pd.to_datetime('2020-04-01'), 8.5, 'COVID shock', fontsize = 9)

plt.axvline(pd.to_datetime('2022-03-16'), color = 'gray', linestyle = '--')
plt.text(pd.to_datetime('2022-04-15'), 8, 'Fed hiking cycle begins', fontsize = 9) 

plt.title('US Inflation (YoY, %)', fontsize = 14, fontweight = 'bold', loc='left')
plt.ylabel('Percent (%)')
plt.ylim(0,10)
plt.grid(True, linestyle = ':', alpha = 0.6)
plt.legend(loc = 'lower center', bbox_to_anchor = (0.5, -0.2), ncol = 2, frameon = False)
plt.tight_layout()
plt.legend()
plt.show

# %%



