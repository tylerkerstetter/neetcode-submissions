class Solution {
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
        return nums;
    }

    // Helper method to recursively sort the array
    private void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(arr, low, high);
            
            // Recursively sort elements before and after partition
            quickSort(arr, low, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, high);
        }
    }

    // The partition method
    private int partition(int[] arr, int low, int high) {
        // 1. Pick the middle element as the pivot to avoid worst-case on sorted arrays
        int mid = low + (high - low) / 2;
        int pivot = arr[mid];
        
        // 2. Move the pivot out of the way to the end of the current segment
        swap(arr, mid, high);
        
        // 3. i keeps track of the boundary for elements smaller than the pivot
        int i = low;
        
        // 4. Iterate through the segment and move smaller elements to the left
        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                swap(arr, i, j);
                i++;
            }
        }
        
        // 5. Move the pivot back to its correct, sorted position
        swap(arr, i, high);
        
        return i; // Return the final index of the pivot
    }

    // Helper method to swap two elements in the array
    private void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}