#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return arr[i]
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            minimumIndex = i
            for j in range(i+1, n):
                if arr[j] < arr[minimumIndex]:
                    minimumIndex=j
                    
            element , arr[i]=arr[i],arr[minimumIndex]
            arr[minimumIndex]= element
            
        return arr
            
