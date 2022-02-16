#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:49:06 2018


@author of final code : Malika Navaratna
@author of template: iswariya
"""
import copy
import math
import random
import matplotlib.pyplot as plt




def plot_cost_function(cost):
    """ Function to plot the no. of iterations (x-axis) vs
    cost (y-axis). X-axis of the plot should contain xticks
    from 0 to 10000 in steps of 2000.
    Use matplotlib.pyplot to generate the plot as .png file and store it
    in the results folder. An example plot is
    there in the results folder.

    Parameters
    ----------
    cost : [type]
        [description]
    """
   
    plt.plot(cost)
    plt.show()


def get_successors(curr_seq):
    """ Function to generate a list of 100 random successor sequences
    by swapping any TWO cities randomly. Please note that the first and last city
    should remain unchanged since the traveller starts and ends in
    the same city. 

    Parameters
    ----------
    curr_seq : list
        Take in the current state(path of cities)

    Returns
    -------
    successor_seq
        List of randomized paths(keeping the start and end city the same)
    """
    sequence=copy.deepcopy(curr_seq)
    successor_seq=[]##Create an empty list to store all the 100 random orders
    
    ##Iterate for 100 to create to random samples
    for _ in range(0,100):
        current_rand=copy.deepcopy(sequence)# Create a temporary copy of the sequence
        random_cities=random.sample(current_rand[1:-1],2) # Choose two cities at random
        p1=current_rand.index(random_cities[0]) # Index cities
        p2=current_rand.index(random_cities[1])
        
        current_rand[p1]=random_cities[1] # Swapping city values
        current_rand[p2]=random_cities[0]
        successor_seq.append(current_rand)

    
    return successor_seq


def get_total_distance(distance_matrix, seq):
    """ Function to get the distance while travelling along
    a particular sequence of cities.
    HINT : Keep adding the distances between the cities in the
    sequence by referring the distances from the distance matrix

    Parameters
    ----------
    distance_matrix : [dictionary with floats]
        [the dictionary with all the distance values]
    seq : [list]
        [list of cities in order in which they are visited]

    Returns
    -------
    total_distance
    [float]
        [the total distance it takes to traverse the entire path]
    """
    current_seq=copy.deepcopy(seq)
    total_distance=sum([distance_matrix[current_seq[i],current_seq[i+1]] for i in range(len(current_seq)-1)])


    #Does not caluculate the final strech of the distance from the end point to starting point

    return total_distance


def get_distance_matrix(coordinates):
    """ Function to generate a distance matrix. The distance matrix
    is a square matrix.
    For eg: If there are 3 cities then the distance
    matrix has 3 rows and 3 colums, with each city representing a row
    and a column. Each element of the matrix represents the euclidean
    distance between the coordinates of the cities. Thus, the diagonal
    elements will be zero (because it is the distance between the same city).

    Parameters
    ----------
    coordinates : [list]
        list of all coordinates of the cities

    Returns
    -------
    distance_matrix: [dictionary(nested) of float values]
        distance between each pair of cities
    """
    # coordinates=int(coordinates)
    current_coordinates=copy.deepcopy(coordinates)
    distance_matrix={}
    for i,p1 in enumerate(current_coordinates):
        for j,p2 in enumerate(current_coordinates):
            distance_matrix[i,j]=(((float(p1[0])-float(p2[0]))**2)+((float(p1[1])-float(p2[1]))**2))**0.5



    

    return distance_matrix
