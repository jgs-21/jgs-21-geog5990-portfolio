# -*- coding: utf-8 -*-
"""
Agent-Based Modelling

This agent-based model:
    - builds agents in a space;
    - gets the agents to interact with each other;
    - reads in environmental data;
    - gets agents to interact with the environment;
    - randomizes the order of agent actions;
    - displays the model as an animation;
    - is contained within a GUI;
    - is initialised with data from the web.

"""

# Import modules
import matplotlib
matplotlib.use('TkAgg')
import tkinter
import random
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import requests
import bs4
import time
import argparse

# Set the model parameters at the command line:
# Set the model up to read the parameters from the command line
# The following code to set parameters at the command line is altered from that at
# https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1
parser = argparse.ArgumentParser(description='Agent-Based Modelling')
parser.add_argument("num_of_agents", default = 10, type=int, 
                    help="This is an integer to set the number of agents")
parser.add_argument("num_of_steps", default = 10, type=int, 
                    help="This is an integer to set the number of steps for the model")
parser.add_argument("num_of_iterations", default = 100, type=int, 
                    help="This is an integer to set the number of iterations for the model")
parser.add_argument("neighbourhood", default = 20, type=int, 
                    help="This is an integer to set the neighbourhood for the model")

args = parser.parse_args()
num_of_agents = args.num_of_agents
num_of_steps = args.num_of_steps
num_of_iterations = args.num_of_iterations
neighbourhood = args.neighbourhood
print(num_of_agents, num_of_steps, num_of_iterations, neighbourhood)


# Time how long the code takes to run
start = time.process_time()


# Set the model parameters:
# Number of agents
#num_of_agents = 10
# Number of steps
#num_of_steps = 10
# Number of iterations
#num_of_iterations = 100
# Neighbourhood
#neighbourhood = 20

# The seed method initialises the random number generator so that the same 
# random numbers are produced.
seed = 1
random.seed(seed)


# Initialise with data from the web (web scraping):

# Issue a HTTP request
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
# Get the webpage
content = r.text
# Use beautifulsoup to process the webpage
soup = bs4.BeautifulSoup(content, 'html.parser')
# Get elements by their y x attributes
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# Check the data
#print(td_ys)
#print(td_xs)


# Set up the pop-up figure window:

# Create a figure for the plot
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])

# Create the figure window
root = tkinter.Tk() # build the main window
root.wm_title("Model") # set the title
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


# Display the model as an animation:
    
animation = 0

def run():
    """
    This function runs the model animation.

    Returns
    -------
    None.

    """
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, 
                                    frames=gen_function, repeat=False)
    canvas.draw()
    
    # The following two lines of code create a gif of the animated model to 
    # be used on a website
    #writer = matplotlib.animation.PillowWriter(fps=3)  
    #animation.save("abm.gif", writer=writer)


# Create the GUI:

# Make a menu and assosciate the menu with the function run
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
# When the menu is clicked the run function will run the animated model
model_menu.add_command(label="Run model", command=run) 


# Read in the environmental data:

# Load in the data for the environment from the text file which contains 
# raster data where each value is the equivalent to a pixel in an image, 
# arranged in a grid.
f = open('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

# As the data is being read in, add the data into a 2D list (environment).

# Create the empty lists (containers for the data) before any data is processed
environment = [] #  # list (container) for the environment
agents = [] # list (container) for the agents

# Read each row in the data being loaded
for row in reader:
    # Create an empty list for the data to be added to
    rowlist = []
    # Before each row is processed, for each value in the row, add the value
    # to the empty list (rowlist)
    for values in row:
        # Add the values to the empty list (rowlist).
        rowlist.append(values)
    # After the row is processed, add the data to the environment
    environment.append(rowlist)
      
# Close the file after all the data is processed
f.close()


# Check the agents
def print_agents():
    """
    This function prints out all of the agents to check the code is working.

    Returns
    -------
    None.

    """
    for i in range(num_of_agents):
        print(agents[i])
        

# Build agents in a space:
    
# Make the agents.
for i in range(num_of_agents):
    _y = int(td_ys[i].text)
    #print["y",y] # check the data
    _x = int(td_xs[i].text)
    #print["x",x] # check the data
    agents.append(agentframework.Agent(environment, agents, _y, _x, i))


# Check the agents before they interact with their environment
print("Before moving, eating, and sharing with neighbourhood:")
print_agents()


carry_on = True


def update(frame_number):
    """
    This function:
        - runs the code to make the agents interact with each other and their 
        environment;
        - cretaes a stopping condition to stop the model when a condition is 
        met, in this instance the stopping condition is the agent's store;
        - plots the data in a graph.

    Returns
    -------
    None.

    """
    fig.clear()
    global carry_on

    
    # Get the agents to interact with each other and their environment:
    for j in range(num_of_steps):
        # Print step number
        print("Step: ", j)
        # Randomize the order of agent actions: randomly shuffle the agents to 
        # randomise the order in which the agents are processed at each 
        # iteration to reduce model artifacts.
        random.shuffle(agents)
        for i in range(num_of_agents):
            random.shuffle(agents)
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            
            # Write out the store as a text file
            #print("Step: ", j, " ", agents[i], sep='', end='\n', flush=False, 
            #      file=open("store.txt", "a"))
    
    
    # Create stopping condition for the model - the model will stop running 
    # when the condition is met
    
    # Stop when all agent stores are greater than the limit
    limit = 1000
    count = 0
    # For each agent, if their store is greater than the limit, the count 
    # will increase by one
    for i in range(num_of_agents):
        if agents[i].store > limit:
            count = count + 1
    # If the count reaches the same number as the number of agents, meaning all
    # agents stores have exceeded the limit, the model will stop
    if (count == num_of_agents):
        carry_on = False
        print("Stopping Condition")
    
    
    # Check the agents after they have interacted with their environment
    print("After moving, eating, and sharing with neighbourhood:")
    print_agents()  
    
    
    # Time how long the code takes to run
    end = time.process_time()
    print("Time taken = " + str(end - start))

   
    # Plot data in a graph
    matplotlib.pyplot.ylim(0, 100)
    matplotlib.pyplot.xlim(0, 100)
    # Show the environment
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
        # Check the agents
        #print(agents[i]._x,agents[i]._y)

def gen_function(b = [0]):
    """
    This function returns an object (iterator) which we can iterate over 
    (one value at a time).

    """
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a	 # returns control and waits next call
        a = a + 1


# Calculate distance
#for agents_row_a in agents:
    #for agents_row_b in agents:
        #distance = agents_row_a.distance_between(agents_row_b)
        #print(distance)


# Function to stop the console from continuously running the code
def exiting():
    """
    This function stops the console from running the code.

    Returns
    -------
    None.

    """
    root.quit()
    root.destroy()

# Stop running the code when the pop-up window is closed
root.protocol('WM_DELETE_WINDOW',exiting)

# Set the GUI waiting for events
tkinter.mainloop()


# Write out the environment as a text file
#print(environment, sep='', end='\n', flush=False, file=open("environment.txt", "a"))
