import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.data_viz_to_coder.ex7 import *
print("Setup Complete")
# Fill in the line below: Specify the path of the CSV file to read
my_filepath = "../input/fivethirtyeight-comic-characters-dataset/dc-wikia-data.csv"
# Fill in the line below: Read the file into a variable my_data
my_data = pd.read_csv(my_filepath)
# Print the first five rows of the data
my_data.head()
# Create a plot
#plt.figure(figsize=(12x6))
sns.lineplot(data=my_data)
