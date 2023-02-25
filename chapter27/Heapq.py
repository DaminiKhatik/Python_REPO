#Largest and smallest items in a collection
import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8] 
print(heapq.nlargest(5, numbers)) 
print(heapq.nsmallest(5, numbers)) 


#Smallest item in a collection
import heapq
numbers = [10, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.heapify(numbers) 
print(numbers) 