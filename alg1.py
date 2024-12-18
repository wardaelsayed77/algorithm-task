def heap_sort(list1):
    n = len(list1)
    for i in range(n // 2 - 1, -1, -1):
       list_heap_sorted(list1, n, i)

    for i in range(n - 1, 0, -1):
        list1[i], list1[0] = list1[0], list1[i]  
      
        list_heap_sorted(list1, i, 0)  
        
def list_heap_sorted(list1, n, i):
    large = i  
    l = 2 * i + 1 
    r = 2 * i + 2  
    if l < n and list1[l] > list1[large]:
       large = l
    if r < n and list1[r] >list1[large]:
      large = r
    if large != i:
        list1[i], list1[large] = list1[large], list1[i]
        list_heap_sorted(list1, n, large)

print(" Implementation of Heap Sort :")
list1 = [32,3,5,7,2,16,20,10,9]
print("Input Random List:", list1)
heap_sort(list1)
print("Sorted List:", list1)
