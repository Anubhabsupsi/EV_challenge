import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import requests
import zipfile
import io
import pandas as pd

url = 'https://codalab.lisn.upsaclay.fr/my/datasets/download/4b524c74-e8b9-4630-b3f9-4eb841677538'
response = requests.get(url)
response.raise_for_status()

with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    # List all files in the zip archive
    file_names = z.namelist()
    print("Files in the zip archive:", file_names)

    # Step 3: Read a specific file inside the zip archive
    # Assuming there's a CSV file inside the zip
    csv_filename = [f for f in file_names if f.endswith('.csv')][1]

    with z.open(csv_filename) as f:
        train_df = pd.read_csv(f)
        # Display the first few rows of the dataframe
        print(train_df.head())


train_slice = train_df[train_df['Station'].isin(['FR*V75*EBELI*10*1', 'FR*V75*EBELI*11*1'])]
sns.set_theme(style='darkgrid')
ax = sns.lineplot(x='date', y='Available', hue="Station", data=train_slice.iloc[np.arange(612)])
start_date = train_slice.iloc[0]['date']
end_date = train_slice.iloc[-1]['date']
plt.xticks([start_date, end_date], labels=[start_date, end_date])
ax.set_title('Distribution of Available charging points for a slice')
plt.show()

