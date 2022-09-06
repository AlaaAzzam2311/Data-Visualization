import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
# Path of the file to read
ign_filepath = "../input/ign_scores.csv"
ign_data = pd.read_csv(ign_filepath, index_col="Platform")
ign_data
high_score = 7.759930
worst_genre = 'Simulation'
plt.figure(figsize=(8, 6))
sns.barplot(x=ign_data['Racing'], y=ign_data.index)
plt.xlabel("")
plt.title("Average Score for Racing Games, by Platform")
plt.figure(figsize=(10,10))
sns.heatmap(ign_data, annot=True)
plt.xlabel("Genre")
plt.title("Average Game Score, by Platform and Genre")



