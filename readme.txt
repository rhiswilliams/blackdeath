CONTENTS LIST

- blackdeath.ipynb : Jupyter notebook version
- blackdeath.py : alternative Py version
- death.parishes : human population data
- death.rats : rat population data
- Previous Versions folder : 5 older versions of the project throughout its development


WHAT IS THE PROGRAM?

The program reads in data of rat populations recorded by rat catchers and population density derived from parish 
records. The data is recorded according to 100m x 100m squares of London. The program displays this data as
raster maps.

Using the equation d = (0.8 x r) x (1.3 x p), the program calculates the estimated number of deaths for each
square. The program displays this data as a raster map, displays the total sum of the estimated number of
deaths, and saves the data as a txt file in the current working directory. The 0.8 and 1.3 weightings can be
changed to different values through user input.

Potential uses for the program include:

- comparing numbers of people, rats and deaths in different areas of London.
- testing the equation d = (0.8 x r) x (1.3 x p) by comparing the results to historical data.
- investigating the impact of different equation weightings.


HOW TO RUN THE PROGRAM

- Open blackdeath.ipynb in Jupyter notebooks and run all cells.


WHAT TO EXPECT WHEN IT RUNS

When you run the program, a 'Model' window opens. Clicking the 'Model' button will open an options list. 
Click an option to run a function.

- 'Population graph' : displays a raster map of the human population data in a new window.
- 'Rat population graph' : displays a raster map of the rat population data in a new window.
- 'Estimated deaths graph' : a message window requests the user to input custom equation weightings for 
   rat and human populations, displaying default values of 0.8 and 1.3. When the weightings have been
   submitted, estimated numbers of deaths are calculated using the weightings and human and rat population
   data. The deaths data is displayed as a raster map.
- 'Show total deaths' : a message window requests the user to input custom equation weightings for 
   rat and human populations, displaying default values of 0.8 and 1.3. When the weightings have been
   submitted, the total estimated number of deaths is calculated using the weightings and human and rat 
   population data. The total figure is displayed in a message window.
- 'Save deaths data as txt' : a message window requests the user to input custom equation weightings for 
   rat and human populations, displaying default values of 0.8 and 1.3. When the weightings have been
   submitted, estimated numbers of deaths are calculated using the weightings and human and rat population
   data. The deaths data is saved as a txt file in the current working directory.
- 'Exit' : closes the program.


LICENCE INFORMATION

The program uses a GNU General Public License. Further information can be found by reading the LICENSE document
in this folder.

GITHUB

All files can be found at https://github.com/rhiswilliams/blackdeath