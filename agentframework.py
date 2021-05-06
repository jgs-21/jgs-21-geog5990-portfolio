# -*- coding: utf-8 -*-
"""
This agent class contains the agent's attributes and behaviours.

"""
import random


class Agent():
        
    def __init__(self, environment, agents, _y, _x, i):
        """
        Create the model parameters.

        Parameters
        ----------
        environment : list
            Environment for the agents.
        agents : list
            Agents for the model.
        y : integer
            Agents y coordinate.
        x : integer
            Agents x coordinate.
        i : integer
            Agents number (i.e. if there are 10 agents, i will range from 0-9).

        Returns
        -------
        None.

        """

        if (_y == None):
            self._y = random.randint(0,100)
        else:
            self._y = _y
        
        if (_x == None):
            self._x = random.randint(0,100)
        else:
            self._x = _x
        
        # Protect the self.x and self.y variables by implementing a property 
        # attribute with set and get methods 
        # (https://docs.python.org/3/library/functions.html#property)
        
        @property
        def y(self):
            """I'm the 'y' property."""
            return self._y
        
        @y.setter
        def y(self, value):
            self._y = value
        
        @y.deleter
        def y(self):
            del self._y
    
        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x
        
        @x.setter
        def x(self, value):
            self._x = value
    
        @x.deleter
        def delx(self):
            del self._x
        
        
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.i = i
        
    def __str__(self):
        """
        This provides information about the agents which can be used later in
        the code to determine which agents are sharing with each other.

        Returns
        -------
        String
            Returns a string displaying the agent number (i), the agent's x 
            and y coordinates, and the agent's store.

        """
        return ("i=" + str(self.i) + ", x=" + str(self._x) + ", y=" +
                str(self._y) + ", store=" + str(self.store))

    def move(self):   
        """
        This modifies the x and y variables for the agent increasing or 
        decreasing them pseudorandomly.

        Returns
        -------
        None.

        """
        if random.random()< 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
    
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
            
    def eat(self):
        """
        This tells the agents to eat the environment.

        Returns
        -------
        None.

        """
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighbourhood):
        """
        
        This method will calculate the distance from an agent to each of the 
        other agents, and if they fall within neighbourhood distance, it will 
        set the agent and its neighbours stores to the average of their two 
        stores. 

        Parameters
        ----------
        neighbourhood : integer
            The neighbourhood is the distance within which two
            agents will share resources.

        Returns
        -------
        None.

        """
        # Loop through the agents in self.agents .
        for agent in self.agents:
            # Calculate the distance between self and the current other agent:
            distance = self.distance_between(agent)
            # If distance is less than or equal to the neighbourhood
            if distance <= neighbourhood:
                # Sum self.store and agent.store.
                sum = self.store + agent.store
                # Divide sum by two to calculate average.
                average = sum / 2
                # self.store = average
                self.store = average
                # agent.store = average
                agent.store = average
                print(str(self) + " sharing with " + str(agent) + ": distance=" 
                      + str(distance) + ", average=" + str(average))
            
        
    def distance_between(self, a):
        """
        Distance between self and a.

        Parameters
        ----------
        a : agent
            The agent.

        Returns
        -------
        Float integer
            The distance between agents.

        """
        return (((self._x - a._x)**2) + 
             ((self._y - a._y)**2))**0.5