# Values (stored in list v)
# Weights (stored in list w)
# Number of distinct items (n)
# Knapsack capacity W
def knapSack(v, w, n, W):

	# base case: Negative capacity
	if W < 0:
		return float('-inf')

	# base case: no items left or capacity becomes 0
	if n < 0 or W == 0:
		return 0

	# Case 1. include current item n in Knapsack (v[n]) and recur for
	# remaining items (n - 1) with decreased capacity (W - w[n])
	include = v[n] + knapSack(v, w, n - 1, W - w[n])

	# Case 2. exclude current item n from Knapsack and recur for
	# remaining items (n - 1)
	exclude = knapSack(v, w, n - 1, W)

	# return maximum value we get by including or excluding current item
	return max(include, exclude)


# 0-1 Knapsack problem
if __name__ == '__main__':

	# Input: set of items each with a weight and a value
	v = [20, 5, 10, 40, 15, 25]
	w = [1, 2, 3, 8, 7, 4]

	# Knapsack capacity
	W = 10

	print("Knapsack value is", knapSack(v, w, len(v) - 1, W))
