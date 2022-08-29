import heapq
import math
from os import stat

class Agent:
    def __init__(self, start_state, end_state):
        self.start_state = start_state
        self.goal_state = end_state
        self.visited = list()

    def find_optimal_path(self, env):
        current_state = self.start_state
        
        self.visited.append(current_state)

        env.nodes[current_state] = (env.nodes[current_state][0], env.nodes[current_state][0])

        while(current_state != self.goal_state):
            current_state = self.interact_with_env(env, current_state)
            # print("Current State", current_state)
            # print("Visited", self.visited)
            self.visited.append(current_state)

    def interact_with_env(self, env, current_state):
        next_states = env.adjacency_list[current_state]

        #Update cost of travelling to next available nodes and their parent nodes
        costs = []
        next_unvisited_states = []
        for state in next_states:
            if not state in self.visited:
                next_unvisited_states.append(state)
                cost = env.nodes[current_state][1] + env.nodes[state][0]
            
                #If the calculated cost is lesser then previous cost update cost and parent node
                if(env.nodes[state][1] > cost):
                    env.nodes[state] = (env.nodes[state][0], cost)
                    env.nodes_last_node[state] = current_state
                    env.frontier.append((cost, state))
                costs.append(cost)

        # print("Self.visited in interact with env", self.visited)
        # print("Next Unvisited States", next_unvisited_states)
        # print("Costs", costs)
        
        heapq.heapify(env.frontier)

        next_state = None

        _, next_state = heapq.heappop(env.frontier)

        # print("Frontier", env.frontier)
        
        return next_state

class Environment:
    def __init__(self, nodes, adjacency_list):
        self.adjacency_list = adjacency_list
        self.nodes = nodes
        self.nodes_last_node = dict()
        self.frontier = list()

        #Stores the cost to reach given node from source and the its previous node
        #Eg.
        #{
        #   node1: (distance/cost from source, previous node)   
        #}
        for key in self.nodes.keys():
            self.nodes_last_node[key] = tuple()

def main():

    infinity = math.inf
    
    #Node cost will be calculated by some function
    nodes = {
        '-8.177083333333329-49.78125': (3878, infinity),
        '-8.177083333333329-49.78541666666666': (3883, infinity),
        '-8.181250000000006-49.78125': (3862, infinity),
        '-8.181250000000006-49.78541666666666': (3866, infinity),
        '-8.185416666666669-49.78125': (3847, infinity),
        '-8.185416666666669-49.78541666666666': (3850, infinity),
        '-8.189583333333331-49.78125': (3832, infinity),
        '-8.189583333333331-49.78541666666666': (3836, infinity)
    }

    adjacency_list = {
        '-8.177083333333329-49.78125': [
            '-8.181250000000006-49.78125',
            '-8.181250000000006-49.78541666666666',
            '-8.177083333333329-49.78541666666666'
        ],
        '-8.177083333333329-49.78541666666666': [
            '-8.181250000000006-49.78541666666666',
            '-8.181250000000006-49.78125',
            '-8.177083333333329-49.78125'
        ],
        '-8.181250000000006-49.78125': [
            '-8.185416666666669-49.78125',
            '-8.185416666666669-49.78541666666666',
            '-8.177083333333329-49.78125',
            '-8.177083333333329-49.78541666666666',
            '-8.181250000000006-49.78541666666666'
        ],
        '-8.181250000000006-49.78541666666666': [
            '-8.185416666666669-49.78541666666666',
            '-8.185416666666669-49.78125',
            '-8.177083333333329-49.78541666666666',
            '-8.177083333333329-49.78125',
            '-8.181250000000006-49.78125'
        ],
        '-8.185416666666669-49.78125': [
            '-8.189583333333331-49.78125',
            '-8.189583333333331-49.78541666666666',
            '-8.181250000000006-49.78125',
            '-8.181250000000006-49.78541666666666',
            '-8.185416666666669-49.78541666666666'
        ],
        '-8.185416666666669-49.78541666666666': [
            '-8.189583333333331-49.78541666666666',
            '-8.189583333333331-49.78125',
            '-8.181250000000006-49.78541666666666',
            '-8.181250000000006-49.78125',
            '-8.185416666666669-49.78125'
        ],
        '-8.189583333333331-49.78125': [
            '-8.185416666666669-49.78125',
            '-8.185416666666669-49.78541666666666',
            '-8.189583333333331-49.78541666666666'
        ],
        '-8.189583333333331-49.78541666666666': [
            '-8.185416666666669-49.78541666666666',
            '-8.185416666666669-49.78125',
            '-8.189583333333331-49.78125'
        ]
    }

    env = Environment(nodes, adjacency_list)

    agent = Agent("-8.177083333333329-49.78125", "-8.189583333333331-49.78541666666666")

    agent.find_optimal_path(env)

    print(env.nodes)

    print(env.nodes_last_node)

    path = list()
    current_state = agent.goal_state
    while(True):
        path.append(current_state)
        if(current_state == agent.start_state):
            break
        current_state = env.nodes_last_node[current_state]
    print()
    print("path", path)

if __name__ == "__main__":
    main()

