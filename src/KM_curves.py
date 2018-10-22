import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines import CoxPHFitter

data = pd.read_csv('data/processed_delivery_data.csv')

kmf = KaplanMeierFitter()

groups = data['Adherence to Dosing Protocol for all doses']
ix = (groups == 'No')

T = data['Time to Delivery']
C = (data['Vaginal Delivery'] == 'Yes')

kmf.fit(T[~ix], C[~ix], label='Routine Interval Dosing', alpha=.95)
ax = kmf.plot(show_censors=True, color='b')

kmf.fit(T[ix], C[ix], label='Extended Interval Dosing', alpha=.95)
kmf.plot(ax=ax, show_censors=True, color='r')

ax.set_xlim(0, 60)
ax.set_ylim(0, 1)
plt.xlabel('Time to Delivery (hrs)')
plt.ylabel('Frac. Not Delivered')
plt.title('Time to Vaginal Delivery as a Function of Dosing Interval')
plt.savefig('output/traditional_KM.png')

kmf = KaplanMeierFitter()

T = data['Adjusted Time to Delivery']
C = (data['Vaginal Delivery'] == 'Yes')

kmf.fit(T[~ix], C[~ix], label='Routine Interval Dosing', alpha=.95)
ax = kmf.plot(show_censors=True, color='b')

kmf.fit(T[ix], C[ix], label='Extended Interval Dosing', alpha=.95)
kmf.plot(ax=ax, show_censors=True, color='r')

ax.set_xlim(0, 60)
ax.set_ylim(0, 1)
plt.xlabel('Time to Delivery (hrs)')
plt.ylabel('Frac. Not Delivered')
plt.title('Delay Adjusted Time to Vaginal Delivery as a Function of Dosing Interval')
plt.savefig('output/adjusted_KM.png')

cph = CoxPHFitter()
cph.fit(data[['Time to Delivery', 'Vaginal Delivery', 'CumulativeDelay']], duration_col='Time to Delivery',
        event_col='Vaginal Delivery', show_progress=True)

cph.plot_covariate_groups('CumulativeDelay', [0, 2, 4, 8, 16])
ax.set_xlim(0, 60)
ax.set_ylim(0, 1)
plt.xlabel('Time to Delivery (hrs)')
plt.ylabel('Frac. Not Delivered')
plt.title('Predicted Delivery Curves as a Function of Cumulative Dosing Interval Delay')
plt.savefig('output/predicted_KM.png')




