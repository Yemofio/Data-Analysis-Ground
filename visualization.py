import seaborn as sns
import matplotlib.pyplot as plt

# load data
tips = sns.load_dataset("tips")

# create scatter plot
sns.scatterplot(x="total_bill", y="tip", data=tips)

# set plot title and axis labels
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")

# display plot
plt.show()
