# Task - 1
# 1. Define an array and operations on array such as 
# a) Traversal b) Insertion c) Deletion d) Search e) Update

# Code :-
class Array :
    def __init__(self,array):
        self.array = array
    def traversal(self):
        print("\nTravelling : ")
        for i in self.array:
            print(i)
    def insertion(self,position,element):
        print("\nInserting :-")
        if len(self.array) < position :
            print("Cant insert : position not exist in array")
            return
        self.array.insert(position,element)
        print("Inserted successfully...")
        return
    def deletion_at_index(self,position):
        print("\nDeleting element using index :-")
        if not self.array:
            print("Cant delete : array size = 0")
            return
        a = self.array.pop(position)
        print(f"deleted successfully (index = {a})")
        return
    def deletion_at_value(self,element):
        print("\nDeleting element :-")
        if not self.array:
            print("Cant delete : array size = 0")
            return
        if element in self.array:
            a = self.array.pop(self.array.index(element))
            print(f"deleted successfully (element = {a})")
            return
        print("Cant delete : Element not found !")
        return
    def search(self,element):
        print("\nSearching :-")
        if not self.array:
            print("Cant Search : array size = 0")
            return
        if element in self.array:
            print(f"{element} found at index = {self.array.index(element)}")
            return
        print("Element not found in array !")
        return
    def update(self,position,element):
        print("\nUpdating :-")
        if not self.array:
            print("Cant Update : array size = 0")
            return
        if len(self.array) < position :
            print("Cant Update : position not exist in array")
            return
        self.array[position] = element
        print(f"Updated = {element} at index = {position}")
        return
    def display(self):
        print(f"\nArray = {self.array}")

def runTask1():
    a = eval(input("Enter array : "))
    array = Array(a)
    array.traversal()
    array.insertion(1,6)
    array.deletion_at_index(0)
    array.deletion_at_value(4)
    array.search(3)
    array.update(2,200)
    array.display()
# runTask1()

# Task - 2 
# Write a python program to find the largest element in an array using function

# Code :-
def findmax(array):
    if not array:
        print("Empty array !")
        return "None"
    m = array[0]
    for i in range(0,len(array)):
        if array[i] > m:
            m = array[i]
    return m
def runTask2():
    a = eval(input("Enter array : "))
    res = findmax(a)
    print(res)
# runTask2()

# Task - 3
# Write a python program to find factors of a number

# Code :-
def factors(num):
    a = [i for i in range(1,num+1) if num%i==0]
    return a
def runTask3():
    a = int(input("Emter number : "))
    res = factors(a)
    print(res)
runTask3()