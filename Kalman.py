import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from filterpy.kalman import KalmanFilter

csv_path = "/Users/lgw/Downloads/elevator_data/up_2.csv"
acc_df = pd.read_csv(csv_path)

Kf = KalmanFilter(dim_x=2, dim_z=1)

Kf.x = np.array([0, 0])
Kf.P *= 1e-2

Kf.F =np.array([[1, 1],
               [0, 1]])

Kf.H = np.array([[1, 0]])

Kf.Q *= 1e-5
Kf.R *= 1e-1

filtered_data = []
print('check point')
for measurement in acc_df['z'] :
    Kf.predict()
    Kf.update(measurement)

    state_estimate = Kf.x

    filtered_data.append(state_estimate[0])
    print('successfully filtered')
acc_df['filtered_z'] = filtered_data

raw_acc = acc_df['z']
filtered_acc = acc_df['filtered_z']

time = range(len(raw_acc))

plt.figure(figsize=(10,6))
plt.plot(time, raw_acc, label='Raw Acc',alpha=.5)
plt.plot(time, filtered_acc, label = "Filtered Acc", color='red')
plt.xlabel('Time')
plt.ylabel('ACC')
plt.legend()
plt.grid()
plt.title('Kalman Filtered')

plt.show()
