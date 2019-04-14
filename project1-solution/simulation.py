
# library imports
import numpy as np
import matplotlib.pyplot as plt

# internal imports
from constants import (
    INITIAL_PROBABILITY, FINAL_PROBABILITY, PROBABILITY_INCREMENT, 
    NUM_SIMULATIONS, NUM_INPUTS, NUM_OUTPUTS
)

class Simulation:
    def __init__(self):
        self.results = {}
    
    def start(self):
        for p in np.arange(INITIAL_PROBABILITY, FINAL_PROBABILITY, PROBABILITY_INCREMENT):
            p = round(p, 2)

            passed = [0]*1000
            dropped = [0]*1000

            for sim in range(0, NUM_SIMULATIONS):
                result = np.random.binomial(size=NUM_INPUTS, n=1, p=p).tolist()
                num_packets = sum(result)

                passed[sim] = min(NUM_OUTPUTS, num_packets)
                dropped[sim] = num_packets - passed[sim]
            
            self.results[p] = { "passed": passed, "dropped": dropped }
    
    def graph(self):
        x_axis = list(self.results.keys()) # all p-values

        # calculate average number of busy ouputs per p-value
        y_axis1 = [sum(self.results[p]['passed']) / 1000 for p in x_axis]

        # calculate average number of dropped packets per p-value
        y_axis2 = [sum(self.results[p]['dropped']) / 1000 for p in x_axis]

        # graph #1
        plt.subplot(2, 1, 1) # prepare the first plot
        plt.plot(x_axis, y_axis1) # plot x-axis and y-axis points
        plt.xticks(np.array(x_axis)) # set x-ticks
        plt.ylabel('Average # of Busy Outputs') # label the x-axis
        plt.xlabel('Probability') # label the y-axis
        plt.title('Average # of Busy Outputs vs. Probability')  # title the graph

        # graph #2
        plt.subplot(2, 1, 2) # prepare the second plot
        plt.plot(x_axis, y_axis2) # plot x-axis and y-axis points
        plt.xticks(np.array(x_axis)) # set x-ticks
        plt.ylabel('Average # of Dropped Packets') # label the x-axis
        plt.xlabel('Probability') # label the y-axis
        plt.title('Average # of Dropped Packets vs. Probability')  # title the graph 

        # display the two graphs
        plt.show() 

def main():
    simulation = Simulation()
    simulation.start()
    simulation.graph()

if __name__ == "__main__":
    main()
