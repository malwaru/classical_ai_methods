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
import time
blocked_path=['=','|']

def maze_map_to_tree(maze_map):
    """Function to create a tree from the map file. The idea is
    to check for the possible movements from each position on the
    map and encode it in a data structure like list.

    Parameters
    ----------
    maze_map : [type]
        [description]

    Returns
    -------
    [list]
        [Returns a list with each position as an element of a list]
    """
    rows_in_map=len(maze_map)
    
    cols_in_map=len(maze_map[0])
    map_matrix = [[] for _ in range(rows_in_map)] ## Creat a nested list to store elements of maze_map into a matrix format that is
                                                 ## easy to work with

    
    ##Adding each element in the map to indiviual elements so that they can be called by their position in the list
    for row_num,row_value in enumerate(maze_map):
        for i in range(len(row_value)):
            if (row_value[i]!="\n" and row_value[i]!=", ") :
                map_matrix[row_num].append(row_value[i])

    
    ##Search for the start position and storing its coordinates
    for i in range(len(map_matrix)):
        try:
            start_pos=[i,map_matrix[i].index('s')]
        except:
            pass
    

    ##Search for the goal position and storing its coordinates      
    goal_pos=[] # List to store multiple goals

    for j in range(len(map_matrix)):
        
        ## Try catch block to avoid errors caused if the index is not found
        try:
            goal_pos.append([j,map_matrix[j].index('*')])
            
        except:
            pass
            
    
   
 
    
    return map_matrix,start_pos,goal_pos


def assign_character_for_nodes(maze_map, current_node, prev_node):
    """Function to assign character for the visited nodes. Please assign
    meaningful characters based on the direction of tree traversal.

    Parameters
    ----------
    maze_map : [type]
        [description]
    current_node : [type]
        [description]
    prev_node : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """


    raise NotImplementedError


def write_to_file(file_name,print_file,file_path):
    """Print the final output of the search algorithm of all the goals

    Parameters
    ----------
    filen_name : string
        This parameter defines the name of the txt file.

    print_file: list
        This is the nested list containig the traversed paths
    path : string
        Location of the folder to be saved

    """

    
    
    try:
        map_nos=len(print_file)
        
        f=open(file_path+file_name,'x') ##Open/Create a file to store data
        
        ##Join all the elements in the matrix together so that it can be printed on a textfile    
        for row_num,row_value in enumerate(print_file[0]):  
            current_line=''.join((print_file[0])[row_num])      
            f.write(current_line+'\n')

        f.close()   
    except :
        
        print("\n Maps already exist in results folder \n")
    
    


def find_valid_neighbours(maze_map,x,y,queue,visited,max_row,max_col):

    
    
        
     
    


    
    return None





    



    
    
