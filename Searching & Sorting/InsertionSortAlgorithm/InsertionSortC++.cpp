// C++ program for insertion sort

#include <bits/stdc++.h>
using namespace std;

// function to sort an array using Insertion sort.
void insertionSort(int arr[], int n)
{
	int i, key, j;
	for (i = 1; i < n; i++)
	{
		key = arr[i];
		j = i - 1;

		/* Compare the key with i - 1 element, if element
        is greater then key it will swap the position. */
		while (j >= 0 && arr[j] > key)
		{
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
    cout << "Sorted array : " << endl;
	for (i = 0; i < n; i++)
		cout << arr[i] << " ";
}

// Driver program to test insertion sort.
int main()
{
	int arr[] = { 50, 30, 40, 10, 20 };
	int n = sizeof(arr) / sizeof(arr[0]);

    // Calling function
	insertionSort(arr, n);
	printArray(arr, n);

	return 0;
}

// This is code is contributed by Aditya Mishra.
