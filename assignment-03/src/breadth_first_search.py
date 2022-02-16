#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template Created on Fri Apr 27 21:15:04 2018
Final    Created on Sat Nov 28          2020

@author of final code: Malika Navaratna
@author of template: Iswariya Manivannan

"""
import sys
import os
from collections import deque
from helper import maze_map_to_tree, write_to_file, assign_character_for_nodes,find_valid_neighbours

def find_route(goal_x,goal_y,start_x,start_y,solution,maze_map):
    """
    This function backtracks the path taken to goal poisition by iterativeley searching the dictionary of solutions

    Parameters
    ----------
    goal_x : int
        X coordinate of the goal
    goal_y : int
        Y coordinate of the goal
    start_x : int
        X coordinate of the start position
    start_y : int
        Y coordinate of the start position
    solution: dictionary
        A dictionary containing the way nodes were expanded
    maze_map: list
        The nested list of the maze

    

    Returns
    -------
    [list]
        [Returns a maze map with 'X's marking the traversed paths to all the goals]
 
    
    
    """


    x=goal_x
    y=goal_y
    write_map=maze_map
    while (x, y) != (start_x, start_y):    
        write_map[x][y]='x'

        if(x==goal_x and y==goal_y):## Make sure the goal positon is not overwritten
            write_map[x][y]='*'
        x, y = solution[x,y]      




    return write_map

def breadth_first_search(maze_map, start_pos, goal_pos):
    """Function to implement the BFS algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    maze_map : Nested List
            A graph of all the elements in the map
    start_pos : [list]
        [list of ints containing the starting position of the maze maked by 's']
    goal_pos : [list]
        [list of ints containing the goals of the maze maked by '*']

    Returns
    -------
    [list]
        [returns a list with traversed paths to goals using breath first search ]
    """


    blocked_path=['=','|'] ## Define that the symbols in this list means that the path is blocked
    queue = deque()        ##Initiate queue
    solution={}            ## Stores the way the nodes were expanded
      
    visited=set()          ## Stores the visited nodes
    
    max_row=len(maze_map)
    max_col=len(maze_map[0])

    ##Intialise variables
    goal_found=False
    start_pos=start_pos_map1 
    queue.append(start_pos) ## Initate the Queue with the starting postion 
    solution[(start_pos[0],start_pos[1])]=start_pos[0],start_pos[1] ## Initiate the dictionary item of node expansion
    printed_path=[] ##Initiat the final path of all traversed paths to goals
    


    



    while len(queue)>=1:

        

        x,y=queue.popleft() # Usinng FIFO to choose node
        
        
        neighbours=[]       # Initiate the neighbours 
    



        #UP
        if (x-1)>0: # Check if its hitting the upper boundary
            if (maze_map[x-1][y]) not in blocked_path and (x-1,y) not in visited:
                cell=(x-1,y)
                queue.append(cell)
                neighbours.append(cell)
                solution[cell]=x,y
                visited.add((x-1,y))
            
        #Down 
        if (x+1)<max_row: # Check if its hitting the lower boundary
            if ((maze_map[x+1][y]) not in blocked_path) and ((x+1,y) not in visited):
                cell=(x+1,y)
                queue.append(cell)
                neighbours.append(cell)        
                solution[cell]=x,y
                visited.add((x+1,y))
            
        #Left
        if (y-1)>0: # Check if its hitting the left boundary
            if ((maze_map[x][y-1]) not in blocked_path) and ((x,y-1) not in visited):
                cell=(x,y-1)
                queue.append(cell)
                neighbours.append(cell)
                solution[cell]=x,y
                visited.add((x,y-1))

        #Right
        if (y+1)<max_col: # Check if its hitting the lower boundary
            if ((maze_map[x][y+1]) not in blocked_path) and ((x,y+1) not in visited):
                cell=(x,y+1)
                queue.append(cell)
                neighbours.append(cell)
                solution[cell]=x,y
                visited.add((x,y+1))
            
    
            
        #Check for goal
        for neighbour in neighbours:
                
            character_in_node=maze_map[neighbour[0]][neighbour[1]]
            
            if character_in_node=="*":
                goal_found=True
                print(f'Goal is found {neighbour}')
                #Find the path taken to reach current goal and append it to a list
                currentPath=find_route(neighbour[0],neighbour[1],start_pos[0],start_pos[1],solution,maze_map)
                # print(currentPath)
                # print('\n \n \n \n')
                printed_path.append(currentPath)
                
                
            

        
            
            
            


    
        
    
    return printed_path


if __name__ == '__main__':

    

    working_directory = os.getcwd()

    if len(sys.argv) > 1:
        map_directory = sys.argv[1]
    else:
        map_directory = 'maps'

    file_path_map1 = os.path.join(working_directory, map_directory + '/map1.txt')
    file_path_map2 = os.path.join(working_directory, map_directory + '/map2.txt')
    file_path_map3 = os.path.join(working_directory, map_directory + '/map3.txt')

    maze_map_map1 = []
    with open(file_path_map1) as f1:
        maze_map_map1 = f1.readlines()

    maze_map_map2 = []
    with open(file_path_map2) as f2:
        maze_map_map2 = f2.readlines()

    maze_map_map3 = []
    with open(file_path_map3) as f3:
        maze_map_map3 = f3.readlines()
    
    
    
    maze_matrix1,start_pos_map1,goal_pos_map1=maze_map_to_tree(maze_map_map1)
    maze_matrix2,start_pos_map2,goal_pos_map2=maze_map_to_tree(maze_map_map2)
    maze_matrix3,start_pos_map3,goal_pos_map3=maze_map_to_tree(maze_map_map3)

    
    # CALL THESE FUNCTIONS after filling in the necessary implementations
    # for i in range(len(maze_matrix1)):
    #     print(f'{maze_matrix1[i]} \n')
    result_directory='results'    
    file_path_result = os.path.join(working_directory,result_directory+'/')

    path_map1 = breadth_first_search(maze_matrix1, start_pos_map1, goal_pos_map1)
    write_to_file("bfs_map1",path_map1,file_path_result)

    path_map2 = breadth_first_search(maze_matrix2, start_pos_map2, goal_pos_map2)
    write_to_file("bfs_map2",path_map2,file_path_result)

    path_map3 = breadth_first_search(maze_matrix3, start_pos_map3, goal_pos_map3)
    write_to_file("bfs_map3",path_map3,file_path_result)

    print("\n All maps printed to results folder \n")
    
 

#############
# References 
#############

# [1]https://www.youtube.com/watch?v=W9F8fDQj7Ok&t=231s
# [2]https://www.youtube.com/watch?v=KiCBXu4P-2Y
# [3]https://www.youtube.com/watch?v=oDqjPvD54Ss
# [4]https://www.youtube.com/watch?v=hettiSrJjM4&t=21s
# [5]https://www.codespeedy.com/breadth-first-search-algorithm-in-python/
# [6]https://www.youtube.com/watch?v=ZuHW4fS60pc&feature=youtu.be