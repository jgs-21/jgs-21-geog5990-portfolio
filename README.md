# jgs-21-geog5990-portfolio
This repository is a portfolio for the python code I have created during the University of Leeds' Programming for Geographical Information Analysis module as part of my GIS MSc.

The source code in this repository creates an agent-based model which:
- builds agents in a space;
- gets the agents to interact with each other;
- reads in environmental data;
- gets the agents to interact with the environment;
- randomizes the order of agent actions (to reduce model artifacts);
- displays the model as an animation;
- is contained within a GUI;
- is initialised with data from the web.

####**REPOSITORY CONTENTS:**
- model.py (found in the source_code directory) - this file is the main model containing the code for the agent-based model.
- agentframework.py (found in the source_code directory) - this file is a module containing the agents attributes and behaviours which is imported into the main model.py.
- in.txt (found in the source_code directory) - this text file is the environmental raster data for the main model.py.
- model_doc.html (found in the documentation directory) - this html file was generated by PyDoc to produce documentation for the main model.py.
- agentframework_doc.html (found in the documentation directory) - this html file was generated by PyDoc to produce documentation for the agentframework.py.


####**HOW TO RUN:**
- The model.py can be run the command line and needs four argument values, for example, at the command line: **python model.py 10 10 100 20**
- The model.py can also be run in spyder whereby the command line options need to be set in the configuration per file prior to running (run --> configuration per file
--> set command line options) (alternatively, Ctrl+F6 --> set command line options)
- The four arguments to be set at the command line are:
    - num_of_agents (this is an integer value to set the number of agents)
    - num_of_steps (this is an integer value to set the number of steps for the model)
    - num_of_iterations (this is an integer value to set the number of iterations for the model)
    - neighbourhood (this is an integer value to set the neighbourhood for the model)
    
- Note: the parameter variables have been left in the code commented out if one wants to set the values in the script instead of at the command line


What to expect when the programme is run:
- After the parameters have been set at the command line, a pop-up window containing a GUI will appear. 'Model' should be selected from the menu bar, then 
'run model' should then be selected from the drop-down menu to run the code to produce the model.
- A figure will appear showing an environment with agents moving around the environment and eating the environment.


Testing:
- Print statements have been used throughout the code to ensure the code is performing in the intended way.


Further development:
- For further development of the model, the agents could be given more behaviours to enhance their interaction with their environment.
