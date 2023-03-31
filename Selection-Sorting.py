class Solution:
    def select(self, arr, i):
        mini = i
        for j in range(i, n):
            if arr[j] < arr[mini]:
                mini = j
        return mini

    def selectionSort(self, arr, n):
        for i in range(n):
            mini = i
            x=self.select(arr,mini)
            arr[i], arr[x] = arr[x], arr[i]
