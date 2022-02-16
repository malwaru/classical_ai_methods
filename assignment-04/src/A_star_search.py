#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:39:47 2018

@author: iswariya
"""

import sys
import timeit

import heapq
import helper



def Astar_search(board, opt):
    """Function to implement the A-star search algorithm.
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
    
    f_score = 0  # evaluation function value
    g_score = 0  # cost function value
    h_score = 0  # heuristic function value

    # Creating a heap from list to store the nodes with the priority h_score
    heapq.heappush(priority_queue,(f_score, g_score, h_score, board.get_initial_state()))
    goal_check=board.goal_test(priority_queue[0][1])

    #Starting Iterator
    n=0
    while (len(priority_queue)>0) and not(goal_check):
        
        current_node=(heapq.heappop(priority_queue))     
        helper.print_puzzle(current_node[3],False)
        print('\n')
        
        nodes=helper.get_possible_moves(current_node[3],board)

        
        
        

        for node in nodes:
            
            goal_check=board.goal_test(node)
            if goal_check:
                
                helper.print_puzzle(node,False)
                print(f'found it in {n} iterations')
                break

            if opt==1:
                h_score=helper.manhattan_distance_heuristic(node,board)

            if opt==2:
                h_score=helper.misplaced_tile_heuristic(node,board)
            g_score=current_node[1]+1
            f_score=h_score+g_score
            

            

            
            heapq.heappush(priority_queue,(f_score,g_score,h_score,node))

                
        

        n+=1
    
    
    # FILL IN YOUR CODE HERE

    return None


if __name__ == '__main__':       
    puzzle_8 = [0, 1, 2, 3, 4, 5, 8, 6, 7] # Initial Configuration for testing
    # puzzle_8 = [8, 7, 6, 5, 1, 4, 2, 0, 3] # Second Configuration for testing
    # puzzle_8 = [1, 5, 7, 3, 6, 2, 0, 4, 8] # Final Configuration for testing

    print("Initial Configuration")
    board = helper.Puzzle(puzzle_8)
    helper.print_puzzle(puzzle_8,True)
    opt = int(sys.argv[1])

    if opt == 1 or opt == 2:

        if opt ==1:
            print("\nRunning A star search with Manhattan Dist heuristic\n")
        else:
            print("\nRunning A star search with Misplaced Tiles heuristic\n")

        start_time = timeit.default_timer()
        Astar_search(board, opt)
        end_time = timeit.default_timer()
        print('Time: {}s'.format(end_time-start_time))
    else:
        print("Invalid Choice")
