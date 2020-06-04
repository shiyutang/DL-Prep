# Python3 program to illustrate 
# recursive approach to ternary search 
  
# Function to perform Ternary Search 
def ternarySearch(l, r, key, ar): 
    if (r >= l): 
        # Find the mid1 and mid2 
        mid1 = l + (r - l) //3
        mid2 = r - (r - l) //3
  
        # Check if key is present at any mid 
        if (ar[mid1] == key):  
            return mid1 
          
        if (ar[mid2] == key):  
            return mid2 
          
        if (key < ar[mid1]):  
            return ternarySearch(l, mid1 - 1, key, ar) 
        elif (key > ar[mid2]):  
            return ternarySearch(mid2 + 1, r, key, ar) 
        else:  
            return ternarySearch(mid1 + 1,  
                                 mid2 - 1, key, ar) 
    return -1
  
  
# Get the array sorted
ar = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 

# Starting index 
l = 0
# length of array 
r = 9
# Key to be searched in the array 
key = 5
  
# Search the key using ternarySearch 
p = ternarySearch(l, r, key, ar) 
print("Index of", key, "is", p) 
