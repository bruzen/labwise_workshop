import random
from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector

class Agent(Agent):
    '''
    Schelling agent class
    '''
    def __init__(self, model, pos, type):
        '''
         Initialize the agent

         Args:
            model:     Instance of the Schelling abm model class.
            pos:       Agent's initial unique position on the grid, a tuple (x,y).
            type:      Agents may belong to type 1 or type 2.
        '''
        super().__init__(pos, model) # Initial position is agent's unique_id
        self.pos  = pos
        self.type = type

    def step(self):
        '''
         Step function for each agent occurs in each timestep
        '''    	
        # Count nearest neighbours like me
        neighbors_like_me = 0
        for n in self.model.grid.neighbor_iter(self.pos):
            if n.type == self.type:
                neighbors_like_me += 1

        # Move if fewer neighbors like me than threshold for happiness
        if neighbors_like_me < self.model.threshold:
            self.model.grid.move_to_empty(self)
        else:
            self.model.no_happy_this_timestep += 1        

class SchellingModel(Model):
    '''
    Schelling model class
    '''
    def __init__(self, width=5, height=5, threshold=0.5, population_density=0.8, population_breakdown=0.5):
        '''
         Initialize the model

         Args:
            width:     Width  of the grid containing agents.
            height:    Height of the grid containing agents.
            threshold: Homophily threshold, the number, from 0-8, of nearest neighbours at which I am so unhappy that I move.
        	population_density:   Proportion of cells occupied, from 0-1.
        	population_breakdown: Proportion of agents of type 1, from 0-1.
        '''        
        self.running   = True

        self.height    = height
        self.width     = width
        self.threshold = threshold
        self.population_density     = population_density
        self.population_breakdown   = population_breakdown
        self.no_happy_this_timestep = 0
        self.schedule  = RandomActivation(self)
        self.grid      = SingleGrid(width, height, torus=True)
        
        self.datacollector = DataCollector(
            {"happy": lambda m: m.no_happy_this_timestep},
            {"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]})
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if random.random() < self.population_density:
                if random.random() < self.population_breakdown:
                    agent_type = 1
                else:
                    agent_type = 0
                agent = Agent(self,(x, y), agent_type)
                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)

    def step(self):
        '''
        Update model once in each time step
        '''
        self.no_happy_this_timestep = 0
        self.schedule.step()
        self.datacollector.collect(self)

        # End the simulation if all agents are happy since none will move
        if self.no_happy_this_timestep == self.schedule.get_agent_count():
            self.running = False