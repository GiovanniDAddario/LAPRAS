import matplotlib.pyplot as plt
from Person import Person
from EnvironmentClass import Environment

class Simulation:
    def __init__(self,size,endtime,population,initial_infected):
        '''
        size : [xwidth,ywidth]
        '''
        self.size = size
        self.endtime = endtime
        self.time = 0 
        self.population = population
        self.infected = initial_infected
        self.dead = 0
        # Age distribution of population https://www.statista.com/statistics/281174/uk-population-by-age/
        self.age_dist =   {'yrs0-19': 0.2346032224,
                            'yrs20-44': 0.3241981629,
                            'yrs45-54': 0.1382321939,
                            'yrs55-64': 0.1198614666,
                            'yrs65-74': 0.1001355218,
                            'yrs75-84': 0.0588766752,
                            'yrs85plus':0.02409275711}

    def draw(self):
        fig = plt.figure()
        plt.xlim(-self.size[0],self.size[0])
        plt.ylim(-self.size[1],self.size[1])
        plt.show()

sim = Simulation([50, 50], 10, 100, 1)
sim.draw()