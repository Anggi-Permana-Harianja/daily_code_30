'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You are given an array of non-negative integers that represents a
 two-dimensional elevation map where each element is unit-width wall and the integer is the height. 
Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, 
and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

'''
trapped_water = minimum(tallest left hand wall, tallest right hand wall) - height tower
'''

input_walls1 = [2, 1, 2]
input_walls2 = [3, 0, 1, 3, 0, 5]
input_walls3 = [2, 0, 3, 0, 2]

def trapped_waters(input_walls):
	highest_wall = max(input_walls)
	idx_highest_wall = input_walls.index(highest_wall)
	limit_wall_left = min(input_walls[0], highest_wall)
	limit_wall_right= min(input_walls[-1], highest_wall)
	sum_trapped_waters = 0

	for i in range(len(input_walls)):
		if i < idx_highest_wall:
			sum_trapped_waters += limit_wall_left - input_walls[i]
		elif i > idx_highest_wall:
			sum_trapped_waters += limit_wall_right - input_walls[i]

	return sum_trapped_waters

print(trapped_waters(input_walls1)) #--> 1
print(trapped_waters(input_walls2)) #--> 8
print(trapped_waters(input_walls3)) #--> 4