import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

file_path = '/home/anubhabb/Documents/EV comp/public_data/'
train_df = pd.read_csv(''.join([file_path,'train.csv']))
train_slice = train_df[train_df['Station'].isin(['FR*V75*EBELI*10*1', 'FR*V75*EBELI*11*1'])]
sns.set_theme(style='darkgrid')
ax = sns.lineplot(x='date', y='Available', hue="Station", data=train_slice.iloc[np.arange(612)])
start_date = train_slice.iloc[0]['date']
end_date = train_slice.iloc[-1]['date']
plt.xticks([start_date, end_date], labels=[start_date, end_date])
ax.set_title('Distribution of Available charging points for a slice')
plt.show()