# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import libraries
import csv
import matplotlib
import matplotlib.pyplot
matplotlib.use('TkAgg')
from matplotlib import colors
import tkinter
from tkinter import simpledialog
import timeit

# Create lists
population = []
poprow = []
ratscaught = []
ratsrow = []
deaths=[]
deathrow=[]
deathstotal=[]

### Reading in data ###

# Read in population data to population list
f = open('death.parishes.txt', newline='')

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:    
    population.append(row)
    poprow = []
    for people in row:
        poprow.append(people)
    
f.close()

"""
# Test data import by finding total
poptotal=[]
for poprow in population:
    poptotal.append((sum(poprow)))

print(sum(poptotal))
"""

# Read in data of average rats caught to ratscaught list
f = open('death.rats.txt', newline='')

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for value in reader:
    ratsrow=[]
    ratscaught.append(value)
    for rat in value:
        ratsrow.append(rat)
    
f.close()

"""
# Test data import by finding total
rattotal=[]
for ratsrow in ratscaught:
    rattotal.append((sum(ratsrow)))
print(sum(rattotal))
"""


### Defining functions ###


# Define function to create map
# Set map area
# Remove tick labels
# Set colour bar
# Set title name
# Display map

def create_map(datalist, titlename):
    fig,ax = matplotlib.pyplot.subplots()
    cmap = colors.ListedColormap(['#FFFFFF', '#E2E2E2', '#C6C6C6', '#AAAAAA',
                                  '#8D8D8D', '#717171', '#555555', '#383838',
                                  '#1C1C1C', '#000000'])
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    matplotlib.pyplot.title(titlename)
    matplotlib.pyplot.imshow(datalist, cmap=cmap)
    matplotlib.pyplot.colorbar()


# Create map using population data
def runpop():
    create_map(population, 'Population density')


# Create map using rats caught data
def runrat():
    create_map(ratscaught, 'Numbers of rats caught')     


# Get user input for equation weighting
# Calculate deaths data
# Create map using deaths data
    
def rundeath():
    rat_inp = simpledialog.askfloat(title="Input",
                                  prompt="What is the rat weighting?:",
                                  initialvalue=0.8)


    pop_inp = simpledialog.askfloat(title="Input",
                                  prompt="What is the population weighting?:",
                                  initialvalue=1.3)

    calc_deaths(rat_inp,pop_inp)
    create_map(deaths, 'Estimated deaths')
    
    
# Get user input for equation weighting
# Calculate deaths data
# Save deaths data to directory as txt
# Display message to tell user data is saved
    
def maketxt():
    rat_inp = simpledialog.askfloat(title="Input",
                                  prompt="What is the rat weighting?:",
                                  initialvalue=0.8)


    pop_inp = simpledialog.askfloat(title="Input",
                                  prompt="What is the population weighting?:",
                                  initialvalue=1.3)

    calc_deaths(rat_inp,pop_inp)
    f = open('death.deaths.txt','w', newline='\n')
    newfile = csv.writer(f)
    for deathrow in deaths:
        newfile.writerow(deathrow)
    tkinter.messagebox.showinfo("File saved", ('Deaths data saved to current directory'))
    f.close()


# Close window to exit
def close_window(): 
    root.destroy()


# Get user input for equation weighting
# Calculate deaths data
# Sum deaths data to find total number of deaths
# Display total in message    
    
def total_deaths():    
    rat_inp = simpledialog.askfloat(title="Input",
                                  prompt="What is the rat weighting?:",
                                  initialvalue=0.8)


    pop_inp = simpledialog.askfloat(title="Input",
                                  prompt="What is the population weighting?:",
                                  initialvalue=1.3)

    calc_deaths(rat_inp,pop_inp)
    
    for deathrow in deaths:
        deathstotal=[]
        deathstotal.append((sum(deathrow)))
    deathsum = sum(deathstotal)
    tkinter.messagebox.showinfo("Total deaths", ('The estimated total number of deaths is ' + str(deathsum))) 


# Simultaneously read population and rat caughts data to find data pairs
# Caluclate death figure using data pairs and weighting from input
    
def calc_deaths(rat_inp,pop_inp):    
    for poprow, ratsrow in zip(population, ratscaught):
        deathrow=[]
        for p, r in zip(poprow, ratsrow):
            d = (rat_inp*r)*(pop_inp*p)
            deathrow.append(d)
        deaths.append(deathrow)
    """
    # Test contents of deaths list
    print(deaths)
    """
    
### Create GUI ###

fig, ax = matplotlib.pyplot.subplots()

# Set opening canvas with introductary text
root = tkinter.Tk()
root.geometry('400x400')
c = tkinter.Canvas(root, height=400, width =400, bg="white")
c.create_text(200,40,text='The Black Death hit London in 1665.\nSelect the options on the menu bar to find out more.')
c.pack()


#  Create model canvas
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# Create menu and commands to run functions
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Population graph", command=runpop)
model_menu.add_command(label="Rat population graph", command=runrat)
model_menu.add_command(label="Estimated deaths graph", command=rundeath)
model_menu.add_command(label="Show total deaths", command=total_deaths)
model_menu.add_command(label="Save deaths data as txt", command=maketxt)
model_menu.add_command(label="Exit", command=close_window)

timeit.timeit()
tkinter.mainloop()