# libraries
import pandas as pd
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import axes3d
 
 
# Get the data 
data = pd.read_csv('e_field.csv')
 
# Transform it to a long format
df=data.unstack().reset_index()
df.columns=["X","Y","Z"]
 
# Rescale the spreadsheet rows and columns to centimeters
df['X']=pd.Categorical(df['X'])

df['X']=df['X'].cat.codes*2 +1

df['Y']=pd.Categorical(df['Y'])

df['Y']=df['Y'].cat.codes*2 +1

# Make the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Giving you some color options

ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.coolwarm, linewidth=1)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.viridis, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.inferno, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.RdBu, linewidth=0.2)
#ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap=plt.cm.PiYG, linewidth=0.2)

ax.set_xlabel('X coordinate (cm)')
ax.set_ylabel('Y coordinate (cm)')
ax.set_zlabel('Voltage (V)')
plt.title('Electric Potential Scalar Field')

plt.show()
