# Return true if there exists a subsequence of A[0..n] with given sum
def subsetSum(A, n, sum):

	# return true if sum becomes 0 (subset found)
	if sum == 0:
		return True

	# base case: no items left or sum becomes negative
	if n < 0 or sum < 0:
		return False

	# Case 1. include current item in the subset (A[n]) and recur
	# for remaining items (n - 1) with remaining sum (sum - A[n])
	include = subsetSum(A, n - 1, sum - A[n])

	# Case 2. exclude current item n from subset and recur for
	# remaining items (n - 1)
	exclude = subsetSum(A, n - 1, sum)

	# return true if we can get subset by including or excluding the
	# current item
	return include or exclude


# Subset Sum Problem
if __name__ == '__main__':

	# Input: set of items and a sum
	A = [7, 3, 2, 5, 8]
	sum = 14

	print("Yes" if subsetSum(A, len(A) - 1, sum) else "No")
