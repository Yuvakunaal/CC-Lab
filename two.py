# Task - 1
# Perform Linear search

import random
class Search:
    def linear_search(self,arr,element):
        print("\nLinear Searching...")
        print(f"Searching = {element}")
        for i in range(len(arr)):
            if arr[i] == element:
                return f"Element found at index = {i}"
        return "Not found"
    
    def binary_search(self,arr,element):
        print("\nBinary Searching...")
        print(f"Searching = {element}")
        arr.sort()
        left,right = 0,len(arr)-1
        while left <= right:
            mid = (left + right)//2
            if arr[mid] == element:
                return f"Element found at index = {mid}"
            elif arr[mid] < element:
                left = mid + 1
            else:
                right = mid - 1
        return "Not Found"
    
def runSearch():
    search = Search()
    arr = eval(input("Enter array : "))
    element = random.randint(0,10)
    print(f"{search.linear_search(arr,element)}")
    print(f"{search.binary_search(arr,element)}")
# runSearch()

class Sort:
    def Bubble_sort(self,arr1):
        print(f"\nBubble sorting...{arr1}")
        arr = arr1.copy()
        for i in range(len(arr)-1):
            for j in range(0,len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
        return arr
    
    def Selection_sort(self,arr1):
        print(f"\nSelection sorting...{arr1}")
        # arr = arr1.copy()
        # for i in range(len(arr)):
        #     min_index = i
        #     for j in range(i,len(arr)):
        #         if arr[min_index] > arr[j]:
        #             min_index = j
        #             arr[i],arr[min_index] = arr[min_index],arr[i]
        arr = arr1.copy()
        n = len(arr)
        for i in range(n):
            a = arr.index(min(arr[i:]))
            arr.insert(i,arr.pop(a))
        return arr
    
    def Insertion_sort(self,arr1):
        print(f"\nInsertion sorting...{arr1}")
        arr = arr1.copy()
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                arr[j + 1] = key
        return arr

def runSort():
    sort = Sort()          
    arr = eval(input("Enter array : "))
    print(f"Sorted array = {sort.Bubble_sort(arr)}")
    print(f"Sorted array = {sort.Selection_sort(arr)}")
    print(f"Sorted array = {sort.Insertion_sort(arr)}")
runSort()