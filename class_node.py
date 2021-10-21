import pandas as pd

class Node:
    def __init__(self,town_name,cumulated_time,cumulated_distance,depth,visited_towns,parent_node):
        self.town_name = town_name
        self.destinations = []
        self.isdivisible = None
        self.cumulated_time = cumulated_time
        self.cumulated_distance = cumulated_distance
        self.depth = depth
        self.visited_towns = visited_towns
        self.nodes_sons = []
        self.parent_node = parent_node
        
    def is_divisible(self,max_depth,final_town):
        is_divisible = True
        if self.depth >= max_depth or self.town_name == final_town or self.destinations == []:
            is_divisible = False
        self.is_divisible = is_divisible
        return None
    
    def get_destinations(self,connections):
        df = connections.loc[self.town_name]
        if isinstance(df, pd.Series):
            if df['ville2'] not in self.visited_towns:
                self.destinations.append(df.values)
        else:
            for i in range(len(df)):
                if df['ville2'].iloc[i] not in self.visited_towns:
                    self.destinations.append(df.iloc[i].values)
        return None
    
    def is_leaf(self):
        if len(self.nodes_sons) == 0:
            return True
        else:
            return False
    
    def display_node(self,offset):
        string = f"{offset}Town: {self.town_name} \n{offset}Cumulated distance: {self.cumulated_distance} \n{offset}Cumulated time: {self.cumulated_time} \n{offset}Depth: {self.depth}"
        return string
