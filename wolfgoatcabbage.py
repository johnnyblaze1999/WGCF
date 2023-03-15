from search import *

class WolfGoatCabbage(Problem):
    
    def __init__(self,initial=frozenset({'F', 'W', 'G', 'C'}), goal=set()):
        super().__init__(initial, goal)
        

    def actions(self, state):
        action = list()
        
        if state == self.initial:
            action.append({'G', 'F'})
            return action
        if state == {'W', 'C'}:
            action.append({'F'})
            return action
        if state == {'W', 'C', 'F'}:
            action.append({'C', 'F'})
            action.append({'W', 'F'})
            return action
        if state == {'C'}:
            action.append({'G', 'F'})
        if state == {'W'}:
            action.append({'G', 'F'})
            action.append({'C', 'F'})
            return action
        if state == {'W', 'G', 'F'}:
            action.append({'W', 'F'})
            return action
        if state == {'G'}:
            action.append({'F'})
            return action
        if state == {'G', 'F'}:
            action.append({'G', 'F'})
            return action
        if state == {'C', 'G', 'F'}:
            action.append({'C', 'F'})
            return action
        return action
        
    def result(self, state, action):
        # Farmer is crossing
        if action.issubset(state):
            return state - action
        else:
            return state | action

    def goal_test(self, state):
        return state == self.goal
        


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)