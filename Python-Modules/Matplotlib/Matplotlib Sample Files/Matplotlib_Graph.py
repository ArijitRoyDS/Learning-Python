import matplotlib                              # To Plot Basic Graphs
import pandas as pd                            # For performing excel file open/read/write/Data Cleaning operations against the input text file
from matplotlib import pyplot as plt           # To Plot Advanced Graphs
from matplotlib.ticker import LinearLocator, FormatStrFormatter                # To format graphs visually
from mpl_toolkits.mplot3d import Axes3D                                        # To format Axes in Graph
from matplotlib import tri                                                     # For Triangulation functions in triangular surface plots (interpolation)
from matplotlib.lines import Line2D            # To format 2D line graphs
import numpy as np                             # To build Numerical Arrays for Multiple Bar Graphs 
# import glob
# from PIL import Image
# import os



###############################################################################################################################################
#1 --> SIMPLE 2D LINE GRAPH
###############################################################################################################################################

# Read data from excel with the given path and file name / sheet name
df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "Simple Line")     

# Extract the X, Y, Z Axis Labels from the Column Headers
list1 = list(df.columns)
x_label = list1[0]
y_label = list1[1]

# Option 1: Read Graph Data by Column Index                                         
# X = df.iloc[:,0]                                                                                                                       
# Y = df.iloc[:,1]                                                                    

# Option 2: Read Graph Data by Column Name
X = df[x_label]                                                                                                       
Y = df[y_label]     

# Create and Define size and aspect ratio of the graph
fig = plt.figure(figsize = (8,8))                                                                      

plt.plot(X, Y, label = "TRQL_MIN_TORQUE_TEMP_MAP_Y", marker='o')                                           # Syntax to plot the graph
plt.xlabel(x_label, fontsize=12, labelpad=4, fontweight='bold', fontname='calibri')                        # Define X Axis Label, font and distance between axis and label
plt.ylabel(y_label, fontsize=12, labelpad=10, fontweight='bold', fontname='calibri')                       # Define Y Axis Label, font and distance between axis and label
plt.title("TRQL_MIN_TORQUE_TEMP_MAP_Y", fontsize=16, fontweight='bold', fontname='times new roman')        # Define Graph Title and font size
plt.grid(linewidth=0.3)                                                                                    # Define thickness / weight of the line

# Create Annotations and define the position where it should be printed
for x, y in zip(X, Y):
    # Set the exact location, font size and angle of plot data
    # plt.annotate(x, (x-10,y), textcoords='data', fontsize=10, rotation=45)
    plt.annotate(y, (x,y-20), textcoords='data', fontsize=10, rotation=45)     
    
plt.tight_layout()                                                             # Fits the plot, labels and ticks inside the frame

fig.savefig("Simple Line Plot.png", dpi=300)                                   # Set the resolution and save the image
#fig.savefig('SineSignal.svg', format = 'svg')                                 # To save image in svg format

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  
 
print("Successfully plotted Simple Line Plot") 


###############################################################################################################################################
#2 --> MULTIPLE 2D LINES IN A SINGLE GRAPH
###############################################################################################################################################

# Read the temporary excel using Pandas and plot Line Graph based on column numbers identified by iloc where iloc[:,0] is the first column
df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "Multiple Lines")

# Extract the X, Y, Z Axis Labels from the Column Headers
list1 = list(df.columns)
x_label = list1[0]
y_label = list1[1]

# # Option 1: Read Graph Data by Column Index
# X = df.iloc[:,0]
# Y1 = df.iloc[:,1]
# Y2 = df.iloc[:,2]
# Y3 = df.iloc[:,3]

# Option 2: Read Graph Data by Column Name
X = df[list1[0]] 
Y1 = df[list1[1]]
Y2 = df[list1[2]]
Y3 = df[list1[3]]

# Create and Define size and aspect ratio of the graph
fig = plt.figure(figsize = (15,4)) 

# Plot all the lines in the same graph defined above
plt.plot(X, Y1, marker='o')
plt.plot(X, Y2, marker='o')
plt.plot(X, Y3, marker='o')

# Set the Legends                              
legend_elements = [Line2D([0], [0], color='b', lw=2, label=list1[1]), Line2D([0], [0], color='orange', lw=2, label=list1[2]), Line2D([0], [0], color='green', lw=2, label=list1[3])]  
plt.legend(handles=legend_elements)

# Define Graph Titles, Labels and font type/size
plt.title(x_label + " V/S " + y_label, fontsize=16, fontweight='bold', fontname='times new roman')         
plt.xlabel(x_label, fontsize=12, labelpad=8, fontweight='bold', fontname='calibri')
plt.ylabel(y_label, fontsize=12, labelpad=10, fontweight='bold', fontname='calibri')
plt.grid(linewidth=0.3)

plt.tight_layout()                                                             # Fits the plot, labels and ticks inside the frame
fig.savefig("Multiple Lines Plot.png", dpi=300)                                # Define a resolution and save the image

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  
 
print("Successfully plotted Multiple Lines Plot")   


###############################################################################################################################################
#3 --> SIMPLE BAR GRAPHS
###############################################################################################################################################

# Read the excel using Pandas and plot bAR Graph based on column numbers identified by iloc where iloc[:,0] is the first column
df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "Bar")

# Define X and Y Labels
list1 = list(df.columns)
x_label = list1[0]
y_label = list1[1]

# # Option 1: Read Graph Data by Column Index
# X = df.iloc[:,0]
# Y = df.iloc[:,1]    

# Option 2: Read Graph Data by Column Name
X = df[list1[0]] 
Y = df[list1[1]]

# Create and Define size and aspect ratio of the graph
fig1 = plt.figure(figsize = (15,4))   

# Plot the Graph
plt.bar(X, Y, width=40, color = "Red")

# Set Graph Title and X / Y Axis Labels
plt.title(x_label + " V/S " + y_label, fontsize=16, fontweight='bold', fontname='times new roman')         # Define Graph Title and font size
plt.xlabel(x_label, fontsize=12, labelpad=8, fontweight='bold', fontname='calibri')
plt.ylabel(y_label, fontsize=12, labelpad=10, fontweight='bold', fontname='calibri')

plt.grid(linewidth=0.3)
plt.tight_layout()                                                             # Fits the plot, labels and ticks inside the frame

fig1.savefig("Simple Bar Graph.png", dpi=300)                                  # to save files in png format
#fig1.savefig('Simple Bar Graph.svg', format = 'svg')                            # to save files in svg format

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  
 
print("Successfully plotted Simple Bar Graph")   


###############################################################################################################################################
#4 --> MULTIPLE BARS IN A SINGLE GRAPH
###############################################################################################################################################
   
# Read the excel using Pandas and plot bAR Graph based on column numbers identified by iloc where iloc[:,0] is the first column
df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "Bar")

# Define X and Y Labels
list1 = list(df.columns)
x_label = list1[0]
y1_label = list1[1]
y2_label = list1[2]
y3_label = list1[3]

# # Option 1: Read Graph Data by Column Index
# X = df.iloc[:,0]
# Y1 = df.iloc[:,1]   
# Y2 = df.iloc[:,2]    
# Y3 = df.iloc[:,3]   

# Option 2: Read Graph Data by Column Name
X = df["Engine_Speed [rpm]"] 
Y1 = df["Engine_Torque 1 [Nm]"]
Y2 = df["Engine_Torque 2 [Nm]"]
Y3 = df["Engine_Torque 3 [Nm]"]

# Create and Define size and aspect ratio of the graph
fig2 = plt.figure(figsize = (15,4))    

# Define an array for X Axis values to equally space them even if they are not linearly apart
X_axis = np.arange(len(X))  

# Plot the Graph
plt.bar(X_axis - 0.2, Y1, 0.2, color = "Red", label = y1_label)
plt.bar(X_axis, Y2, 0.2, color = "Green", label = y2_label)
plt.bar(X_axis + 0.2, Y3, 0.2, color = "Blue", label = y3_label)

# Set Graph Title and X / Y Axis Labels
plt.xticks(X_axis, X)
plt.title(x_label + " V/S " + y_label, fontsize=16, fontweight='bold', fontname='times new roman')         # Define Graph Title and font size
plt.xlabel(x_label, fontsize=12, labelpad=8, fontweight='bold', fontname='calibri')
plt.ylabel(y_label, fontsize=12, labelpad=10, fontweight='bold', fontname='calibri')

plt.grid(linewidth=0.3)
plt.legend()

plt.tight_layout()                                                             # Fits the plot, labels and ticks inside the frame
fig2.savefig("Multiple Bar Graphs.png", dpi=300)  

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  
 
print("Successfully plotted Multiple Bar Graphs")   


###############################################################################################################################################
#5 --> 3D SCATTER PLOT
###############################################################################################################################################

df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "3D Scatter")

# Define X, Y, Z Labels
list1 = list(df.columns)
x_label = list1[0]
y_label = list1[1]
z_label = list1[2]

# # Option 1: Read Graph Data by Column Index
# X = df.iloc[:,0]                                                           
# Y = df.iloc[:,1]
# Z = df.iloc[:,2]

# Option 2: Read Graph Data by Column Name
X = df["EMS_A7.itvcc_ThrottlePos"] 
Y = df[y_label]
Z = df[z_label]

# X = df["EMS_A7.itvcc_ThrottlePos"] 
# Y = df[y_label]
# Z = df[z_label]

matplotlib.rcParams['savefig.dpi'] = 200                                       # Set the resolution of the graph. Increase it if a higher resolution image is needed
matplotlib.rcParams["figure.dpi"] = 200                                        # Set the resolution of the saved image. Increase it if a higher resolution image is needed

# Create and Define size and aspect ratio of the graph
fig = plt.figure(figsize = (14, 10))
ax = plt.axes(projection ="3d")

# Set Graph Background Colour and fontsize of Axis Tickers
ax.set(facecolor = "white")
ax.tick_params(axis='x', labelsize=12, pad=12)
ax.tick_params(axis='y', labelsize=12, pad=12)
ax.tick_params(axis='z', labelsize=12, pad=12)

# Creating plot
ax.scatter3D(X, Y, Z, color = "red")
ax.scatter3D(X*1.2, Y+5, Z+5, color = "blue")

# Set the view angle of the plotted SUrface Map before saving it. 
ax.view_init(elev=30, azim=45)

# Set the Graph Title, X, Y, Z Axis Labels and their font size
fig.title = ("3D Scatter Plot")
ax.set_title("3D Scatter Plot", fontsize=26, fontweight='bold', fontname='times new roman')  
ax.set_xlabel(x_label, fontsize=14, labelpad=35, fontweight='bold', fontname='calibri')
ax.set_ylabel(y_label, fontsize=14, labelpad=35, fontweight='bold', fontname='calibri')
ax.set_zlabel(z_label, fontsize=14, labelpad=35, fontweight='bold', fontname='calibri')

plt.tight_layout()                                                             # Fits the plot, labels and ticks inside the frame
fig.savefig("3D Scatter Plot.png")  

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  

print("Successfully plotted 3D Scatter Plot")  


###############################################################################################################################################
#6 --> SIMPLE TRIANGULAR SURFACE PLOT 3D
###############################################################################################################################################

df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "Trisurf")

# Define X, Y, Z Labels
list1 = list(df.columns)
x_label = list1[0]
y_label = list1[1]
z_label = list1[2]

# # Option 1: Read Graph Data by Column Index
# X = df.iloc[:,0]                                                           
# Y = df.iloc[:,1]
# Z = df.iloc[:,2]

# Option 2: Read Graph Data by Column Name
X = df[x_label] 
Y = df[y_label]
Z = df[z_label]

matplotlib.rcParams['savefig.dpi'] = 300                                       # Set the resolution of the graph. Increase it if a higher resolution image is needed
matplotlib.rcParams["figure.dpi"] = 300                                        # Set the resolution of the saved image. Increase it if a higher resolution image is needed

fig = plt.figure(figsize = (15,12))                                            # Create and Define size and aspect ratio of the graph
ax = fig.gca(projection='3d')                                                  # Define the projection for 3D Graph  

# Set Graph Background Colour and fontsize of Axis Tickers
ax.set(facecolor = "white")
ax.tick_params(axis='x', labelsize=12, pad=8)
ax.tick_params(axis='y', labelsize=12, pad=8)
ax.tick_params(axis='z', labelsize=12, pad=8)

# Plot the surface Map with X, Y, Z Axis Values
surf = ax.plot_trisurf(X, Y, Z, cmap=("brg"), linewidth=0, antialiased=True, shade = True)

# Customize the z axis tickers
ax.zaxis.set_major_locator(LinearLocator(10))                                  # Place 10 evenly spaced Linear data locators on X Axis
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))                      # Each value should be a float with 2 places of decimal, converted to string

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=12)

# Set the view angle and zoom level of the plotted Surface Map before saving it. 
ax.view_init(elev=30, azim=45)
ax.dist=10

# Set the Graph Title, X, Y, Z Axis Labels and their font size
fig.title = ("TMFD_FUEL_ECON_MAP_Z_")
ax.set_title("TMFD_FUEL_ECON_MAP_Z_", fontsize=30, fontweight='bold', fontname='times new roman')     
ax.set_xlabel(x_label, fontsize=14, labelpad=20, fontweight='bold', fontname='calibri')
ax.set_ylabel(y_label, fontsize=14, labelpad=20, fontweight='bold', fontname='calibri')
ax.set_zlabel(z_label, fontsize=14, labelpad=20, fontweight='bold', fontname='calibri')

fig.savefig("Simple Triangular Surface Plot.png")  

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  
 
print("Successfully plotted Simple Triangular Surface Plot")                            


###############################################################################################################################################
#7 --> TRIANGULAR SURFACE PLOT USING INTERPOLATION
###############################################################################################################################################

df = pd.read_excel("C:\\Python\\Backup\\Projects\\Matlab to Python\\Matplotlib Training\\Sample.xlsx", "Trisurf")

# Define X and Y Labels
list1 = list(df.columns)
x_label = list1[0]
y_label = list1[1]
z_label = list1[2]

# # Option 1: Read Graph Data by Column Index
# X = df.iloc[:,0]                                                           
# Y = df.iloc[:,1]
# Z = df.iloc[:,2]

# Option 2: Read Graph Data by Column Name
X = df[x_label] 
Y = df[y_label]
Z = df[z_label]

matplotlib.rcParams['savefig.dpi'] = 200                                       # Set the resolution of the graph. Increase it if a higher resolution image is needed
matplotlib.rcParams["figure.dpi"] = 200                                        # Set the resolution of the saved image. Increase it if a higher resolution image is needed

fig = plt.figure(figsize = (12,11))                                            # Create and Define size and aspect ratio of the graph
ax = Axes3D(fig)                                                               # Define the projection for 3D Graph  

# Set Graph Background Colour and fontsize of Axis Tickers
ax.set(facecolor = "white")
ax.tick_params(axis='x', labelsize=12, pad=8)
ax.tick_params(axis='y', labelsize=12, pad=8)
ax.tick_params(axis='z', labelsize=12, pad=8)

# Code to get a smooth surface by interpolating the mean values of X, Y, Z axes
triang = tri.Triangulation(X, Y)
refiner = tri.UniformTriRefiner(triang)
new, new_z = refiner.refine_field(Z, subdiv=4)   
kwargs = dict(triangles=new.triangles, cmap=("brg"), linewidth=0.5)

# Plot the surface Map with X, Y, Z Axis Values
surf = ax.plot_trisurf(new.x, new.y, new_z, **kwargs)

# Customize the z axis.
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=12)

# Set the view angle and zoom level of the plotted Surface Map before saving it. 
ax.view_init(elev=30, azim=45)
ax.dist=12

# Set the Graph Title, X, Y, Z Axis Labels and their font size
fig.title = ("TMFD_FUEL_ECON_MAP_Z_")
ax.set_title("TMFD_FUEL_ECON_MAP_Z_", fontsize=30, fontweight='bold', fontname='times new roman')     
ax.set_xlabel(x_label, fontsize=14, labelpad=20, fontweight='bold', fontname='calibri')
ax.set_ylabel(y_label, fontsize=14, labelpad=20, fontweight='bold', fontname='calibri')
ax.set_zlabel(z_label, fontsize=14, labelpad=20, fontweight='bold', fontname='calibri')

fig.savefig("Triangular Surface Plot using Interpolation.png")  

# To open the image in interactive window. Go to Tools>Preferences>IPython Console>Graphics and set backend to Qt5. Refresh the Console and run the code
plt.ion() 

# To show the graph in the console. Go to Tools>Preferences>IPython Console>Graphics and set backend to Inline. Refresh the Console and run the code                                                                                                                    
plt.show()  

print("Successfully plotted Triangular Surface Plot using Interpolation")   

