#########################################################
#														#
#		Counting inversions in an unsorted array		#
#														#
#########################################################

import pandas as pd
import numpy as np
from __future__ import division

#inv_count = 0
#arr = [2,1,4,6,3,9]
#sorted_array_left = [1,2,4]
#sorted_array_right = [3,6,9]

def count_inversions(unsorted_array):

	#sorted_array_left = [1,2,4]
	#sorted_array_right = [3,6,9]
	l = len(unsorted_array)
	if l == 0 or l == 1: #or len(sorted_array_right) == 0 or len(sorted_array_right) == 1:
		return 0, unsorted_array
	#Divide into sub arrays....
	if l%2 == 0: #even length array
		array_left = unsorted_array[:int(l/2)]
		array_right = unsorted_array[int(l/2):]
	else:
		array_left = unsorted_array[:int((l+1)/2)]
		array_right = unsorted_array[int((l+1)/2):]
		
	#print  'left array: ', array_left
	#print 'right_array: ', array_right
	
	left_inv_count, sorted_array_left = count_inversions(array_left)
	right_inv_count, sorted_array_right = count_inversions(array_right)
	
	#print 'sorted left array: ', sorted_array_left
	#print 'sorted right array: ', sorted_array_right
	
	#calculating the split inversions
	merged_arr = []
	#sorted_array_left = [3,6]
	#sorted_array_right = [9]
	split_inv_count = 0
	i = 0
	j = 0
	len_left = len(sorted_array_left)
	len_right = len(sorted_array_right)
	for k in range(len_left + len_right):
		if sorted_array_left[i] < sorted_array_right[j]:
			merged_arr.append(sorted_array_left[i])
			#split_inv_count += len(sorted_array_right[j:])
			i += 1
			#print 'i = ', i
		elif sorted_array_left[i] > sorted_array_right[j]:
			merged_arr.append(sorted_array_right[j])
			split_inv_count += len(sorted_array_left[i:])
			j += 1
			#print 'j = ', j
		else:
			merged_arr.append(sorted_array_left[i])
			#split_inv_count += len(sorted_array_right[j:])
			i += 1
		if i == len_left:
			merged_arr = merged_arr + (sorted_array_right[j:])
			break
		elif j == len_right:
			merged_arr = merged_arr + (sorted_array_left[i:])
			break

	
	#print 'split inversions: ', split_inv_count
	#print '************************************'
	return (left_inv_count + right_inv_count + split_inv_count) , merged_arr
		
#f = open(r'C:\Pers\Educational\Algorithm Design and Analysis\Programming Assignment 1\IntegerArray_test.txt')
#s = f.read()
#l = s.split()

df = pd.read_csv(r'C:\Pers\Educational\Algorithm Design and Analysis\Programming Assignment 1\IntegerArray.txt', names = ['int'])
l = df['int'].tolist()
x , y = count_inversions(l)
	
