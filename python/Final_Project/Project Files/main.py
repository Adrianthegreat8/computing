import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 12
plt.rcParams['font.family'] = 'Arial'

# Load unemployment data
unemployment_data = pd.read_csv('cpsaat01.csv', skiprows=6, index_col=0)
unemployment_data = unemployment_data.iloc[:, 8].dropna()

# Extract years as integers
unemployment_years = np.array([int(year) for year in unemployment_data.index.values])

# Define ticks
years_ticks = np.arange(unemployment_years.min(), unemployment_years.max(), 10)

# Load GDP data
gdp_data = pd.read_csv('API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_84037.csv', skiprows=3, header=0, index_col=0)
gdp_us = gdp_data.loc['United States'][4:-2]
gdp_years = np.array([int(year) for year in gdp_us.index.values])

# Unemployment Rate x Year Plot
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(unemployment_years, unemployment_data.values, '-b', label='Unemployment Rate')
ax1.tick_params(labelrotation=90)
ax1.set_xticks(years_ticks)

# Labeling and customization for Unemployment Rate plot
ax1.set_xlabel('Year')
ax1.set_ylabel('Unemployment Rate (%)')
ax1.set_title('US Unemployment Rate Over Time')
ax1.legend(loc='upper left')
ax1.grid(True)

# GDP x Year Plot
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(gdp_years, gdp_us, '-r', label='GDP Growth')
ax2.tick_params(labelrotation=90)
ax2.set_xticks(years_ticks)

# Labeling and customization for GDP plot
ax2.set_xlabel('Year')
ax2.set_ylabel('GDP Growth (%)')
ax2.set_title('US GDP Growth Over Time')
ax2.legend(loc='upper left')
ax2.grid(True)

# Alignment of data based on common years
common_years = unemployment_data.index.intersection(gdp_us.index)
unemployment_data_aligned = unemployment_data.loc[common_years]
gdp_us_aligned = gdp_us.loc[common_years].astype(float)

# Regression
# Fit a linear regression model
model_coeffs = np.polyfit(unemployment_data_aligned, gdp_us_aligned, 1)
model_func = np.poly1d(model_coeffs)

# Generate predicted GDP growth values based on the model
predicted_gdp_growth = model_func(unemployment_data_aligned)

# Plot GDP growth and Linear Model
fig3, ax3 = plt.subplots(figsize=(10,6))
ax3.plot(unemployment_data_aligned, gdp_us_aligned, '.b', label='GDP Growth')
ax3.plot(unemployment_data_aligned, predicted_gdp_growth, '-r', label='Linear Model')
ax3.tick_params(labelrotation=90)
ax3.set_xlabel('Unemployment Rate (%)')
ax3.set_ylabel('GDP Growth (%)')
ax3.set_title('Modeling US GDP with Unemployment Rate')
ax3.legend()
ax3.grid(True)

# Calculate R^2
SSR = ((gdp_us_aligned - predicted_gdp_growth)**2).sum()
SST = ((gdp_us_aligned - gdp_us_aligned.mean()) ** 2).sum()
R2 = 1-(SSR/SST)
print('The R^2 Value is %.2f' %R2)

# Calculate and plot residuals
fig4, ax4 = plt.subplots(figsize=(10,6))
residuals = gdp_us_aligned - predicted_gdp_growth
ax4.plot(unemployment_data_aligned,residuals,'.b',label='Residuals')
xsmall = np.arange(unemployment_data_aligned.min()-.5,unemployment_data_aligned.max()+.5,0.5)
y0small = np.zeros(xsmall.size)
ax4.plot(xsmall,y0small,'r',label='Y = Zero')
ax4.set_xlabel('Unemployment Rate %')
ax4.set_ylabel('Residuals')
ax4.legend()
ax4.grid()

plt.show()

# Compute the mean of the independent variable
x_mean = unemployment_data_aligned.mean()
# Compute the sum of squares of the independent variable
SSX = ((unemployment_data_aligned - x_mean) ** 2).sum()
# Compute the standard error of the slope (SE(m))
SE_m = np.sqrt(SSR / ((len(unemployment_data_aligned) - 2) * SSX))
# Compute the standard error of the intercept (SE(b))
SE_b = SE_m * np.sqrt((unemployment_data_aligned ** 2).sum() / len(unemployment_data_aligned))

# T-Test of slope
t_score = np.abs((model_coeffs[0] / SE_m))

# Save Results
myfile = open('results.txt','w')
myfile.write('Linear Model Coefficients:\n')
myfile.write('Intercept (b): ' + str(model_coeffs[1]) + '\n')
myfile.write('Standard Error of the Intercept (SE(b)): ' + str(SE_b) + '\n')
myfile.write('Slope (m): ' + str(model_coeffs[0]) + '\n')
myfile.write('Standard Error of the Slope (SE(m)): ' + str(SE_m) + '\n')
myfile.write('R^2:' + str(R2) + '\n')
myfile.write('T-Statistic of slope as compared to 0: ' + str(t_score) + '\n')
myfile.close()

# savve figures
fig1.savefig('unemployment_plot.jpg', dpi=300)
fig2.savefig('gdp_plot.jpg', dpi=300)
fig3.savefig('linear_model_plot.jpg', dpi=300)
fig4.savefig('residuals_plot.jpg', dpi=300)