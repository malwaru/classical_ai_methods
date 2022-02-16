#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:28:19 2018

@author: iswariya
"""

import copy
import math
from heapq import *
from colorama import Fore,Back,Style
import random
import numpy as np
import os
import sys



## Define set of global variables

PUZZLE_TYPE = 8
ROW_SIZE = int(math.sqrt(PUZZLE_TYPE + 1))
max_row_size=2 ## Max row index allowed
max_col_size=2 ## Max col index allowed

# unicode for puzzle printing and define the style to print
left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'

middle_junction = '\u253C'
top_junction = '\u252C'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251C'
dash = '\u2500'
bar = Style.BRIGHT + Fore.CYAN + '\u2502' + Fore.RESET + Style.RESET_ALL
first_line = Style.BRIGHT + Fore.CYAN + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL
middle_line = Style.BRIGHT + Fore.CYAN + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL
last_line = Style.BRIGHT + Fore.CYAN + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL

##Define the format of  standard arrays
print_array_format = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

current_array = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

# invalid_state = [[9, 9, 9],
#                 [9, 9, 9],
#                 [9, 9, 9]]

invalid_state=('uerr','derr','lerr','rerr')



class Puzzle:
    """ Class for creating N puzzle game environment.
    This class has been implemented to provide a minimalistic
    game environment to you. Please try to avoid modifying this
    class unless absolutely necessary.
    """

    def __init__(self, init_state):
        """Class Construction for initializing the board
        NOTE: The 0 tile is the EMPTY tile that can be used
        for swapping.

        Parameters
        ----------
        init_state : list
            Initial position of the board obtained from user
        """
        for r,value in enumerate(init_state):
        
            if 0<=r<=2:
                current_array[0][1-(1-r)]=init_state[r]

            if 3<=r<=5:
                current_array[1][1-(4-r)]=init_state[r]
            if 6<=r<=8:
                current_array[2][1-(7-r)]=init_state[r] 
        self.initial_state = current_array
        # self.goal_state = [i for i in range(0, PUZZLE_TYPE + 1)]
        self.goal_state = [[0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8]]
        #Make this a tuple
        self.explored_states = ()
        self.path_to_goal={}

    def get_goal_state(self):
        """Class method to get the goal state of the board

        Returns
        -------
        list
            Configuration of board when goal state has been reached
        """

        return self.goal_state

    def get_initial_state(self):
        """Class method to get the initial state of the board

        Returns
        -------
        list
            Initial configuration of board during start of search
        """

        return self.initial_state

    def goal_test(self, node):
        """Class method to test if goal state is reached and 
        appends the particular board configuration to the list
        of explored states. Returns true if goal state is reached.

        Parameters
        ----------
        node : list
            Board configuration obtained from the search tree

        Returns
        -------
        boolean
            Returns true if the passed configuration is equal to
            goal configuration
        """
        current_node=copy.deepcopy(node)
        temp=list(self.explored_states)
        temp.append(current_node)
        self.explored_states=tuple(temp)
        # self.path_to_goal[ex]
                
        # self.explored_states.append(node)
        return current_node == self.goal_state

    def is_explored(self, node):
        """Class method to check if a particular board configuration
        has already been explored

        Parameters
        ----------
        node : list
            Board configuration obtained from the search tree

        Returns
        -------
        boolean
            Returns true if a particular configuration has already been explored
        """
        # print(f'explored {self.explored_states}')
        return node in self.explored_states

    def find_path_to_goal(self,initial_node):
   
        key_list=self.path_to_goal.keys()
        val_list=self.path_to_goal.values()
       
        
        
        back_track_puzzle=str([0,1,2],)
        
        n=0
        while back_track_puzzle != str(initial_node):
            print(n)
            
            print(back_track_puzzle) 
            key_pos=val_list.index(back_track_puzzle)
            back_track_puzzle=key_list[key_pos] 
            n+=1

    
def print_to_file(print_file):
    try:
        map_nos=len(print_file)
        working_directory = os.getcwd()
        
        result_directory = 'results'
        file_path = os.path.join(working_directory, result_directory + '/map1.txt')
        file_name='malike'
        f=open(file_path+file_name,'x') ##Open/Create a file to store data
        
        ##Join all the elements in the matrix together so that it can be printed on a textfile    
        for row_num,row_value in enumerate(print_file[0]):  
            current_line=''.join((print_file[0])[row_num])      
            f.write(current_line+'\n')

        f.close()   
    except :
        
        print("\n Maps already exist in results folder \n")
    

def print_puzzle(puzzle,flat):
    """Function to print the puzzle to console

    Parameters
    ----------
    puzzle : list
        8 puzzle configuration
    """

    # for idx, val in enumerate(puzzle):

    #     if (idx + 1) % ROW_SIZE == 0:     
    #         print("  ", val)
    #     else:
    #         print("  ", val, end="")
    print_array=copy.deepcopy(print_array_format)
    if flat:
        
        for r,value in enumerate(puzzle):
            
            if 0<=r<=2:
                print_array[0][1-(1-r)]=puzzle[r]

            if 3<=r<=5:
                print_array[1][1-(4-r)]=puzzle[r]
            if 6<=r<=8:
                print_array[2][1-(7-r)]=puzzle[r]
    
    ##see if this works
    else:
        print_array=puzzle

    for a in range(len(print_array)):
        for i in print_array[a]:
            if i == 0:
                print(bar, Back.RED + ' ' + Back.RESET, end=' ')
            else:
                print(bar, i, end=' ')
        print(bar)
        if a == 2:
            print(last_line)
        else:
            print(middle_line)


    


def move_left(position,node):
    """Function to move one position left in 8 puzzle if possible

    Parameters
    ----------
    position : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    left_node=copy.deepcopy(node)
    
    # print(f'left {left_node} \n')
    if (position[1]-1)>=0:


        try:        
            left_node[position[0]][position[1]]=left_node[position[0]][position[1]-1]
            left_node[position[0]][position[1]-1]=0
        except :
            left_node='lerr'
    else:
         left_node='lerr'

    

    return left_node


def move_right(position,node):
    """Function to move o,ne position right in 8 puzzle if possible

    Parameters
    ----------
    position : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    right_node=copy.deepcopy(node)
    
    # print(f'right {right_node} \n')

    if (position[1]+1)<=max_col_size:
        try:        
            right_node[position[0]][position[1]]=right_node[position[0]][position[1]+1]
            right_node[position[0]][position[1]+1]=0
        except :
            right_node='rerr'
    else: 
        right_node='rerr'

    

    return right_node


def move_up(position,node):
    """Function to move one position up in 8 puzzle if possible

    Parameters
    ----------
    position : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    up_node=copy.deepcopy(node)
    # print(f'Up {up_node} \n') 

    if (position[0]-1)>=0:
        try:        
            up_node[position[0]][position[1]]=up_node[position[0]-1][position[1]]
            up_node[position[0]-1][position[1]]=0
        except :
            up_node='uerr' 
    else:
        up_node='uerr'

      
    
    return up_node


def move_down(position,node):
    """Function to move one position down in 8 puzzle if possible

    Parameters
    ----------
    position : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    down_node=copy.deepcopy(node)
    
    # print(down_node[position[0]][position[1]])
    if (position[0]+1)<=max_row_size:
        try:        
            down_node[position[0]][position[1]]=down_node[position[0]+1][position[1]]
            down_node[position[0]+1][position[1]]=0
        except :
            down_node='derr' 
    else:
        down_node='derr'
    
    return down_node


def get_possible_moves(node, board):
    """Function to check whether a move is possible in left,
    right, up, down direction and store it.

    Parameters
    ----------
    node : [type]
        [description]
    board : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """

    possible_moves = []
    current_node=node

    # print(current_node)

    position=[10,10]
       
    #Check this
    for i in range(len(current_node)):
        try:
            position[1]=current_node[i].index(0) 
            position[0]=i
        except:
            pass
          


    # print(f'yawze{position}')
    # position=[position[0][0],position[1][0]]
    
    
    
    

    
    
    possible_moves.append(move_left(position,current_node))
    
    possible_moves.append(move_right(position,current_node))
    
    possible_moves.append(move_up(position,current_node))
    
    possible_moves.append(move_down(position,current_node))
   
   ## Find the indexes of the items to be removed
    items_to_remove=[]
    for x in range(len(possible_moves)):

        if (possible_moves[x] in invalid_state) or (Puzzle.is_explored(board,possible_moves[x])):
            items_to_remove.append(x)

    #Remove invalid items
    for item in sorted(items_to_remove,reverse=True):
        del possible_moves[item]

    #Adding path to current node
    # for moves in possible_moves:
    #     # Puzzle()
    #     print('setting')
        
        

    # print(f'possible after {possible_moves}\n')
    

      

   
    
    # HINT :
    # 1. Convert the list to a heap and push the possible moves
    # to the heap based on priority.
    # 2. Please note priority depends on your search algorithm
    # For Eg: A-star uses f_score as priority while greedy search
    # uses h_score as priority
    # print(f'possible after {possible_moves} \n\n')

    return possible_moves


# def no_of_misplaced_tiles(node,board):
#     """Function to get the number of misplaced tiles for a
#     particular configuration

#     Parameters
#     ----------
#     node : [type]
#         [description]

#     Return
#     ------
#     [type]
#         [description]
#     """
#     goal=Puzzle.get_goal_state(board)

#     current_node=copy.deepcopy(node)

#     misplaced_tiles_cost=sum(node!=goal)-1
#     return misplaced_tiles_cost if misplaced_tiles_cost>0 else 0


def misplaced_tile_heuristic(node, board):
    """Function to implement misplaced tiles heuristic in
    combination with no_of_misplaced_tiles() for each of
    the search algorithms

    Parameters
    ----------
    node : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """
    
    goal=copy.deepcopy(Puzzle.get_goal_state(board))
    current_node=copy.deepcopy(node)   

    current_node=np.array(current_node)
    goal=np.array(goal) 

    misplaced_tiles_cost=np.sum(current_node!=goal)   
    

    
    return misplaced_tiles_cost if misplaced_tiles_cost>0 else 0


# def get_manhattan_distance(node,board):
#     """Function to calculate the manhattan distance for a
#     particular configuration

#     Parameters
#     ----------
#     node : [type]
#         [description]

#     Return
#     ------
#     [type]
#         [description]
#     """

#     goal=Puzzle.get_goal_state(board)
    
    
  
    
#     a=abs(node//3-goal//3)
#     b=abs(node%3-goal%3)
    
    
#     manhattan_cost=a+b
#     print(f' man cost{manhattan_cost}')

    

#     return sum(manhattan_cost[1:])


def manhattan_distance_heuristic(node,board):
    """Function to implement manhattan distance heuristic in
    combination with get_manhattan_distance() for each of
    the search algorithms

    Parameters
    ----------
    node : [type]
        [description]

    Return
    ------
    [type]
        [description]
    """

    goal=copy.deepcopy(Puzzle.get_goal_state(board))
    current_node=copy.deepcopy(node)   

    current_node=np.array(current_node)
    goal=np.array(goal) 

    a=abs(np.subtract(current_node//3,goal//3))
    b=abs(np.subtract(current_node%3,goal%3))
    
    
    manhattan_cost=np.sum(np.add(a,b))


    return manhattan_cost
