from numpy import *
import pandas as pd
import random
#############################################################################
def get_cut(df, V):
	while len(V) > 2:
		# Pick an edge uniformly at random
		idx = random.choice(df.index.values)
		#print 'random index: ', idx
		merged_node = df.get_value(idx, 'Node1')
		discarded_node = df.get_value(idx, 'Node2')
		# Find all edges where Node1 = discarded_node and change the value to the merged_node.
		df.ix[df.Node1 == discarded_node, 'Node1'] = merged_node
		# Find all edges where Node2 = discarded_node and change the value to the merged_node.
		df.ix[df.Node2 == discarded_node, 'Node2'] = merged_node
		# delete all self loops
		cond = df['Node1'] <> df['Node2']
		df = df[cond]
		V = set(df['Node1'].unique()).union(df['Node2'].unique())
			
	this_cut = len(df.index)
	return this_cut
############################################################################

f = open(r'C:\Pers\Educational\Algorithm Design and Analysis\Programming Assignment 3\kargerMinCut.txt')
edges = []

for line in f:
	row = line.split()
	for i in range(1, len(row)):
		if int(row[0])<int(row[i]):
			edges.append([int(row[0]), int(row[i])])

df_main = pd.DataFrame(edges, columns = ['Node1', 'Node2'])
# The universal set of all vertices in the graph
V_main = set(df_main['Node1'].unique()).union(df_main['Node2'].unique())
n = len(V_main)
min_cut = len(df_main.index)
# only works for n >2
for i in range(20):#range(int(floor(n**2*log(n)))):
	print i
	df = df_main.copy()
	V = V_main
	#initialize the random number generator for every trial to ensure a different seed for each trial
	random.seed()
	if len(V) > 2:
		this_cut = get_cut(df, V)
		if this_cut < min_cut:
			min_cut = this_cut
		#print 'min_cut: ', min_cut
	
print 'final min cut: ', min_cut
