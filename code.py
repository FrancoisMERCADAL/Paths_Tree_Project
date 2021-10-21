from class_node import *

def open_towns_file(file_name):
    return pd.read_csv(file_name)['ville'].values

def open_connections_file(file_name):
    array = []
    file = pd.read_csv(file_name)
    file = file.set_index('ville1')
    for duree in file['duree']:
        split = duree.split(':')
        array.append(float(split[0])+round(float(split[1])/60,3))
    file['duree'] = array
    return file

def build_tree(current_node,arrival_town,max_depth,connections):
    current_node.get_destinations(connections)
    current_node.is_divisible(max_depth,arrival_town)
    if current_node.is_divisible == False:
        return None
    else:
        index = 0
        for destination in current_node.destinations:
            current_node.nodes_sons.append(Node(destination[0],
                                                current_node.cumulated_time + destination[2],
                                                current_node.cumulated_distance + destination[1],
                                                current_node.depth + 1,
                                                current_node.visited_towns + [destination[0]],
                                                current_node
                                               ))
            build_tree(current_node.nodes_sons[index],arrival_town,max_depth,connections)
            index += 1
            
def display_tree(root_node):
    offset = '   ' * root_node.depth
    print(root_node.display_node(offset))
    if root_node.is_leaf() == False:
        for node in root_node.nodes_sons:
            display_tree(node)
    return None

def get_leaves(root_node):
    return None

def display_1_way(root_node):
    return None

def main():
    menu_selection = -1
    towns_names_file = 'villes.csv'
    connections_file = 'connexions.csv'
    towns = open_towns_file(towns_names_file)
    connections = open_connections_file(connections_file)

    start_town = input('Select a start town: ')
    arrival_town = input('Select a destination town: ')
    max_depth = int(input('Enter a max depth for the tree: '))

    root_node = Node(start_town,0,0,0,[start_town],None)
    build_tree(root_node,arrival_town,max_depth,connections)

    print('\nMenu: \n1- display a way \n2- display all ways \n3- display the shortest way \n4- display the fastest way \n5- display the tree \n6- Leave program \n')
    while menu_selection != 6:
        menu_selection = input('Select a menu option: ')
        if menu_selection == '1':
            print('To Do')
        elif menu_selection == '2':
            print('To Do')
        elif menu_selection == '3':
            print('To Do')
        elif menu_selection == '4':
            print('To Do')
        elif menu_selection == '5':
            display_tree(root_node)
        else:
            print('Leaving the program')
    return None

main()
