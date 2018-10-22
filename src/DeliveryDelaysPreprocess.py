import pandas as pd
import numpy as np

data = pd.read_csv('Data4516.csv')
data = data[(data['Cervidil'] == 'No') & (data['Gestational Age (Weeks)'] > 10)]
data['delay1'] = data['Interval Between Dose #1 and #2 (hours)'] - 4
data['delay2'] = data['Interval Between Dose #2 and #3 (hours)'] - 4
data['delay3'] = data['Interval Between Dose #3 and #4 (hours)'] - 4
data['delay4'] = data['Interval Between Dose #4 and #5 (hours)'] - 4
data['delay5'] = data['Interval Between Dose #5 and #6 (hours)'] - 4
data['delay6'] = data['Interval Between Dose #6 and #7 (hours)'] - 4

data['CumulativeDelay'] = data[['delay1', 'delay2', 'delay3', 'delay4', 'delay5', 'delay6']].sum(axis=1)
data['Time to Delivery'] = data['Time to Vaginal Delivery (hours)']
data['Time to Delivery'].fillna(data['Time to Operative Delivery (Hours)'], inplace=True)
data['Time to Delivery'].fillna(data['Time to Cesarean Section (Hours)'], inplace=True)
data = data[['Adherence to Dosing Protocol for all doses', 'Time to Delivery', 'Vaginal Delivery', 'CumulativeDelay']]

data = data[np.isfinite(data['Time to Delivery'])]
data['Adherence to Dosing Protocol for all doses'].fillna('Yes',inplace=True)

data['Adjusted Time to Delivery'] = data['Time to Delivery'] - data['CumulativeDelay']

data.to_csv('processed_delivery_data.csv')