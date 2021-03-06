import pandas as pd
import numpy as np

count = 0
arr = [3,9,8,4,6,10,2,5,7,1]

#df = pd.read_csv(r'C:\Pers\Educational\Algorithm Design and Analysis\Programming Assignment 2\100.txt', names = ['ints'])
#df = np.loadtxt(r'C:\Pers\Educational\Algorithm Design and Analysis\Programming Assignment 2\100.txt', delimiter = '\n')
#df = df[:10]
#s = df['ints']
#arr = s.tolist()

####################################################################################################################################################################
def quick_sort_1(arr):
	l = len(arr)
	if l <= 1:
		return arr
	p = arr[0]
	print 'pivot = ', p
	global count
	count = count + (l-1)
	print 'count = ', count
	i = 1 
	# i is the first element of the right side of the partitioned array
	for j in range(1, l):
		if arr[j] <= p:
			c = arr[j]
			arr[j] = arr[i]
			arr[i] = c
			i += 1
	#q,r = divmod((l-1), 2) 
	#l_arr = arr[1:q+1]
	#r_arr = arr[q+1:]
	l_arr = arr[1:i]
	r_arr = arr[i:]
	print 'left array = ', l_arr, ' | ', 'right array = ', r_arr
	# quick sort the left array
	l_arr_sorted = quick_sort_1(l_arr)
	
	r_arr_sorted = quick_sort_1(r_arr)
	
	result_array = l_arr_sorted + [p] + r_arr_sorted
	return result_array

######################################################################################################

def quick_sort_2(arr):
	
	l = len(arr)
	if l <= 1:
		return arr
	print 'subarray = ', arr
	# swap the 1st and the last elements of the array
	temp = arr[0]
	arr[0] = arr[-1]
	arr[-1] = temp
	
	
	p = arr[0]
	print 'pivot = ', p
	global count
	count = count + (l-1)
	#print 'count = ', count
	i = 1 
	# i is the first element of the right side of the partitioned array
	for j in range(1, l):
		if arr[j] <= p:
			c = arr[j]
			arr[j] = arr[i]
			arr[i] = c
			i += 1
	#q,r = divmod((l-1), 2) 
	#l_arr = arr[1:q+1]
	#r_arr = arr[q+1:]
	l_arr = arr[1:i]
	r_arr = arr[i:]
	print l_arr, ' | ', r_arr, ': ', 'comparisons ', l-1

	# quick sort the left array
	l_arr_sorted = quick_sort_2(l_arr)
	
	r_arr_sorted = quick_sort_2(r_arr)
	
	result_array = l_arr_sorted + [p] + r_arr_sorted
	return result_array
	'''
	l = len(arr)
	if l <= 1:
		return arr
	p = arr[0]

	global count
	count = count + (l-1)
	i = 0 
	# i is the first element of the right side of the partitioned array
	for j in range(0, l-1):
		if arr[j] <= p:
			c = arr[j]
			arr[j] = arr[i]
			arr[i] = c
			i += 1
	#q,r = divmod((l-1), 2) 
	#l_arr = arr[1:q+1]
	#r_arr = arr[q+1:]
	l_arr = arr[0:i]
	r_arr = arr[i:l-1]
	# quick sort the left array
	l_arr_sorted = quick_sort_2(l_arr)

	r_arr_sorted = quick_sort_2(r_arr)

	result_array = l_arr_sorted + [p] + r_arr_sorted
	return result_array
	'''

######################################################################################################	
def quick_sort_3(arr):
	l = len(arr)
	s = pd.Series(arr, name = 'int')
	if l <= 1:
		return arr
	#choose the pivot based on the steps given in the problem.
	q,r = divmod(l-1, 2) # locate the "middle" element

	#find the median among the first, middle and last elements of the array
	s1 = s.ix[[0,q,l-1]]
	s1.sort()
	p_idx = s1.index.values[1] # p_idx is the index of the median element / pivot.
	#p = s1[p_idx] # the middle element is the median and also our pivot.

	#swap the pivot with the first element.
	temp = arr[p_idx]
	arr[p_idx] = arr[0]
	arr[0] = temp
	
	# Start of the partition subroutine
	p = arr[0]
	global count
	count = count + (l-1)
	i = 1 
	# i is the first element of the right side of the partitioned array
	for j in range(1, l):
		if arr[j] <= p:
			c = arr[j]
			arr[j] = arr[i]
			arr[i] = c
			i += 1
	#q,r = divmod((l-1), 2) 
	#l_arr = arr[1:q+1]
	#r_arr = arr[q+1:]
	l_arr = arr[1:i]
	r_arr = arr[i:]
	# quick sort the left array
	l_arr_sorted = quick_sort_3(l_arr)
	
	r_arr_sorted = quick_sort_3(r_arr)
	
	result_array = l_arr_sorted + [p] + r_arr_sorted
	return result_array
	
	
	
	
	
	
	
	
	
	
	
	
	
	
