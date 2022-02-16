#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 11:04:22 2018
@author of final code : Malika Navaratna
@author of template: iswariya
"""
import argparse
import os
import random
import timeit
import helper
import copy


def hill_climb_steepest_descent(start_seq, distance_matrix):
    """ Function to implement steepest descent hill climbing algorithm
    for the travelling salesman problem.
    Run the hill climbing algorithm for 10000 iterations and
    print the results for every 2000 iterations.
    Please use the functions in helper.py to complete the algorithm.
    Please do not clutter the code this file by adding extra functions.
    Additional functions if required should be added in helper.py

    Parameters
    ----------
    start_seq : [type]
        [description]
    distance_matrix : [type]
        [description]

    Returns
    -------
    [type]
    """

    best_cost = float('inf')
    best_seq = None
    cost = []
    seen_states = []
    curr_seq = start_seq
    curr_seq.append(start_seq[0])
    curr_dist = 0
    restarts_count = 0

    ##Get the distance matrix that contain all possible combinations of distances
    distance_matrix=helper.get_distance_matrix(coordinates)

    #Set overall best for initial values
    best_cost=helper.get_total_distance(distance_matrix,curr_seq)
    best_seq=curr_seq

    
    current_best_cost=float('inf')

    for _ in range(0,10000):

        cost.append(current_best_cost)
               
        ##Create new random states when it becomes 20000
        if restarts_count%2000==0 and (restarts_count>1):
            print(f'Staring new random sequence at itertion {restarts_count}')
            print(f'Current best cost {best_cost}')
            temp_list=copy.deepcopy(curr_seq)
            temp_list.pop()
            temp_list=random.sample(temp_list,len(temp_list))
            temp_list.append(temp_list[0])
            curr_seq=temp_list
            current_best_cost = float('inf')
            
            

        

        neighbours=helper.get_successors(curr_seq)

        for neighbour in neighbours:
            curr_dist=helper.get_total_distance(distance_matrix,neighbour)
            if curr_dist<current_best_cost:
                current_best_cost=curr_dist
                curr_seq=neighbour                
                


        if current_best_cost<best_cost:
            best_cost=current_best_cost
            best_seq=curr_seq
              
        


        restarts_count+=1
    


    return best_cost, best_seq,cost


if __name__ == '__main__':

    # Reading txt file from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', type=str)
    args = parser.parse_args()
    file_path = os.path.join(os.getcwd(), args.filename)
    with open(file_path) as file:
        data = file.readlines()

    # Getting the list of cities and their coordinates
    list_of_cities = [i.strip().split(',') for i in data]
    city_names = [row[0] for row in list_of_cities[1:]]
    coordinates = [[row[1], row[2]] for row in list_of_cities[1:]]

    # Generating a random soln.
    random_seq = random.sample(range(0, len(list_of_cities[1:])),
                               len(list_of_cities[1:]))

    # Calculating the least dist using steepest descent hill climbing
    start_time = timeit.default_timer()
    least_distance, best_seq,cost = hill_climb_steepest_descent(random_seq,
                                                           coordinates)
    end_time = timeit.default_timer()

    # print("Best Sequence:", best_seq)
    print(" \n \n Best Sequence:")
    for name in best_seq:
        print(city_names[name])
    print("\n Least distance from Steepest Ascent:", least_distance)
    print("Time: {}s".format(end_time-start_time))
    helper.plot_cost_function(cost)
