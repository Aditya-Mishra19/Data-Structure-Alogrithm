class Heap:

	def heapify(self, arr, n, i):
		largest = i 
		left = 2*i + 1
		right = 2*i + 2

		if left < n and arr[i] < arr[left]:
			largest = left
		if right < n and arr[largest] < arr[right]:
			largest = right
		#if root is not largest, swap with largest and
		#continue heapify
		if largest != i:
			arr[i], arr[largest] = arr[largest], arr[i]
			self.heapify(arr, n, largest)

	def buildMaxHeap(self, arr, n):
		for i in range(n//2, -1, -1):
			self.heapify(arr, n, i)

	def heapsort(self, arr):

		n = len(arr)
		self.buildMaxHeap(arr, n)
		for i in range(n-1, 0, -1):
			arr[i], arr[0] = arr[0], arr[i]
			self.heapify(arr, i, 0)


arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
h = Heap()
h.heapsort(arr)
print(arr)
