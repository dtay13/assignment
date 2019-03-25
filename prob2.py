#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:35:54 2019

@author: dtay
"""

import pandas as pd
import numpy as np
   
from collections import defaultdict

class Graph: 
   
    def __init__(self,num_vertices): 
        #No. of vertices 
        self.V=num_vertices
        # stores graph in to a dictionary of keys:vertices, value: list of adj vertices
        self.graph = defaultdict(list)  
   
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    '''Given a source and a destination, finds, next adjacent node
    to destination. Function is recursively called until a path is found.
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    
    ## BUG HERE, calling the recursive  function doesnt work because the state of
    # of the graph (which are visited and which are not) is important and has to
    # be passed.
    def find_next(self, s, d, visited, path, traj):
        # Mark the current node as visited and store in path 
        visited[s]= False
        path.append(s)
        # If current vertex is same as destination, then print 
        # current path[] 
        if s==d and len(path)!=1:
            traj.append(path)
            print(path)
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[s]: 
                if visited[i]==False and len(path)<15:
                    path, traj = self.find_next(i, d, visited, path=path, traj=traj)
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop()
        visited[s]= False
        return path, traj
   
    # Wrap into a runner
    def find_paths(self,s, d, path=[], traj=[]): 
        # Initializing
        visited =[False]*(self.V) 
        # Find path until conditions are met
        _, paths = self.find_next(s, d,visited, path=path, traj=traj)
        return paths

# Read Data
data =pd.read_csv("data_Problem2.csv")

# Some data exploration
set(data["TO_NODE"]).union(set(data["FROM_NODE"]))

# Rename the blank node to a new node = "0" because it leads to nowhere anyway
data = data.fillna(0)

# Some data exploration
max_ = max(set(data["TO_NODE"]).union(set(data["FROM_NODE"])))+1

#TODO: Hashing, if I have time, for now since there is no space constraint,
#       just use brute max.

# Create a graph
g = Graph(max_) 

# Initialize the dist
dist = np.zeros([max_,max_])
# Build the graph
graph = defaultdict(list)

# Build both the graph and the dist
G = data[["FROM_NODE","TO_NODE","VALUE"]].values
for row in G:
    dist[int(row[0]),int(row[1])]=row[2]
    g.addEdge(int(row[0]),int(row[1]))
    
for i in range(max_):
    traj = g.find_paths(i, i)
    print(traj)


