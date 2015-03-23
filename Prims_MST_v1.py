# Implementing Prim's Minimum Spanning Tree Algorithm using Adjacency Lists
'''
The input file describes an undirected graph with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is an edge 
connecting vertex #2 and vertex #3 that has cost -8874. The below algorithm assumes that the 
graph has no parallel edges. No assumption are made about the edge costs being positive, or 
being distinct.
'''

import pandas as pd
from numpy import *

def get_MST(path):
	#test the Algo with a toy dataset
	#arr = array([[1,2,-2], [2,3,3], [3,4, 5], [4,1,-6], [1,3,-4]])
	#df_e_to_v = pd.DataFrame(arr,  columns = ['Node1', 'Node2', 'cost'])

	# List of edge to vertices mappings
	df_e_to_v = pd.read_csv(path, sep = ' ', header = 0, skiprows = 1, names = ['Node1', 'Node2', 'cost'])

	left_nodes = df_e_to_v['Node1'].unique()
	right_nodes = df_e_to_v['Node2'].unique()
	''' Edge to vertex mapping
	  Node1  Node2  cost
	0      1      2    -2
	1      2      3     3
	2      3      4     5
	3      4      1    -6
	4      1      3    -4
	'''
	# List of All vertices
	V = pd.Series(append(left_nodes, right_nodes)).unique().tolist()
	set_V = set(V) # create an unordered set of the unique values in V

	# List of all edges
	E = df_e_to_v.index.tolist()

	#Initializing the Algorithm
	# List of examined Vertices
	X = []
	# Edges in the spanning tree-so-far
	T = []
	# Start with the first vertex arbitrarily.
	x = V[0]
	X.append(x)

	#Find the edges (e) with one end (u) in X and the other (v) outside of X.
	f = lambda x: True if x in X else False

	# Assuming a connected graph
	while set(X) <> set(V):

		#indexes of edges that have Node1 in X
		set_n1_in_X = set(df_e_to_v[df_e_to_v['Node1'].map(f)].index.tolist())
		#indexes of edges that have Node2 in X
		set_n2_in_X = set(df_e_to_v[df_e_to_v['Node2'].map(f)].index.tolist())

		#indexes of edges that have either Node1 in X or Node2 in X but not both (XOR).
		set_ = set_n1_in_X ^ set_n2_in_X
		list_ = list(set_)
		# find the index of the edge that has the minimum cost. Since the way the graph is represented 
		# the index of the edge is also the identifier of the edge. Therefore this is all we need.
		t = df_e_to_v.ix[list_]['cost'].idxmin()
		#add the edge with the minimum cost to the MST-so-far.
		T.append(t)
		# find the two ends of t and add the one to X that is not already in X.
		n1 = df_e_to_v.ix[t]['Node1']
		n2 = df_e_to_v.ix[t]['Node2']
		if n1 not in X:
			X.append(n1)
		else:
			X.append(n2)

	#Calculate the cost of the min spanning tree
	cost = df_e_to_v.ix[T]['cost'].sum()
	
	return T, cost
	
def main():
	file_path = r'C:\Pers\Educational\Algorithm Design and Analysis - II\ProgAss1_data_q3.txt'
	tree, edge_cost = get_MST(file_path)
	print 'the total edge cost of the MST is ', edge_cost

%time main()
