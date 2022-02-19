# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims, i, j):

	# base case: one matrix
	if j <= i + 1:
		return 0

	# stores minimum number of scalar multiplications (i.e., cost)
	# needed to compute the matrix M[i+1]...M[j] = M[i..j]
	min = float('inf')

	# take the minimum over each possible position at which the
	# sequence of matrices can be split

	"""
		(M[i+1]) x (M[i+2]..................M[j])
		(M[i+1]M[i+2]) x (M[i+3.............M[j])
		...
		...
		(M[i+1]M[i+2]............M[j-1]) x (M[j])
	"""

	for k in range(i + 1, j):

		# recur for M[i+1]..M[k] to get an i x k matrix
		cost = MatrixChainMultiplication(dims, i, k)

		# recur for M[k+1]..M[j] to get a k x j matrix
		cost += MatrixChainMultiplication(dims, k, j)

		# cost to multiply two (i x k) and (k x j) matrix
		cost += dims[i] * dims[k] * dims[j]

		if cost < min:
			min = cost

	# return min cost to multiply M[j+1]..M[j]
	return min


if __name__ == '__main__':

	# Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
	# input is 10 × 30 matrix, 30 × 5 matrix, 5 × 60 matrix
	dims = [10, 30, 5, 60]

	print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1))
