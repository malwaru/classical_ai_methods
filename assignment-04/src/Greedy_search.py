#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 19:12:09 2018

@author: iswariya
"""

import sys
import timeit
from copy import deepcopy
import heapq
import helper

##Global variables
path_to_solution={}
goal_node_format=[[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def find_path_to_goal(initial_node,root_goal_node):
   
    key_list=list(path_to_solution.keys())
    val_list=list(path_to_solution.values())
    print(val_list)
    
    # print(goal_node_format)
    back_track_puzzle=str(root_goal_node)
    
    n=0
    while back_track_puzzle != str(initial_node):
        print(n)
        
        print(back_track_puzzle) 
        key_pos=val_list.index(back_track_puzzle)
        back_track_puzzle=key_list[key_pos] 
        n+=1
    
                 
            
                

            
   
          





def Greedy_search(board, opt):
    """Function to implement the Greedy search algorithm.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    board : [type]
        [description]
    opt : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """

    priority_queue = []
    h_score = 0  # heuristic function value
    

    # Creating a heap from list to store the nodes with the priority h_score
    heapq.heappush(priority_queue, (h_score, board.get_initial_state()))

    goal_check=board.goal_test(priority_queue[0][1])


    temp_key=str(deepcopy(priority_queue[0][1])) 
    # path_to_solution[temp_key]=temp_key
    board.path_to_goal[temp_key]=temp_key
    

   
    
    ## Iterator limit
    n=0
    
    
    while (len(priority_queue)>0) and n<5 and not(goal_check):
        
        current_node=(heapq.heappop(priority_queue)) 
        # helper.print_puzzle(current_node[1],False) 
        # print('\n')      
        
        nodes=helper.get_possible_moves(current_node[1],board)

        ##Used for the path dictionary key
        temp_key=str(deepcopy(current_node[1]))
        

        for node in nodes:
            
            if opt==1:
                h_score=helper.manhattan_distance_heuristic(node,board)

            if opt==2:
                h_score=helper.misplaced_tile_heuristic(node,board)       
                     

            
            heapq.heappush(priority_queue,(h_score,node))

                        
            temp_element=str(deepcopy(node))
            # path_to_solution[temp_key]=temp_element
            board.path_to_goal[temp_key]=temp_element

            
            

            goal_check=board.goal_test(node)
            if goal_check:
                
                print(f'found it in {n} iterations')
                # find_path_to_goal(board.get_initial_state(),current_node[1])
                helper.print_puzzle(node,False)
                
                break
              
                
                
                
                
                
            
                

                

                           
        

        n+=1
    print(board.path_to_goal)
    return None


if __name__ == '__main__':       
    # puzzle_8 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
    # puzzle_8 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
    puzzle_8 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing

    print("Initial Configuration")
    board = helper.Puzzle(puzzle_8)
    helper.print_puzzle(puzzle_8,True)
    opt = int(sys.argv[1])
    
    if opt == 1 or opt == 2:

        if opt ==1:
            print("\nRunning Greedy search with Manhattan Dist heuristic\n")
        else:
            print("\nRunning Greedy search with Misplaced Tiles heuristic\n")

        start_time = timeit.default_timer()
        Greedy_search(board, opt)
        end_time = timeit.default_timer()
        print('Time: {}s'.format(end_time-start_time))
    else:
        print("Invalid Choice")
