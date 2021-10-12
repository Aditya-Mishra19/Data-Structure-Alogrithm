// C program for insertion sort

#include <math.h>
#include <stdio.h>

// function to sort an array using Insertion sort.
void insertionSort(int arr[], int n)
{
	int i, key, j;
	for (i = 1; i < n; i++) {
		key = arr[i];
		j = i - 1;

		/* Compare the key with i - 1 element, if element
           is greater then key it will swap the position. */
		while (j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}

// printArray is a function to print an array of size n.
void printArray(int arr[], int n)
{
	int i;
    printf("Sorted array : \n");
	for (i = 0; i < n; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

// Driver program to test insertion sort.
int main()
{
	int arr[] = { 50, 30, 40, 10, 20 };
	int n = sizeof(arr) / sizeof(arr[0]);

    // Calling Functions.
	insertionSort(arr, n); 
	printArray(arr, n);

	return 0;
}
/* This code is contributed by Aditya Mishra */