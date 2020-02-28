# Environmental Informatics

## Assignment 06 - Graphing Data with Python

### Lab Objectives

On completion of this lab, students will be able to:
1. Use NumPy arrays to more efficiently work with large tables of numbers; and
2. Create simple figures in Python using the MatPlotLib plotting library and MatLab like plotting syntax.

### Reading Assignment

1. Start with the brief introduction into the NumPy module found at [What is NumPy?](https://docs.scipy.org/doc/numpy/user/whatisnumpy.html).  
2. Then complete a tutorial on using the `matplotlib` module for 2-D plotting from Python.  There are multiple options for learning how to use pyplot to generate 2-D figures, here are two that I like:  

   1. The first, [the PyPlot Tutorial](http://matplotlib.org/users/pyplot_tutorial.html) is the tutorial created by the designers of matplotlib.  It is not as slick as some of the others out there, but it covers the basics and has plenty of links to follow, if you wat to do more. 

   2. The second [Matplotlib tutorial](http://www.loria.fr/~rougier/teaching/matplotlib/), now builds directly on the first but presents a few of the more advanced topics esriler and in a more relatable way.  It is also a GitHub repository, so all of the code and data they use is available, if you clone the reposity.

For this assignment, avoid any tutorials that make use of the `pandas` module, which includes all tutorials I have found using the `seaborn` module.  We will get there with the next assignment.

### The Lab Assignment

Clone this repository.  You are welcome to work through the tutorials in the repository directory, though I suggest that you make a subdirectory called "matplotlib_tutorial" or something similar so that the main folder structure remains clean.  You can leave everything related to the tutorial in this directory and push it to the repository to preserve it, or do the tutorial somewhere else as nothing from it is required for the assingment this week.

For this week's assignment, you will write a Python program to read in a data file (two have been provided) and generate summary figures for that file.  The Python program should then be rerun to process the second file.

The Python program should do the following (note the percentages below reflect the break-down of scoring within the "program running" category):

1. (10%) Open one of the files using the NumPy command genfromtxt() and use the first line as a header to define the name of arrays that are generated.  
   - An example of using the genfromtxt() command can be found [at this tutorial website](http://python-astro.blogspot.com/2012/02/read-ascii-file-cont.html), while 
   - details of the command and its options (including how to work with headers) can be found in the [SciPy documentation](http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html).

2. (10%) Use the matplotlib library to generate a single page with three plots.

   - (20%) The top plot should include the mean, maximum and minimum daily streamflow using lines of black, red, and blue, respectively.  The plot should also include a legend for the three lines.
   - (10%) The middle plot should use symbols to represent the annual values of Tqmean, multiplied by 100%.
   - (10%) The bottom plot should be a bar plot of R-B index.
   - (10%) The x-axis should be labeled with the values for years found in the input file.
   - (10%) The y-axis on each plot should be labeled for the appropriate variable type and units, which are:
     - "Streamflow (cfs)", 
     - "Tqmean (%)", and 
     - "R-B Index (ratio)"
   - (10%) Final output from this program should be written to a PDF file, see [this help page](http://stackoverflow.com/questions/9622163/matplotlib-save-plot-to-image-file-instead-of-displaying-it-so-can-be-used-in-b) for guidance.

3. (10%) Finally, your Python program should accept command line options to determine the input and output filenames so that the program can be rerun using the other data file as input and to generate a second PDF file.  

#### What to turn in

Push the repository with source code, and the output PDF files for grading.
